File repository structure:

Authoritative human/project intent
----------------------------------
config/course.yaml
config/sources.yaml
config/taxonomy.yaml
config/provisional_plan.yaml
decisions/course_principles.md

Authoritative accepted curriculum decisions
-------------------------------------------
decisions/topic_decisions.yaml
decisions/video_decisions.md
decisions/reading_decisions.md
decisions/assignment_decisions.md
decisions/project_decisions.md
decisions/syllabus_decisions.yaml
decisions/decision_log.md

Evidence
--------
sources/<source_id>
├── manifest.yaml
├── README.md
├── lectures/
├── assignments/
├── projects/
├── readings/
└── snapshots/
sources/RLbook2020.pdf

Course entries under `sources` in `config/sources.yaml` use the source-directory
structure above. Book entries under `books` refer directly to their configured
files and do not require a manifest or a separate source directory.

The book supports mapping course topics to relevant chapters, sections, and
pages, answering book-grounded questions, and examining possible curriculum
gaps when requested. Store course-to-book topic mappings with the normalized
evidence in `analysis/normalized_topics.yaml` during Phase 2, using the configured
book ID and precise references. Keep book coverage distinct from evidence that
a course taught or assigned that material. Book-grounded answers should cite the
relevant passages; curriculum recommendations remain analysis until accepted.

Treat all material under `sources/current_course/` as one baseline course for
inventory and comparison. Mixed years, course codes, and filename/title
discrepancies do not require splitting it into separate offerings or correcting
the original files. Use the content to identify each artifact's purpose and
retain its file reference as provenance.

Analysis / recommendations
--------------------------
analysis/

Editable teaching artifacts
----------------------------
course/

Generated views / reports
-------------------------
output/


Notes:
* We will have derived relationships. Generated/derived files should not be edited to change authoritative state. Some examples:
	* decisions/topic_decisions.yaml -> output/topic_details.md
	* decisions/topic_decisions.yaml -> output/lecture_plan.md
	* decisions/reading_decisions.md -> output/readings.md
* Phase definitions and file/folder modification permissions are defined in docs/workflow.md
* `decisions/syllabus_decisions.yaml` records the accepted syllabus identity and freeze scope. The frozen DOCX in `course/syllabus/` supplies student-facing wording; `output/syllabus.md` is its generated text view. Other decision files retain internal planning detail omitted from the concise syllabus. Exporters must not restore that detail to the student document or silently change frozen artifact fingerprints.
