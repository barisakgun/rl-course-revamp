"""Regression checks for frozen-syllabus export and drift detection; no source edits."""
import copy
from pathlib import Path
import re
import tempfile
import unittest
from unittest.mock import patch

import syllabus_report as syllabus
from phase3_audit import read
from phase5_report import decision


class FrozenSyllabusTests(unittest.TestCase):
    def test_export_preserves_all_text_and_useful_formatting(self):
        paragraphs, tables, _ = syllabus.inspect()
        exported = syllabus.build()
        unlinked = re.sub(r'\[([^]]+)\]\(<[^>]+>\)', r'\1', exported)
        unescaped = re.sub(r'\\([\\`*_\[\]<>|])', r'\1', unlinked)
        normalize = lambda value: ' '.join(value.split())
        for text in paragraphs + [cell for table in tables for row in table for cell in row if cell]:
            self.assertIn(normalize(text), normalize(unescaped))
        self.assertIn('1. Distinguish RL', exported)
        self.assertIn('8. Connect modern RL', exported)
        self.assertIn('- Project Proposal Report (5%)', exported)
        self.assertIn('| Total |  | 100 |', exported)
        self.assertIn('[Reinforcement Learning: An Introduction](<http://incompleteideas.net/book/the-book.html>)', exported)
        self.assertIn('### COMP421/521: Machine Learning', exported)
        for old_detail in ('Week 14', 'at least 21 days', 'Two required background videos'):
            self.assertNotIn(old_detail, exported)

    def test_changed_artifacts_are_rejected_without_accepting_new_hashes(self):
        original = syllabus.freeze_record()
        with tempfile.TemporaryDirectory() as tmp:
            changed = Path(tmp)/'changed-artifact'
            changed.write_bytes(b'unapproved change')
            for kind in ('docx', 'pdf'):
                with self.subTest(kind=kind):
                    record = copy.deepcopy(original)
                    record['artifacts'][kind]['path'] = str(changed)
                    before = copy.deepcopy(record)
                    with patch.object(syllabus, 'freeze_record', return_value=record):
                        with self.assertRaisesRegex(AssertionError, 'Frozen artifact changed'):
                            syllabus.check_frozen()
                    self.assertEqual(record, before)
        syllabus.check_frozen()

    def test_published_facts_pass_and_decision_drift_fails(self):
        cfg = read('config/course.yaml')
        policy, grading, project = [decision(k) for k in ('assignment', 'grading', 'project')]
        syllabus.check_content(cfg, policy, grading, project)
        changed = copy.deepcopy(grading)
        changed['categories_percent']['project'] = 40
        with self.assertRaises(AssertionError):
            syllabus.check_content(cfg, policy, changed, project)


if __name__ == '__main__':
    unittest.main()
