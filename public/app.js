(() => {
'use strict';
const $=id=>document.getElementById(id);
const levels={easy:{label:'Fácil',roman:'I',note:'Los primeros pasos'},medium:{label:'Intermedia',roman:'II',note:'Pon a prueba tu lógica'},hard:{label:'Difícil',roman:'III',note:'Acepta el desafío'}};
let items=[], ordered=[], current=-1;
const el=(tag,cls,text)=>{const node=document.createElement(tag);if(cls)node.className=cls;if(text!==undefined)node.textContent=text;return node;};
function show(){
 const id=location.hash.slice(1), item=items.find(x=>x.id===id);
 $('board').hidden=Boolean(item);$('challenge').hidden=!item;$('back').hidden=!item;
 if(!item){current=-1;document.title='Code Relay · Hacktoberfest × IEEE HKN Nu Zeta';return;}
 current=ordered.findIndex(x=>x.id===id);const level=levels[item.level];
 $('challenge').className=item.level;$('challenge-meta').textContent=`CODE RELAY · ${item.id} · PYTHON`;
 $('challenge-title').textContent=item.title;$('challenge-level').textContent=level.label;
 $('statement').textContent=item.summary;$('conditions').replaceChildren(...item.conditions.map(s=>el('li','',s)));
 $('skills').textContent='Conocimientos: '+item.skills.join(' · ');
 $('example-input').textContent=item.input;$('example-output').textContent=item.output;
 $('position').textContent=`${current+1} / ${ordered.length}`;$('prev').disabled=current===0;$('next').disabled=current===ordered.length-1;
 document.title=item.title+' · Code Relay';window.scrollTo(0,0);$('challenge').focus({preventScroll:true});
}
function move(delta){if(current<0)return;const next=ordered[current+delta];if(next)location.hash=next.id;}
function home(){location.hash='';}
function notice(text){$('notice').textContent=text;$('notice').hidden=false;setTimeout(()=>$('notice').hidden=true,3500);}
async function fullscreen(){try{if(document.fullscreenElement)await document.exitFullscreen();else await document.documentElement.requestFullscreen();}catch{notice('Usa F11 en tu navegador para activar pantalla completa.');}}
document.addEventListener('fullscreenchange',()=>{$('fullscreen').setAttribute('aria-label',document.fullscreenElement?'Salir de pantalla completa':'Pantalla completa');});
$('fullscreen').addEventListener('click',fullscreen);$('back').addEventListener('click',home);$('prev').addEventListener('click',()=>move(-1));$('next').addEventListener('click',()=>move(1));
document.addEventListener('keydown',e=>{if(e.target.closest('input,summary,details'))return;if(e.key==='Escape')home();if(e.key==='ArrowRight'){e.preventDefault();move(1);}if(e.key==='ArrowLeft'){e.preventDefault();move(-1);}if(e.key.toLowerCase()==='f'&&!e.ctrlKey&&!e.metaKey&&!e.altKey){e.preventDefault();fullscreen();}});
window.addEventListener('hashchange',show);
fetch('challenges.json').then(r=>{if(!r.ok)throw Error(r.status);return r.json();}).then(data=>{
 items=data;ordered=Object.keys(levels).flatMap(level=>items.filter(x=>x.level===level));const columns=[];
 for(const [level,meta] of Object.entries(levels)){
  const group=items.filter(x=>x.level===level),section=el('section','difficulty '+level),header=el('div','difficulty-header'),copy=el('div');
  copy.append(el('h2','difficulty-title',meta.label),el('p','',`${group.length} retos · ${meta.note}`));header.append(copy,el('span','tier',meta.roman));section.append(header);
  for(const item of group){const button=el('button','challenge-link');button.setAttribute('aria-label','Proyectar '+item.title);const number=el('span','number');number.append(el('span','',item.id.slice(-2)));const copy=el('span','copy');copy.append(el('strong','',item.title),el('small','',item.short));button.append(number,copy,el('span','arrow','↗'));button.addEventListener('click',()=>{location.hash=item.id;});section.append(button);}
  if(level==='hard')section.append(el('p','hard-note','Lee las condiciones con atención. Organiza la lógica con tu equipo antes de escribir.'));
  columns.push(section);
 }
 $('challenge-columns').replaceChildren(...columns);show();
}).catch(()=>{$('challenge-columns').replaceChildren(el('p','','No se pudieron cargar los retos. Recarga la página para volver a intentarlo.'));});
})();
