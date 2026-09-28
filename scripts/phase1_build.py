#!/usr/bin/env python3
"""Build reviewed Phase 1 manifests from captured catalogs and local-file metadata.

Source-specific descriptions below are factual extraction notes, not topic mappings.
Re-running overwrites manifests; review the diff after refreshing source snapshots.
"""
import hashlib
import json
import re
import tempfile
from pathlib import Path
from urllib.parse import urldefrag
import yaml

ROOT = Path(__file__).resolve().parents[1]
CACHE = Path(tempfile.gettempdir()) / 'rl-phase1-cache'
CONFIG = yaml.safe_load((ROOT / 'config/sources.yaml').read_text())


def clean(text):
    return ' '.join(text.split())


def mid(key):
    return 'm_' + hashlib.sha256(key.encode()).hexdigest()[:12]


class Inventory:
    def __init__(self, source, offering, basis):
        self.sid = source['id']
        self.base = ROOT / 'sources' / self.sid
        self.data = dict(schema_version=1, phase=1, source_id=self.sid,
            configured_source=source, offering=dict(label=offering, evidence=basis),
            inventory_status='inventoried_with_documented_gaps',
            scope='Material inventory only; no normalized topics, cross-course comparison, or curriculum recommendations.',
            materials=[], observations=[], evidence_gaps=[])
        self.by_key = {}

    def index(self, slug):
        path = self.base / 'snapshots' / (slug + '_index.json')
        return json.loads(path.read_text()), str(path.relative_to(ROOT))

    def add(self, title, kind, use, locator, evidence, observed, **extra):
        key = locator.get('url') or locator.get('path') or title + str(evidence)
        if key in self.by_key:
            item = self.by_key[key]
            for e in evidence:
                if e not in item['provenance']:item['provenance'].append(e)
            return item
        item = dict(id=mid(key), title=clean(title), material_type=kind,
            instructional_use=use, offering=self.data['offering']['label'], **locator,
            storage='linked' if 'url' in locator else 'existing_local' if 'path' in locator else 'embedded_reference',
            observed_at=observed, provenance=evidence,
            accessibility={'status':'listed_not_fetched' if 'url' in locator else 'local_readable' if 'path' in locator else 'described_in_parent'})
        item.update(extra)
        self.data['materials'].append(item);self.by_key[key]=item
        return item

    def link(self, slug, link, kind, use, title=None, **extra):
        d,p = self.index(slug)
        item=self.add(title or link['label'] or link['url'], kind,use,{'url':link['url']},
            [{'source_url':d['url'],'index_path':p,'link_index':link['index'],'heading':link['heading']}],d['checked_at'],**extra)
        if link.get('context'):item.setdefault('catalog_context',clean(link['context']))
        return item

    def pages(self, slugs):
        for slug in slugs:
            d,p=self.index(slug)
            kind,use={'project':('project_guidelines','assessment'),
                      'projects':('project_examples_index','reference'),
                      'starter_code':('starter_code','assessment')}.get(slug,('course_index','catalog'))
            self.add(d.get('title',slug),kind,use,{'url':d['url']},
                     [{'index_path':p}],d['checked_at'],accessibility={'status':'page_indexed' if d['status']=='reachable' else d['status'],'http_status':d.get('http_status')})
            if d['status']!='reachable':self.gap('page_access',f'{slug}: {d["status"]}, HTTP {d.get("http_status", "not available")}',[p])

    def note(self, text, evidence):
        self.data['observations'].append({'statement':text,'basis':'direct_source_evidence','evidence':evidence})

    def gap(self, category, text, evidence):
        self.data['evidence_gaps'].append({'category':category,'description':text,'evidence':evidence,
            'interpretation':'A limit of available evidence, not proof that material was not taught or used.'})

    def finish(self):
        # Merge independently observed HTTP metadata and PDF inspection without overstating either.
        pdfs={d['url']:(d,str(p.relative_to(ROOT))) for p in self.base.glob('snapshots/pdf_*.json') for d in [json.loads(p.read_text())]}
        checks=self.base/'snapshots/link_checks.json'
        checkmap={d['url']:d for d in json.loads(checks.read_text())} if checks.exists() else {}
        for item in self.data['materials']:
            url=item.get('url')
            if url and urldefrag(url)[0] in checkmap:
                c=checkmap[urldefrag(url)[0]]
                item['accessibility']={k:c[k] for k in ['status','http_status','resolved_url','checked_at','verification_level'] if k in c}
                item['accessibility']['evidence_path']=str(checks.relative_to(ROOT))
            if url in pdfs:
                d,p=pdfs[url]
                if d.get('sha256'):
                    item['accessibility']={'status':'pdf_text_inspected','checked_at':d['checked_at'],'evidence_path':p}
                    item['remote_sha256']=d['sha256']
                    item['remote_pdf_pages']=int(re.search(r'^Pages:\s+(\d+)',d['pdfinfo'],re.M).group(1))
                    item['provenance'].append({'inspection_path':p,'locator':'PDF title and task/project sections'})
        self.data['inspected_at']=max(m['observed_at'] for m in self.data['materials'])
        (self.base/'manifest.yaml').write_text(yaml.safe_dump(self.data,sort_keys=False,allow_unicode=True,width=110))
        print(self.sid,len(self.data['materials']),'materials')


def external(source):
    sid=source['id']
    offerings={'silver_rl':'2015 (COMPM050/COMPGI13)', 'berkeley_cs285':'Spring 2026 (CS185/285)',
               'stanford_cs234':'Winter 2026', 'stanford_cs224r':'Spring 2026'}
    inv=Inventory(source,offerings[sid],[{'source_url':source['url'],'locator':'course heading; Berkeley also assignment PDF headers'}])
    if sid=='silver_rl':
        inv.pages(['teaching']);d,_=inv.index('teaching')
        for l in d['links']:
            u=l['url'];idx=l['index']
            if 8<=idx<=17:
                inv.link('teaching',l,'lecture_slides','listed_teaching',sequence=idx-7)
            elif idx==18:inv.link('teaching',l,'assignment','assessment',title='Easy21 assignment')
            elif idx in [20,21]:inv.link('teaching',l,'exam_solutions' if idx==21 else 'exam','past_assessment',title='Previous RL exam '+l['label'],offering='Previous exam; year not stated')
            elif idx==7:inv.link('teaching',l,'recording','listed_teaching',title='Video entry point linked from teaching page',check_url=False)
        inv.note('The landing page identifies the course as Advanced Topics 2015. PDF upload paths containing 2025 are hosting paths, not evidence of a 2025 course offering.',[source['url']])
        inv.note('Easy21 is a six-section exercise brief covering environment implementation, Monte Carlo control, TD learning, linear approximation, discussion, and submission.', ['Easy21 assignment PDF, sections 1–6'])
        inv.gap('not_found','No separate project guidelines, starter-code package, or assigned-reading schedule was found on the configured teaching page or in the Easy21 brief. Slide bibliographies are not an assigned-reading list.',[source['url'],'Easy21 assignment PDF'])
        inv.gap('recordings','The teaching page exposes one YouTube video entry point. Playlist completeness and playback were not verified.',[source['url']])
    elif sid=='berkeley_cs285':
        inv.pages(['home','syllabus','resources','calendar','starter_code'])
        d,_=inv.index('home')
        for l in d['links']:
            u=l['url'];label=clean(l['label'])
            if '/static/slides/' in u:inv.link('home',l,'lecture_slides','scheduled_teaching',sequence=int(re.search(r'lec-(\d+)',u).group(1)))
            elif '/static/sections/' in u:inv.link('home',l,'discussion_slides','scheduled_teaching')
            elif '/static/homeworks/' in u:inv.link('home',l,'assignment','assessment')
            elif '/static/misc/' in u:inv.link('home',l,'project_guidelines','assessment')
            elif 'youtube' in u:inv.link('home',l,'recording_collection','supplemental_past_offering',title='Fall 2023 recordings',offering='Fall 2023',check_url=False)
        d,_=inv.index('resources')
        for l in d['links']:
            if l['heading']=='Relevant Textbooks':inv.link('resources',l,'reading','recommended_reference',check_url=False)
            elif l['label']=='Data visualization handout':inv.link('resources',l,'supplemental_notes','optional_reference')
            elif l['heading']=='Previous Offerings' and (re.search(r'20\d\d',l['label']) or 'youtube' in l['url']):
                inv.link('resources',l,'archive_index' if 'youtube' not in l['url'] else 'recording_collection','supplemental_past_offering',offering='Previous offering; see catalog context',check_url=False)
        d,_=inv.index('syllabus')
        for l in d['links']:
            if 'github.com/berkeleydeeprlcourse/' in l['url']:inv.link('syllabus',l,'starter_code','assessment',title='Spring 2026 homework repository')
        inv.note('The syllabus specifies five homeworks, a final project, a midterm, and lecture mini-quizzes. Current recordings are on bCourses; public Fall 2023 recordings are labeled separately.', ['syllabus_index.json: Materials, Course Logistics, Grading','home_index.json: recording announcement'])
        inv.note('The project outline distinguishes the CS185 default-project route from CS285 custom proposals and supplies component requirements and a rubric. Both default-project briefs and their starter-code links are indexed.', ['final_project_outline.pdf, sections 2–5','default project PDFs'])
        inv.gap('date_conflict','The project outline gives an April 6 milestone; both default-project briefs give April 13. No attempt was made to choose the governing date.', ['final_project_outline.pdf p.1','llm_rl_default_final_project.pdf p.1','offline_to_online_rl_default_final_project.pdf p.1'])
        inv.gap('restricted_material','bCourses recordings and Gradescope mini-quiz/exam contents were not accessed. Listed late-term guest-lecture slots do not all have named slide links.', ['syllabus_index.json','home_index.json'])
        inv.gap('readings_and_examples','General recommended books and the default offline-to-online project reading list are indexed. No separate current lecture-by-lecture assigned-reading schedule or current student-project report catalog was found on the inspected course pages.', ['resources_index.json','home_index.json','offline_to_online_rl_default_final_project.pdf section 8'])
    elif sid=='stanford_cs234':
        inv.pages(['home','modules','assignments','project','scpd','faq']);d,_=inv.index('modules')
        for l in d['links']:
            u=l['url']
            if '/cs234/slides/' in u:
                n=re.search(r'lecture(\d+)(pre|post)',u)
                title=(f'Lecture {n.group(1)} — '+('pre-class' if n.group(2)=='pre' else 'post-class annotated')) if n else l['label']
                inv.link('modules',l,'lecture_slides','listed_teaching',title=title,**({'sequence':int(n.group(1))} if n else {}))
            elif l['index'] in [4,5,6,31]:inv.link('modules',l,'reading','additional_material_requirement_unspecified',check_url=False)
        readings=['SB Chp 1','SB Chp 3, 4.1–4.4','SB Chp 5.1, 5.5, 6.1–6.3','SB Chp 5.2, 5.4, 6.4–6.5, 6.7','SB Chp 13']
        for value in readings:inv.add(value,'reading','additional_material_requirement_unspecified',{},[{'source_url':d['url'],'index_path':'sources/stanford_cs234/snapshots/modules_index.json','locator':'Additional Materials'}],d['checked_at'],note='Source-course reading citation only; not a Phase 2 book-topic mapping.')
        d,_=inv.index('assignments')
        for l in d['links']:
            u=l['url'];n=re.search(r'/a(\d)/',u)
            if n:
                kind='assignment' if u.endswith('.pdf') else 'submission_template' if 'template' in u else 'starter_code'
                inv.link('assignments',l,kind,'assessment',title=f'Assignment {n.group(1)} — {kind.replace("_"," ")}')
            elif 'drive.google.com' in u:inv.link('assignments',l,'starter_code','assessment',title='Assignment 3 starter code (Google Drive)',check_url=False)
        inv.note('The materials page lists pre-class and annotated post-class slide variants. Duplicate Lecture 7 links occur under two course headings; these are one file per variant, with both catalog references retained. Lecture 10 explicitly has no pre-class file.', ['modules_index.json'])
        inv.note('The project page provides proposal, milestone, poster, and final-report requirements; the homepage supplies component weights. The project-ideas heading is a placeholder without linked student reports.', ['project_index.json','home_index.json'])
        inv.gap('artifact_year_conflict','Assignment 3 is linked by the Winter 2026 course but its first page gives February 20, 2025. Its hosting offering and internal date are preserved separately; it is not relabeled as verified 2026 content.', ['assignments_index.json','hw3_questions.pdf p.1'])
        inv.gap('restricted_or_unverified','No public current recording links, tutorial sheets, or exam/quiz question files were found on the inspected pages. Assignment 3 Drive code is linked but its download and executability were not verified.', ['home_index.json','modules_index.json','assignments_index.json'])
        inv.gap('reading_status','Readings are labeled Additional Materials; mandatory versus optional status is not consistently specified. The homepage calls its schedule a draft.', ['modules_index.json','home_index.json'])
    else:
        inv.pages(['home','projects']);d,_=inv.index('home')
        for l in d['links']:
            u=l['url'];label=clean(l['label'])
            if '/slides/' in u:inv.link('home',l,'lecture_slides','scheduled_teaching')
            elif '/material/hw' in u:
                n=re.search(r'/hw(\d)/',u).group(1)
                kind='assignment' if u.endswith('.pdf') else 'starter_code' if u.endswith('.zip') else 'submission_template'
                inv.link('home',l,kind,'assessment',title=f'Homework {n} — {kind.replace("_"," ")}')
            elif '_Project_Guidelines.pdf' in u:inv.link('home',l,'project_guidelines','assessment')
            elif 'default_proj.zip' in u:inv.link('home',l,'starter_code','assessment',title='Default project starter code')
            elif 'compute_guide' in u:inv.link('home',l,'compute_guide','assessment_support')
            elif 'Tutotial' in u or 'Review_Session' in u:inv.link('home',l,'discussion_slides','scheduled_teaching')
            elif l['heading']=='Timeline' and any(h in u for h in ['arxiv.org','springer.com','neurips.cc']):inv.link('home',l,'reading','optional_reference',check_url=False)
            elif l['heading']=='Prerequisites:':inv.link('home',l,'reading','prerequisite_reference',check_url=False)
            elif 'youtube.com' in u:inv.link('home',l,'recording_collection','supplemental_past_offering',title='Spring 2025 lecture videos',offering='Spring 2025',check_url=False)
            elif 'spring_2025/projects/' in u:inv.link('home',l,'project_examples_index','supplemental_past_offering',title='Spring 2025 project reports',offering='Spring 2025',check_url=False)
        projects,p=inv.index('projects')
        inv.note(f'The Spring 2026 project gallery indexes {sum("/projects/pdfs/" in l["url"] for l in projects["links"])} report links. Their titles and URLs are retained in the gallery index; individual student reports were not downloaded or evaluated.',[p])
        inv.note('The timeline explicitly labels its reading column Notes & Optional Reading. Three homework briefs and separate code/templates are public. The custom and default project routes have guidelines, milestones, and grading criteria.', ['home_index.json','CS224R_Custom_Project_Guidelines.pdf','CS224R_Default_Project_Guidelines.pdf'])
        inv.gap('restricted_material','Current recordings are described as available through Canvas/Panopto. Public Spring 2025 recordings are a separate offering; no current exam question paper was linked.', ['home_index.json: Additional Information and Grading'])
        inv.gap('document_date_conflict','The default-project brief has a Poster Presentation (6/3) heading but its location/time paragraph says 6/4/25. The Spring 2026 homepage and custom-project brief specify June 3, 2026. Preserve the discrepancy.', ['CS224R_Default_Project_Guidelines.pdf section 4.4','CS224R_Custom_Project_Guidelines.pdf section 6','home_index.json'])
    # PDF inspections supply exact starter-code URLs, avoiding line-wrap corruption in extracted text.
    for p in sorted(inv.base.glob('snapshots/pdf_*.json')):
        d=json.loads(p.read_text())
        if not d.get('sha256'):continue
        for u in d.get('annotation_urls',[]):
            if 'github.com/berkeleydeeprlcourse/homework_spring2026' in u:
                inv.add('Starter code: '+u.rstrip('/').split('/')[-1],'starter_code','assessment',{'url':u},
                        [{'source_url':d['url'],'inspection_path':str(p.relative_to(ROOT)),'locator':'PDF hyperlink annotation'}],d['checked_at'])
        if 'offline_to_online_rl_default_final_project.pdf' in d['url']:
            for label in ['RLPD — Ball et al. (2023)','CQL — Kumar et al. (2020)','Q-chunking — Li et al. (2025)','QAM — Li and Levine (2026)','AWAC — Nair et al. (2021)','Balancing offline and online data — Lee et al. (2021)']:
                inv.add(label,'reading','optional_project_reference',{},[{'source_url':d['url'],'locator':'section 8: Reading list'}],d['checked_at'])
    return inv


def local(source):
    sid=source['id'];path=ROOT/source['path']/'snapshots/local_inventory.json';raw=json.loads(path.read_text())
    if sid=='current_course':offering='Single composite baseline; dates retained only as artifact provenance';basis=[{'path':'docs/repository_contract.md','locator':'single-baseline convention'},{'path':'sources/current_course/syllabusSpring2025.pdf','locator':'title'}]
    elif sid=='sutton':offering='Fall 2017 CMPUT 366/609';basis=[{'path':'sources/sutton/1-admin-and-intro.pdf','pages':[1,31]},{'path':'sources/sutton/25-MCTS.pdf','pages':[1]}]
    else:offering='Foundations of Deep RL in 6 Lectures; publication metadata points to 2021';basis=[{'path':'sources/foundations-deep-rl-abbeel/l1-mdps-exact-methods.pdf','pages':[1,2]},{'source_url':'https://www.youtube.com/watch?v=2o1yrkbpcUk','locator':'Pieter Abbeel channel metadata, published 2021-08-24; not original-download provenance'}]
    inv=Inventory(source,offering,basis)
    for f in raw['files']:
        p=Path(f['path']);name=p.name;kind='support_asset';use='supporting_source_file';title=p.stem
        if p.suffix=='.pdf':
            if sid!='current_course':kind='lecture_slides';use='listed_teaching'
            elif re.match(r'^\d+ -',name):kind='course_administration' if name.startswith('0 -') else 'lecture_slides';use='baseline_teaching_material'
            elif 'exams' in p.parts:kind='exam_solutions' if 'Solutions' in f.get('first_page_excerpt','') or 'Solutions' in name else 'exam';use='assessment'
            elif 'syllabus' in name.lower():kind='syllabus';use='course_administration'
            elif 'Hw1' in name:kind='assignment';use='assessment'
            else:kind='project_guidelines';use='assessment'
        elif p.suffix=='.tex':kind='exam_source';use='assessment_support'
        elif p.suffix=='.txt':kind='instructor_notes';use='planning_notes_not_taught_evidence'
        item=inv.add(title,kind,use,{'path':f['path']},[{'inventory_path':str(path.relative_to(ROOT)),'locator':'file hash and PDF metadata/title where applicable'}],f['inspected_at'],
            sha256=f['sha256'],size_bytes=f['size_bytes'],original_source_url=None,original_retrieved_at=None)
        if 'pdf_metadata' in f:
            item['page_count']=int(f['pdf_metadata']['Pages']);item['accessibility']['status']='local_pdf_text_extracted' if f['text_extraction_exit_code']==0 else 'local_text_extraction_failed'
            item['verification_level']='PDF metadata and title inspected; text extracted; no topic-level coverage coding'
        if kind=='lecture_slides':
            m=re.match(r'(?:l)?(\d+)',name)
            if m:item['sequence_label']=re.split(r'[- ]',name)[0] if sid=='current_course' else name.split('.')[0].split('-')[0]
        if sid=='current_course' and name=='ProposalSpring21.pdf':item['title']='Project proposal instructions'
        if sid=='sutton' and name=='25-MCTS.pdf':item['attribution']='Martin Müller, guest lecturer (title page)'
        if sid=='sutton' and name=='23-biopsych.pdf':item['attribution']='Acknowledges Elliot Ludvig (title page)'
    if sid=='current_course':
        inv.note('All supplied materials form one baseline. The 12 numbered decks include one administration deck and 11 content decks. The collection also contains two assignment briefs, project guidance, exams/solutions, exam source files and figures.', ['sources/current_course/','docs/repository_contract.md'])
        inv.note('The syllabus describes homework, midterms, and a project; Project.pdf gives proposal, formulation/progress, presentation, final-report, and code-submission guidance. Separate proposal, progress/plan, and final-report briefs are available.', ['syllabusSpring2025.pdf pp.2–3','Project.pdf pp.8–12','ProposalSpring21.pdf','ProgressAndPlanSpring2021.pdf','FinalSpring25.pdf'])
        inv.note('Assignment 1A describes supplied gridworld code; Assignment 1B points to Berkeley CS188 Spring 2024 project 6. Code was not supplied locally.', ['Comp438Spring2025Hw1a.pdf pp.1–2','Comp438Spring2025Hw1b.pdf p.1'])
        inv.add('Berkeley CS188 Spring 2024 Project 6 (referenced by baseline HW1B)','assignment_dependency','assessment',{'url':'https://inst.eecs.berkeley.edu/~cs188/sp24/projects/proj6/'},[{'path':'sources/current_course/Comp438Spring2025Hw1b.pdf','pages':[1]},{'index_path':'sources/current_course/snapshots/hw1b_dependency_index.json'}],raw['inspected_at'],note='External dependency only; not added to the configured course comparison set.')
        dependency,_=inv.index('hw1b_dependency')
        for l in dependency.get('links',[]):
            if l['url'].endswith('.zip'):inv.link('hw1b_dependency',l,'starter_code','assessment',title='HW1B external dependency code: '+l['url'].split('/')[-1])
        for title,use in [('Sutton and Barto, Reinforcement Learning: An Introduction, 2nd edition','required_reading'),('Szepesvari, Algorithms for Reinforcement Learning','recommended_reference'),('Goodfellow, Bengio and Courville, Deep Learning','recommended_reference')]:
            inv.add(title,'reading',use,{},[{'path':'sources/current_course/syllabusSpring2025.pdf','pages':[2]}],raw['inspected_at'])
        inv.gap('available_materials','Only Assignment 1A and 1B briefs are supplied; other assignment briefs, starter code, lecture recordings, a dated taught schedule, and student project reports are not in the local collection. These are availability limits, not baseline identity defects.', ['sources/current_course/snapshots/local_inventory.json'])
        inv.gap('local_provenance','Original collection/download dates are unknown. Current inspection timestamps and file hashes are recorded instead; the local files remain in place.', ['sources/current_course/snapshots/local_inventory.json'])
    elif sid=='sutton':
        inv.note('The introductory deck names Rich Sutton and Adam White. Page 31 dates the schedule to September–October 2017; the MCTS guest deck explicitly says Fall 2017.', ['1-admin-and-intro.pdf pp.1,31','25-MCTS.pdf p.1'])
        inv.note('The administration deck contains an early-term class/reading schedule (p.31), Moodle/Drive resource directions (p.32), textbook information (p.33), and assessment weights (p.34). Its syllabus includes assignments, reading-writing exercises, and exams even though those artifacts are not supplied.', ['1-admin-and-intro.pdf pp.31–34'])
        for title,use,page in [('Early-term reading schedule (source-authored chapter references)','assigned_reading',31),('Sutton and Barto, in-progress second edition (book366.pdf/book609.pdf)','assigned_reading',33),('Nils Nilsson, The Quest for AI (2010)','assigned_reading',33)]:
            inv.add(title,'reading',use,{},[{'path':'sources/sutton/1-admin-and-intro.pdf','pages':[page]}],raw['inspected_at'],note='Reference to the historical edition/schedule; not a mapping to the configured 2020 book.')
        inv.gap('unavailable_artifacts','No separate assignment, starter-code, exam, project, or recording files are supplied. The deck directs students to Moodle/Google Drive but gives no usable direct folder URL in extracted text. Assessment presence is known; detailed assessment contents remain unknown.', ['1-admin-and-intro.pdf pp.31–34','snapshots/local_inventory.json'])
        inv.gap('collection_scope','The supplied schedule covers only the early term. Filenames do not include decks 14–15; the schedule labels those sessions review and midterm, so this is not evidence of missing topic teaching.', ['1-admin-and-intro.pdf p.31','snapshots/local_inventory.json'])
        inv.gap('local_provenance','Original download URLs/dates for supplied slides are unknown; local hashes and inspection dates are preserved.', ['snapshots/local_inventory.json'])
    else:
        inv.note('All six lectures advertised on Lecture 1 p.2 are present. Titles identify Pieter Abbeel and the six-lecture series. PDF creation metadata alone is not treated as proof of a course offering date.', ['l1-mdps-exact-methods.pdf pp.1–2','snapshots/local_inventory.json'])
        inv.add('Pieter Abbeel: L6 Model-based RL (Foundations of Deep RL Series)','recording','series_recording',{'url':'https://www.youtube.com/watch?v=2o1yrkbpcUk'},[{'source_url':'https://www.youtube.com/watch?v=2o1yrkbpcUk','locator':'Author-channel search metadata; published 2021-08-24'}],raw['inspected_at'],check_url=False,accessibility={'status':'metadata_found_playback_not_verified'})
        inv.gap('collection_scope','No separate assignment, starter code, project, exam, or assigned-reading schedule is supplied with the six decks. Papers cited within slides are references, not established required readings.', ['snapshots/local_inventory.json'])
        inv.gap('local_provenance','Original slide download URLs/dates are unknown. The 2021 video metadata identifies the series but does not establish exact provenance of each local PDF. Full recording-series completeness was not verified.', ['snapshots/local_inventory.json','https://www.youtube.com/watch?v=2o1yrkbpcUk'])
    return inv


if __name__=='__main__':
    for source in CONFIG['sources']:
        inv=local(source) if 'path' in source else external(source)
        inv.finish()
