"""Regression checks for instructor edits, ordering, notes and overwrite protection."""
import io
from pathlib import Path
import tempfile
import unittest
from contextlib import redirect_stdout, redirect_stderr
from unittest.mock import patch
from zipfile import ZipFile

import pptx_to_markdown as exporter
from pptx_to_markdown import extract_slides, render
from deck_paths import candidate_output, validate_candidate_output

P = 'http://schemas.openxmlformats.org/presentationml/2006/main'
A = 'http://schemas.openxmlformats.org/drawingml/2006/main'
R = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'


def fixture(edited='Instructor edit', image=False):
    def shape(text, ph='body'):
        return f'<p:sp><p:nvSpPr><p:nvPr><p:ph type="{ph}"/></p:nvPr></p:nvSpPr><p:txBody><a:p><a:r><a:t>{text}</a:t></a:r></a:p></p:txBody></p:sp>'
    def slide(body, hidden=False):
        return f'<p:sld xmlns:p="{P}" xmlns:a="{A}" xmlns:r="{R}" show="{0 if hidden else 1}"><p:cSld><p:spTree>{body}</p:spTree></p:cSld></p:sld>'
    rel = lambda kind, target, id: f'<Relationship Id="{id}" Type="{R}/{kind}" Target="{target}"/>'
    def rels(*items):
        return '<Relationships>' + ''.join(items) + '</Relationships>'
    table = '<p:graphicFrame><a:graphic><a:graphicData><a:tbl>' + ''.join(
        '<a:tr>' + ''.join(f'<a:tc><a:txBody><a:p><a:r><a:t>{v}</a:t></a:r></a:p></a:txBody></a:tc>' for v in row) + '</a:tr>'
        for row in [('Milestone', 'Weight'), ('Project', '35%')]) + '</a:tbl></a:graphicData></a:graphic></p:graphicFrame>'
    link = '<p:sp><p:txBody><a:p><a:r><a:rPr><a:hlinkClick r:id="web"/></a:rPr><a:t>Course site</a:t></a:r></a:p></p:txBody></p:sp>'
    notes = f'<p:notes xmlns:p="{P}" xmlns:a="{A}"><p:cSld><p:spTree>' + shape('Private speaker reminder') + shape('999', 'sldNum') + '</p:spTree></p:cSld></p:notes>'
    data = io.BytesIO()
    with ZipFile(data, 'w') as z:
        z.writestr('ppt/presentation.xml', f'<p:presentation xmlns:p="{P}" xmlns:r="{R}"><p:sldIdLst><p:sldId r:id="second"/><p:sldId r:id="first"/></p:sldIdLst></p:presentation>')
        z.writestr('ppt/_rels/presentation.xml.rels', rels(rel('slide', 'slides/slide1.xml', 'first'), rel('slide', 'slides/slide9.xml', 'second')))
        z.writestr('ppt/slides/slide1.xml', slide(shape('Original first', 'title')))
        picture = '<p:pic><p:nvPicPr><p:cNvPr name="QR code"/></p:nvPicPr><p:blipFill><a:blip r:embed="image"/></p:blipFill></p:pic>' if image else ''
        z.writestr('ppt/slides/slide9.xml', slide(shape('Moved slide', 'title') + f'<p:grpSp>{shape(edited)}</p:grpSp>' + table + link + picture, True))
        z.writestr('ppt/slides/_rels/slide9.xml.rels', rels(rel('notesSlide', '../notesSlides/notesSlide2.xml', 'notes'), rel('image', '../media/image1.png', 'image'), f'<Relationship Id="web" Type="{R}/hyperlink" Target="https://example.com/course" TargetMode="External"/>'))
        if image:
            z.writestr('ppt/media/image1.png', b'image bytes preserved exactly')
        z.writestr('ppt/notesSlides/notesSlide2.xml', notes)
    return data.getvalue()


class ExtractTests(unittest.TestCase):
    def test_images_export_check_missing_asset_and_preserve_modified_asset(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder).resolve()
            source, output = root / 'course/deck.pptx', root / 'output/deck.md'
            source.parent.mkdir()
            source.write_bytes(fixture(image=True))
            before = source.read_bytes()
            def run(*args):
                with patch.object(exporter, 'ROOT', root), patch('sys.argv', ['pptx_to_markdown.py', str(source), *args]), redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                    exporter.main()
            run()
            self.assertIn('![QR code](<deck_assets/', output.read_text())
            asset, = (output.parent / 'deck_assets').glob('*.png')
            self.assertEqual(asset.read_bytes(), b'image bytes preserved exactly')
            run('--check')
            asset.unlink()
            with self.assertRaises(SystemExit):
                run('--check')
            run()
            asset.write_bytes(b'manually modified')
            with self.assertRaises(SystemExit):
                run()
            self.assertEqual(asset.read_bytes(), b'manually modified')
            self.assertEqual(source.read_bytes(), before)

    def test_cli_detects_stale_view_and_preserves_manual_markdown(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder).resolve()
            source, output = root / 'course/deck.pptx', root / 'output/deck.md'
            source.parent.mkdir()
            source.write_bytes(fixture())
            def run(*args):
                with patch.object(exporter, 'ROOT', root), patch('sys.argv', ['pptx_to_markdown.py', str(source), *args]), redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                    exporter.main()
            run()
            first = output.read_bytes()
            source.write_bytes(fixture('Saved after export'))
            with self.assertRaises(SystemExit) as result:
                run('--check')
            self.assertEqual(result.exception.code, 1)
            self.assertEqual(output.read_bytes(), first)
            run()
            self.assertIn('Saved after export', output.read_text())
            run('--check')
            output.write_text('Handwritten notes to preserve')
            with self.assertRaises(SystemExit):
                run()
            self.assertEqual(output.read_text(), 'Handwritten notes to preserve')

    def test_reordered_hidden_slide_and_grouped_edits(self):
        slides = extract_slides(fixture())
        self.assertEqual([s['title'] for s in slides], ['Moved slide', 'Original first'])
        self.assertTrue(slides[0]['hidden'])
        self.assertIn('Instructor edit', slides[0]['blocks'])

    def test_tables_hyperlinks_notes_and_metadata(self):
        slide = extract_slides(fixture())[0]
        self.assertIn('| Project | 35% |', '\n'.join(slide['blocks']))
        self.assertIn('[Course site](<https://example.com/course>)', '\n'.join(slide['blocks']))
        self.assertEqual(slide['notes'], ['Private speaker reminder'])

    def test_refresh_reads_saved_edits_without_changing_pptx(self):
        with tempfile.TemporaryDirectory() as folder:
            source, output = Path(folder) / 'deck.pptx', Path(folder) / 'deck.md'
            source.write_bytes(fixture())
            before = source.read_bytes()
            first, count = render(source, output)
            self.assertEqual(count, 2)
            self.assertEqual(source.read_bytes(), before)
            source.write_bytes(fixture('New saved wording'))
            edited = source.read_bytes()
            second, _ = render(source, output)
            self.assertNotEqual(first, second)
            self.assertIn('New saved wording', second)
            self.assertEqual(source.read_bytes(), edited)
            self.assertEqual(second, render(source, output)[0])


class CandidateTests(unittest.TestCase):
    def test_course_target_redirected_and_existing_candidate_preserved(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder).resolve()
            target = candidate_output(root, 'course/lectures/week01/deck.pptx')
            self.assertEqual(target, root / 'output/deck_candidates/deck.candidate.pptx')
            target.parent.mkdir(parents=True)
            target.write_bytes(b'instructor changes')
            with self.assertRaises(FileExistsError):
                candidate_output(root, 'course/lectures/week01/deck.pptx')
            self.assertEqual(target.read_bytes(), b'instructor changes')
            with self.assertRaises(ValueError):
                validate_candidate_output(root, root / 'course/deck.candidate.pptx')

    def test_symlink_to_editable_directory_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder).resolve()
            (root / 'course').mkdir()
            (root / 'output').mkdir()
            (root / 'output/deck_candidates').symlink_to(root / 'course', target_is_directory=True)
            with self.assertRaises(ValueError):
                candidate_output(root, 'deck.pptx')


if __name__ == '__main__':
    unittest.main()
