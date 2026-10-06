/** Explicit lossy round-trip experiment. Reads only exported Markdown + its images.
 * No PPTX import, no original object positions, no promotion to course/.
 * Usage: set SKILL_DIR, RUNTIME_NODE_MODULES, RUNTIME_PYTHON; run with bundled node
 *   scripts/roundtrip_nuts_and_bolts_chatgpt.mjs <fresh-private-build-dir>
 * Follow the presentations skill marker/finalization workflow before running.
 */
import fs from 'node:fs/promises';
import path from 'node:path';
import {createRequire} from 'node:module';
import {fileURLToPath, pathToFileURL} from 'node:url';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const build = path.resolve(process.argv[2] || '');
if (!process.argv[2]) throw new Error('A fresh private build directory is required.');
async function realDestination(p) {
  try { return await fs.realpath(p); }
  catch(e) { if(e.code !== 'ENOENT') throw e; return path.join(await realDestination(path.dirname(p)),path.basename(p)); }
}
const realBuild = await realDestination(build);
for (const dir of ['course','sources','decisions']) {
  const protectedDir = await fs.realpath(path.join(root,dir));
  if(realBuild === protectedDir || realBuild.startsWith(protectedDir + path.sep)) throw new Error('Protected build path.');
}
const {SKILL_DIR:skill,RUNTIME_NODE_MODULES:modules,RUNTIME_PYTHON:python}=process.env;
if (![skill,modules,python].every(v=>v && path.isAbsolute(v))) throw new Error('Resolve the bundled runtime and set the three environment variables.');
const requireRuntime=createRequire(path.join(modules,'__runtime__.cjs'));
const {Presentation,PresentationFile}=await import(pathToFileURL(requireRuntime.resolve('@oai/artifact-tool')).href);
const {makeNativeBulletParagraphs,finalizePresentation}=await import(pathToFileURL(path.join(skill,'container_tools/artifact_tool_utils.mjs')).href);
const mdPath=path.join(root,'output/lectures/week01/nuts_and_bolts_chatgpt.md');
const md=await fs.readFile(mdPath,'utf8');
const sections=[...md.matchAll(/^## Slide (\d+) — (.+)\n\n\*\*On slide\*\*\n\n([\s\S]*?)\n\n\*\*Speaker notes\*\*\n\n([\s\S]*?)(?=\n## Slide |(?![\s\S]))/gm)].map(m=>({n:+m[1],title:m[2],copy:m[3],notes:m[4].trim()}));
if(sections.length!==15 || sections.some(s=>s.title.endsWith('(hidden)'))) throw new Error('Experiment expects the current 15 visible slides.');
await fs.mkdir(build);
await fs.mkdir(path.join(build,'build'));
await fs.mkdir(path.join(build,'final'));
const unescape=s=>s.replace(/\\([\\`*_\[\]<>|])/g,'$1');
function runs(s) {
  const out=[]; let last=0;
  for(const m of s.matchAll(/\[((?:\\.|[^\]])*)\]\(<([^>]*)>\)/g)) {
    if(m.index>last) out.push(unescape(s.slice(last,m.index)));
    out.push({run:unescape(m[1]),textStyle:{color:'#0563C1',underline:'sng'},link:{uri:m[2],isExternal:true}});
    last=m.index+m[0].length;
  }
  if(last<s.length)out.push(unescape(s.slice(last)));
  return out;
}
const plain=s=>runs(s).map(r=>typeof r==='string'?r:r.run).join('');
function para(s,gap) {
  const bullet=s.match(/^( *)- /);
  const text=bullet?s.slice(bullet[0].length):s;
  if(bullet)return {...makeNativeBulletParagraphs([plain(text)],{marginLeftPoints:18+bullet[1].length*9,hangingPoints:13,spaceAfterPoints:gap})[0],runs:runs(text)};
  return {runs:runs(text),bulletCharacter:'',marginLeft:0,indent:0,spaceAfter:gap*100};
}
function text(slide,name,parts,frame,size,gap=12,extra={}) {
  const shape=slide.shapes.add({geometry:'textbox',name,position:frame,fill:'none',line:{fill:'none',width:0}});
  shape.text.style={typeface:'Calibri',fontSize:size,color:'#000000',alignment:'left',verticalAlignment:'top',wrap:'square',autoFit:'none',insets:{left:0,right:0,top:0,bottom:0},...extra};
  shape.text=parts.map(s=>para(s,gap));
  return shape;
}
function table(slide,block,top) {
  const values=block.split('\n').filter(l=>!/^\|\s*---/.test(l)).map(l=>l.split(/(?<!\\)\|/).slice(1,-1).map(v=>plain(v.trim())));
  const height=values.length*49;
  const t=slide.tables.add({rows:values.length,columns:2,left:52,top,width:1176,height,columnWidths:[910,266],values});
  t.styleOptions={headerRow:true,bandedRows:false,bandedColumns:false};
  t.borders.assign({style:'solid',fill:'#000000',width:.7});
  for(let r=0;r<values.length;r++)for(let c=0;c<2;c++) {
    const cell=t.getCell(r,c);cell.fill='#FFFFFF';
    cell.text.style={typeface:'Calibri',fontSize:30,color:r?'#000000':'#C00000',bold:r===0,alignment:c?'center':'left',verticalAlignment:'middle',autoFit:'none',insets:{left:10,right:10,top:4,bottom:4}};
  }
  return height;
}
const p=Presentation.create({slideSize:{width:1280,height:720}});
for(const sec of sections) {
  const slide=p.slides.add();slide.background.fill='#FFFFFF';
  let blocks=sec.copy.split('\n\n').filter(Boolean);
  if(plain(blocks[0])!==unescape(sec.title)) throw new Error('Expected one title block.');
  blocks.shift();
  const images=blocks.filter(s=>s.startsWith('!['));blocks=blocks.filter(s=>!s.startsWith('!['));
  if(images.length>1)throw new Error('Experiment supports one image per slide.');
  const tableBlock=blocks.find(s=>s.startsWith('|'));
  text(slide,'Title',[sec.title],{left:52,top:27,width:1176,height:106},sec.n===15?49:58.67,0,{typeface:'Calibri Light',color:'#C00000'});
  if(images.length) {
    const m=images[0].match(/^!\[(.+)\]\(<(.+)>\)$/);
    if(!m)throw new Error('Unsupported image Markdown.');
    const imgPath=await fs.realpath(path.resolve(path.dirname(mdPath),decodeURIComponent(m[2])));
    if(!imgPath.startsWith(path.dirname(mdPath)+path.sep))throw new Error('Unexpected image path.');
    const contentType=imgPath.endsWith('.png')?'image/png':'image/jpeg';
    slide.images.add({blob:new Uint8Array(await fs.readFile(imgPath)),contentType,alt:unescape(m[1]),fit:'contain',position:{left:825,top:170,width:400,height:450}});
  }
  if(tableBlock) {
    const at=blocks.indexOf(tableBlock); const before=blocks.slice(0,at),after=blocks.slice(at+1);
    // Simple sequential layout from Markdown order, not the original visual order.
    const beforeHeight=sec.n===10?218:90;
    text(slide,'Before table',before,{left:52,top:149,width:1176,height:beforeHeight},32,12);
    const top=149+beforeHeight+14;
    const height=table(slide,tableBlock,top);
    if(after.length)text(slide,'After table',after,{left:52,top:top+height+20,width:1176,height:105},32,8);
  } else {
    const size=sec.n===15?28:images.length?32:sec.n===14?34:36;
    text(slide,'Body',blocks,{left:52,top:153,width:images.length?730:1176,height:525},size,sec.n===15?3:16);
  }
  const notes=sec.notes==='*No speaker notes.*'?'':plain(sec.notes);
  slide.speakerNotes.textFrame.setText(notes);
}
const candidatePath=path.join(build,'build/candidate_chatgpt.pptx');
await(await PresentationFile.exportPptx(p)).save(candidatePath);
const finalPath=path.join(build,'final/nuts_and_bolts.roundtrip.candidate_chatgpt.pptx');
await finalizePresentation({workspaceDir:build,candidatePath,finalPath,pythonExecutable:python,
 integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),
 layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),
 explicitTotalSlideCount:15,requiredNativeTableOwnerSlides:[10,11],
 layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-bullet-geometry','--validate-heading-fit','--require-native-table-slide','10','--require-native-table-slide','11'],
 // Deliberate reconstruction defaults based on the source appearance; no PPTX input.
 fontPolicy:{basis:'design',families:['Calibri','Calibri Light']},verifyArtifactToolImport:true,
 receiptPath:path.join(build,'build/validation.json')});
console.log(finalPath);
