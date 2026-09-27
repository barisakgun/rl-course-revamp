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