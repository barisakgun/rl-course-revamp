#!/usr/bin/env python3
"""Minimal LaTeX -> native PowerPoint equation (OMML) converter for Claude-built decks.

Supports the subset used in lecture decks: letters/digits/operators, sub- and superscripts (x_t, x^{2}, x_a^b),
\\sum with limits, \\mathcal{S}, \\mathbb{E}, \\text{...}, \\Pr, \\{ \\}, \\mid, \\doteq, \\ldots, \\cdots,
Greek letters, primes, spacing commands. Unsupported commands raise ValueError, so a typo cannot silently produce
a wrong equation. The output is editable in PowerPoint's equation editor; the LaTeX source is kept in the slide
notes by the builder.

    math_paragraph(latex, size=24)  -> <a:p> holding a display equation (centred, no bullet)
    inline_math(latex, size=24)     -> <a14:m> element for use inside a text paragraph
    wrap_math_shapes(slide)         -> wraps shapes containing equations in mc:AlternateContent (required by PowerPoint)
"""
import copy
from lxml import etree

NS = {
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'm': 'http://schemas.openxmlformats.org/officeDocument/2006/math',
    'a14': 'http://schemas.microsoft.com/office/drawing/2010/main',
    'mc': 'http://schemas.openxmlformats.org/markup-compatibility/2006',
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
}
A, M, A14, MC = (f'{{{NS[k]}}}' for k in ('a', 'm', 'a14', 'mc'))

SYMBOLS = {
    'gamma': 'γ', 'pi': 'π', 'alpha': 'α', 'beta': 'β', 'delta': 'δ', 'epsilon': 'ε', 'lambda': 'λ', 'theta': 'θ',
    'rho': 'ρ', 'sigma': 'σ', 'mu': 'μ', 'tau': 'τ', 'infty': '∞', 'mid': '∣', 'doteq': '≐', 'ldots': '…',
    'cdots': '⋯', 'to': '→', 'times': '×', 'in': '∈', 'leq': '≤', 'geq': '≥', 'neq': '≠', 'approx': '≈',
    'cdot': '·', 'pm': '±', 'quad': ' ', 'qquad': '  ', ',': ' ', ';': ' ', ' ': ' ',
    '{': '{', '}': '}', 'lvert': '|', 'rvert': '|', 'prime': '′', 'leftarrow': '←', 'sum': '∑',
}
UPRIGHT_CMDS = {'Pr': 'Pr', 'max': 'max', 'min': 'min', 'arg': 'arg', 'log': 'log', 'exp': 'exp'}
CAL = {c: ch for c, ch in zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', '𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵')}
BB = {'E': '𝔼', 'R': 'ℝ', 'N': 'ℕ', 'P': 'ℙ'}


# ---------------------------------------------------------------- tokenizer / parser

def tokens(s):
    i = 0
    while i < len(s):
        c = s[i]
        if c == '\\':
            j = i + 1
            if j < len(s) and not s[j].isalpha():
                yield ('cmd', s[j]); i = j + 1; continue
            while j < len(s) and s[j].isalpha():
                j += 1
            yield ('cmd', s[i + 1:j]); i = j
        elif c in '{}_^':
            yield (c, c); i += 1
        elif c == ' ':
            i += 1                                     # LaTeX math ignores spaces
        else:
            yield ('chr', c); i += 1


class Parser:
    def __init__(self, s):
        self.t = list(tokens(s)); self.i = 0

    def peek(self):
        return self.t[self.i] if self.i < len(self.t) else (None, None)

    def take(self):
        tok = self.peek(); self.i += 1; return tok

    def group(self):
        """A braced group or a single atom (as after _ or ^)."""
        if self.peek()[0] == '{':
            self.take(); out = self.seq('}'); self.take(); return out
        return [self.atom()]

    def raw_group(self):
        assert self.take()[0] == '{', 'expected {'
        depth, out = 1, ''
        while True:
            k, v = self.take()
            if k is None:
                raise ValueError('unclosed {')
            if k == '{': depth += 1
            if k == '}':
                depth -= 1
                if depth == 0: return out
            out += ('\\' + v) if k == 'cmd' else v

    def atom(self):
        k, v = self.take()
        if k == 'chr':
            if v == "'":
                return ('t', '′', False)
            return ('t', v, not (v.isalpha() and v.isascii()))   # letters italic, others upright
        if k == '{':
            out = self.seq('}'); self.take(); return ('grp', out)
        if k == 'cmd':
            if v in ('mathcal', 'mathbb'):
                letters = self.raw_group()
                table = CAL if v == 'mathcal' else BB
                return ('t', ''.join(table[c] for c in letters), True)
            if v in ('text', 'mathrm', 'operatorname'):
                return ('t', self.raw_group(), True)
            if v in UPRIGHT_CMDS:
                return ('t', UPRIGHT_CMDS[v], True)
            if v == 'sum':
                return ('sum',)
            if v in ('left', 'right', 'big', 'Big'):
                return ('grp', [])
            if v in SYMBOLS:
                return ('t', SYMBOLS[v], v not in ('gamma', 'pi', 'alpha', 'beta', 'delta', 'epsilon', 'lambda',
                                                   'theta', 'rho', 'sigma', 'mu', 'tau'))
            raise ValueError(f'unsupported LaTeX command \\{v}')
        raise ValueError(f'unexpected token {k!r}')

    def seq(self, end=None):
        out = []
        while self.peek()[0] not in (None, end):
            if self.peek()[0] == '}' and end is None:
                raise ValueError('unbalanced }')
            base = self.atom()
            sub = sup = None
            while self.peek()[0] in ('_', '^'):
                k, _ = self.take()
                if k == '_': sub = self.group()
                else: sup = self.group()
            if base[0] == 'sum':
                body = self.seq(end)                       # \sum takes the rest of the expression
                out.append(('nary', sub or [], sup or [], body)); break
            out.append(('script', base, sub, sup) if (sub or sup) else base)
        return out


# ---------------------------------------------------------------- OMML emission

def _italic(text):
    """Math-italic Unicode letters, as PowerPoint's equation editor stores them (h is U+210E)."""
    out = []
    for ch in text:
        if 'a' <= ch <= 'z':
            out.append('\u210e' if ch == 'h' else chr(0x1D44E + ord(ch) - ord('a')))
        elif 'A' <= ch <= 'Z':
            out.append(chr(0x1D434 + ord(ch) - ord('A')))
        elif ch in GREEK_ITALIC:
            out.append(GREEK_ITALIC[ch])
        else:
            out.append(ch)
    return ''.join(out)


GREEK_ITALIC = {'α': '𝛼', 'β': '𝛽', 'γ': '𝛾', 'δ': '𝛿', 'ε': '𝜀', 'θ': '𝜃', 'λ': '𝜆', 'μ': '𝜇', 'π': '𝜋',
                'ρ': '𝜌', 'σ': '𝜎', 'τ': '𝜏'}


def _rpr(size, color, italic=False):
    r = etree.Element(A + 'rPr', lang='en-US', sz=str(int(size * 100)))
    if italic:
        r.set('i', '1')
    if color:
        f = etree.SubElement(r, A + 'solidFill'); etree.SubElement(f, A + 'srgbClr', val=color)
    etree.SubElement(r, A + 'latin', typeface='Cambria Math')
    return r


def _run(text, upright, size, color):
    r = etree.Element(M + 'r')
    if upright:
        mp = etree.SubElement(r, M + 'rPr'); etree.SubElement(mp, M + 'sty', {M + 'val': 'p'})
    r.append(_rpr(size, color, italic=not upright))
    t = etree.SubElement(r, M + 't'); t.text = text if upright else _italic(text)
    if text != text.strip():
        t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    return r


def _emit(items, parent, size, color):
    for it in items:
        kind = it[0]
        if kind == 't':
            parent.append(_run(it[1], it[2], size, color))
        elif kind == 'grp':
            _emit(it[1], parent, size, color)
        elif kind == 'script':
            _, base, sub, sup = it
            tag = 'sSubSup' if sub and sup else 'sSub' if sub else 'sSup'
            el = etree.SubElement(parent, M + tag)
            e = etree.SubElement(el, M + 'e'); _emit([base], e, size, color)
            if sub:
                s = etree.SubElement(el, M + 'sub'); _emit(sub, s, size, color)
            if sup:
                s = etree.SubElement(el, M + 'sup'); _emit(sup, s, size, color)
        elif kind == 'nary':
            _, sub, sup, body = it
            el = etree.SubElement(parent, M + 'nary')
            pr = etree.SubElement(el, M + 'naryPr')
            etree.SubElement(pr, M + 'chr', {M + 'val': '∑'})
            if not sup:
                etree.SubElement(pr, M + 'supHide', {M + 'val': '1'})
            s = etree.SubElement(el, M + 'sub'); _emit(sub, s, size, color)
            s = etree.SubElement(el, M + 'sup'); _emit(sup, s, size, color)
            e = etree.SubElement(el, M + 'e'); _emit(body, e, size, color)


def omath(latex, size=24, color=None):
    om = etree.Element(M + 'oMath', nsmap={'m': NS['m']})
    _emit(Parser(latex).seq(), om, size, color)
    return om


def inline_math(latex, size=24, color=None):
    m = etree.Element(A14 + 'm', nsmap={'a14': NS['a14']})
    m.append(omath(latex, size, color))
    return m


def math_paragraph(latex, size=24, color=None, align='ctr'):
    p = etree.Element(A + 'p')
    ppr = etree.SubElement(p, A + 'pPr', algn=align, indent='0', marL='0')
    for tag in ('spcBef', 'spcAft'):
        sp = etree.SubElement(ppr, A + tag); etree.SubElement(sp, A + 'spcPts', val='600')
    etree.SubElement(ppr, A + 'buNone')
    m = etree.SubElement(p, A14 + 'm', nsmap={'a14': NS['a14']})
    para = etree.SubElement(m, M + 'oMathPara', nsmap={'m': NS['m']})
    pp = etree.SubElement(para, M + 'oMathParaPr'); etree.SubElement(pp, M + 'jc', {M + 'val': 'centerGroup' if align == 'ctr' else 'left'})
    para.append(omath(latex, size, color))
    etree.SubElement(p, A + 'endParaRPr', lang='en-US', sz=str(int(size * 100)))
    return p


def wrap_math_shapes(slide):
    """PowerPoint expects a shape that contains a14:m inside mc:AlternateContent/mc:Choice Requires="a14"."""
    tree = slide.shapes._spTree
    for sp in list(tree):
        if sp.tag in (f'{{{NS["p"]}}}sp', f'{{{NS["p"]}}}graphicFrame') and next(sp.iter(A14 + 'm'), None) is not None:
            ac = etree.Element(MC + 'AlternateContent', nsmap={'mc': NS['mc'], 'a14': NS['a14']})
            ch = etree.SubElement(ac, MC + 'Choice', Requires='a14')
            sp.addprevious(ac)
            fb = etree.SubElement(ac, MC + 'Fallback')       # as PowerPoint writes: plain copy without equations
            plain = copy.deepcopy(sp)
            for m in list(plain.iter(A14 + 'm')):
                m.getparent().remove(m)
            ch.append(sp)
            fb.append(plain)


if __name__ == '__main__':
    import sys
    print(etree.tostring(omath(sys.argv[1]), pretty_print=True).decode())
