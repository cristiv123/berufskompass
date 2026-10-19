import { DATA } from './data.js?v=3';
import { UI, LANGS } from './i18n.js?v=3';
import { MODULES, PAGES, ITEMS, ANCHOR_ITEMS, itemText, pageComplete } from './model.js?v=3';
import { renderReport } from './report.js?v=3';
import { demoState } from './demo.js?v=3';
import { esc } from './charts.js?v=3';

const KEY = 'berufskompass.v1';
const MAX_PAGE_MS = 10 * 60 * 1000;
const main = document.getElementById('main');
const progressEl = document.getElementById('progress');
const fileInput = document.getElementById('importFile');

const MAX_NAME = 80;
const fresh = (name = '') => ({ name, answers: {}, picks: [], open: {}, times: {}, page: 0, done: false });

function load() {
  try {
    const s = JSON.parse(localStorage.getItem(KEY));
    return s && typeof s === 'object' && s.answers ? s : null;
  } catch { return null; }
}
function save() {
  try { localStorage.setItem(KEY, JSON.stringify({ ...state, lang })); } catch { /* storage unavailable: progress lives only in this tab */ }
}

let state = load() || fresh();
const browserLang = (navigator.language || '').slice(0, 2).toLowerCase();
let lang = LANGS.includes(state.lang) ? state.lang : LANGS.includes(browserLang) ? browserLang : 'ro';
let view = 'intro';
let demo = null;
let pageEnter = 0;
let confirmRestart = false;
let toast = '';

const L = () => UI[lang];
const D = () => DATA[lang];
const hasProgress = () => Object.keys(state.answers).length > 0;
const moduleCount = MODULES.length;

function setLang(l) {
  leavePage();
  lang = l;
  save();
  render();
}

function leavePage() {
  if (view !== 'test' || !pageEnter) return;
  const p = state.page;
  if (PAGES[p] && PAGES[p].kind === 'items') {
    state.times[p] = (state.times[p] || 0) + Math.min(Date.now() - pageEnter, MAX_PAGE_MS);
  }
  pageEnter = 0;
}

function go(v) {
  leavePage();
  view = v;
  confirmRestart = false;
  render();
  window.scrollTo(0, 0);
}

// ---------------------------------------------------------------- views

function introView() {
  const I = L().intro;
  const counts = { int: 49, conf: 24, anc: 24, b5: 21, sdt: 9, ctx: 10, ad: 12, open: 5 };
  const mods = MODULES.map(m => {
    const M = L().modules[m.id];
    return `<li><div class="mod-num">${MODULES.indexOf(m) + 1}</div><div><h3>${esc(M.title)}</h3><p>${esc(M.what)} · ${esc(I.items(counts[m.id]))}</p><p class="muted small">${esc(M.basis)}</p></div></li>`;
  }).join('');
  const primary = state.done
    ? `<button class="btn" data-action="report">${esc(I.report)}</button>`
    : hasProgress()
      ? `<button class="btn" data-action="resume">${esc(I.resume)}</button>`
      : `<button class="btn" data-action="start">${esc(I.start)}</button>`;
  const restart = hasProgress()
    ? confirmRestart
      ? `<span class="confirm"><span>${esc(I.restartConfirm)}</span><button class="btn danger" data-action="restart-yes">${esc(I.restartYes)}</button><button class="btn ghost" data-action="restart-no">${esc(I.cancel)}</button></span>`
      : `<button class="btn ghost" data-action="restart">${esc(I.restart)}</button>`
    : '';
  return `<section class="intro">
    <p class="eyebrow">${esc(I.eyebrow)}</p>
    <h1>${esc(L().appName)}</h1>
    <p class="lead">${esc(I.lead)}</p>
    <div class="name-field"><label for="personName">${esc(I.nameLabel)}</label>
      <input type="text" id="personName" name="personName" maxlength="${MAX_NAME}" autocomplete="name" value="${esc(state.name || '')}">
      <p class="muted small">${esc(I.nameHint)}</p></div>
    <div class="actions">${primary}<button class="btn ghost" data-action="demo">${esc(I.demo)}</button>
      <button class="btn ghost" data-action="import">${esc(I.import)}</button>${restart}</div>
    ${toast ? `<p class="toast" role="status">${esc(toast)}</p>` : ''}
    <p class="muted small">${esc(I.privacy)}</p>
    <h2>${esc(I.modulesTitle)}</h2>
    <ol class="mods">${mods}</ol>
    <p class="note-line">${esc(I.note)}</p>
  </section>`;
}

function optionLabels(scale) {
  return D().scales[scale].map(o => {
    const i = o.indexOf(':');
    return i > 0 ? [o.slice(0, i).trim(), o.slice(i + 1).trim()] : [o, ''];
  });
}

function itemHTML(it, scale) {
  const v = state.answers[it.id];
  if (scale === 'bi') {
    const [l, r] = D().ctx[it.k];
    const dots = [1, 2, 3, 4, 5].map(n => `<label class="bdot${v === n ? ' on' : ''}" title="${n}"><input type="radio" name="${it.id}" id="${it.id}-${n}" value="${n}"${v === n ? ' checked' : ''} aria-label="${n} / 5${n === 3 ? ' · ' + esc(L().test.biMid) : ''}"><span></span></label>`).join('');
    return `<fieldset class="item bi${v ? ' done' : ''}" id="f-${it.id}"><legend class="sr">${esc(l)} ↔ ${esc(r)}</legend>
      <div class="bi-row"><span class="pole l">${esc(l)}</span><div class="dots">${dots}</div><span class="pole r">${esc(r)}</span></div></fieldset>`;
  }
  const opts = optionLabels(scale);
  const long = opts.some(o => o[1]) || scale === 'true';
  const html = opts.map(([lab, sub], i) => {
    const n = i + 1;
    return `<label class="opt${v === n ? ' on' : ''}"><input type="radio" name="${it.id}" id="${it.id}-${n}" value="${n}"${v === n ? ' checked' : ''}><span class="lab">${esc(lab)}</span>${sub ? `<span class="sub">${esc(sub)}</span>` : ''}</label>`;
  }).join('');
  return `<fieldset class="item${v ? ' done' : ''}" id="f-${it.id}"><legend>${esc(itemText(it, lang, L()))}</legend><div class="opts${long ? ' long' : ''}">${html}</div></fieldset>`;
}

function moduleHead(p) {
  const m = MODULES[p.mi], M = L().modules[m.id], T = L().test;
  return `<div class="mod-head"><p class="eyebrow">${esc(T.moduleOf(p.mi + 1, moduleCount))} · ${esc(M.title)}</p>
    <h2>${esc(p.kind === 'pick' ? T.pickTitle : M.q)}</h2>
    ${p.kind === 'pick' ? `<p>${esc(T.pickInstr)}</p>` : p.first ? `<p>${esc(M.instr)}</p><p class="muted small"><b>${esc(T.basis)}:</b> ${esc(M.basis)}</p>` : ''}</div>`;
}

function navHTML(p, extra) {
  const T = L().test;
  const last = state.page === PAGES.length - 1;
  return `<div class="nav"><button class="btn ghost" data-action="back">${esc(T.back)}</button><span class="msg" id="navMsg" role="status">${extra || ''}</span>
    <button class="btn" data-action="next">${esc(last ? T.finish : T.next)}</button></div>`;
}

function testView() {
  const p = PAGES[state.page];
  const T = L().test;
  if (p.kind === 'items') {
    pageEnter = Date.now();
    const answered = p.items.filter(it => state.answers[it.id]).length;
    return `<section class="test">${moduleHead(p)}<form id="pageForm" class="items" onsubmit="return false">${p.items.map(it => itemHTML(it, p.scale)).join('')}</form>
      ${navHTML(p, `<span class="muted">${esc(T.answered(answered, p.items.length))}</span>`)}</section>`;
  }
  if (p.kind === 'pick') {
    const picks = new Set(state.picks);
    const sorted = ANCHOR_ITEMS.slice().sort((a, b) => (state.answers[b.id] || 0) - (state.answers[a.id] || 0) || ANCHOR_ITEMS.indexOf(a) - ANCHOR_ITEMS.indexOf(b));
    const list = sorted.map(it => {
      const on = picks.has(it.id);
      const dis = !on && picks.size >= 3;
      return `<label class="pick${on ? ' on' : ''}${dis ? ' dis' : ''}"><input type="checkbox" name="pick" value="${it.id}"${on ? ' checked' : ''}${dis ? ' disabled' : ''}><span class="pick-score">${state.answers[it.id] || '–'}</span><span>${esc(itemText(it, lang, L()))}</span></label>`;
    }).join('');
    return `<section class="test">${moduleHead(p)}<form id="pageForm" class="picks" onsubmit="return false">${list}</form>${navHTML(p, `<span class="muted">${esc(T.pickCount(picks.size))}</span>`)}</section>`;
  }
  const M = L().modules.open;
  const qs = MODULES.find(m => m.id === 'open').items.map(it => {
    const o = D().open[it.k];
    return `<div class="open-q"><label for="${it.id}"><b>${esc(o.name)}.</b> ${esc(o.q)}</label><textarea id="${it.id}" name="${it.id}" rows="3" maxlength="1500" placeholder="${esc(T.openPlaceholder)}">${esc(state.open[it.id] || '')}</textarea></div>`;
  }).join('');
  return `<section class="test"><div class="mod-head"><p class="eyebrow">${esc(T.moduleOf(moduleCount, moduleCount))} · ${esc(M.title)}</p><h2>${esc(M.q)}</h2><p>${esc(M.instr)}</p><p class="muted small"><b>${esc(T.basis)}:</b> ${esc(M.basis)}</p></div>
    <form id="pageForm" class="open" onsubmit="return false">${qs}</form>${navHTML(p)}</section>`;
}

function render() {
  document.documentElement.lang = lang;
  const shown = view === 'report' ? (demo || state).name : '';
  document.title = shown ? `${L().appName} – ${shown}` : L().appName;
  document.getElementById('brandName').textContent = L().appName;
  document.querySelectorAll('[data-lang]').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.lang === lang)));
  document.getElementById('langGroup').setAttribute('aria-label', L().langLabel);
  const inTest = view === 'test';
  progressEl.hidden = !inTest;
  if (inTest) {
    const pct = Math.round((state.page / PAGES.length) * 100);
    progressEl.querySelector('.fill').style.width = pct + '%';
    progressEl.querySelector('.ptext').textContent = L().test.progress(pct);
  }
  document.body.classList.toggle('wide', view === 'report');
  main.innerHTML = view === 'test' ? testView() : view === 'report' ? renderReport(demo || state, lang) : introView();
  toast = '';
}

// ---------------------------------------------------------------- actions

function firstIncompletePage(st) {
  const i = PAGES.findIndex(p => !pageComplete(p, st));
  return i === -1 ? PAGES.length : i;
}

function next() {
  const p = PAGES[state.page];
  if (!pageComplete(p, state)) {
    const T = L().test;
    const msg = document.getElementById('navMsg');
    if (p.kind === 'pick') { msg.textContent = T.pickMissing; return; }
    const missing = p.items.filter(it => !state.answers[it.id]);
    missing.forEach(it => document.getElementById('f-' + it.id).classList.add('miss'));
    msg.textContent = T.missing(missing.length);
    const first = document.getElementById('f-' + missing[0].id);
    first.scrollIntoView({ block: 'center' });
    first.querySelector('input').focus({ preventScroll: true });
    return;
  }
  leavePage();
  state.page++;
  if (state.page >= PAGES.length) { state.done = true; state.page = PAGES.length - 1; save(); demo = null; go('report'); return; }
  save();
  render();
  window.scrollTo(0, 0);
}

function back() {
  leavePage();
  if (state.page === 0) { go('intro'); return; }
  state.page--;
  save();
  render();
  window.scrollTo(0, 0);
}

function download() {
  const data = { app: 'berufskompass', version: 1, savedAt: new Date().toISOString(), lang, name: state.name || '', answers: state.answers, picks: state.picks, open: state.open, times: state.times };
  const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  const slug = (state.name || '').normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^A-Za-z0-9]+/g, '-').replace(/^-|-$/g, '').toLowerCase();
  a.download = `berufskompass-${slug ? slug + '-' : ''}${new Date().toISOString().slice(0, 10)}.json`;
  document.body.appendChild(a);
  a.click();
  a.remove();
  setTimeout(() => URL.revokeObjectURL(a.href), 1000);
}

function sanitizeImport(obj) {
  if (!obj || typeof obj !== 'object' || !obj.answers || typeof obj.answers !== 'object') return null;
  const answers = {};
  for (const [id, v] of Object.entries(obj.answers)) {
    if (ITEMS[id] && ITEMS[id].mod !== 'open' && Number.isInteger(v) && v >= 1 && v <= 5) answers[id] = v;
  }
  if (!Object.keys(answers).length) return null;
  const anchorIds = new Set(ANCHOR_ITEMS.map(i => i.id));
  const picks = Array.isArray(obj.picks) ? [...new Set(obj.picks.filter(id => anchorIds.has(id)))].slice(0, 3) : [];
  const open = {};
  for (const [id, v] of Object.entries(obj.open || {})) if (ITEMS[id] && ITEMS[id].mod === 'open' && typeof v === 'string') open[id] = v.slice(0, 1500);
  const times = {};
  for (const [k, v] of Object.entries(obj.times || {})) if (/^\d+$/.test(k) && typeof v === 'number' && v > 0) times[k] = Math.min(v, MAX_PAGE_MS * 3);
  const name = typeof obj.name === 'string' ? obj.name.trim().slice(0, MAX_NAME) : '';
  const st = { name, answers, picks, open, times, page: 0, done: false };
  const fi = firstIncompletePage(st);
  st.done = fi >= PAGES.length;
  st.page = Math.min(fi, PAGES.length - 1);
  return st;
}

fileInput.addEventListener('change', async () => {
  const file = fileInput.files[0];
  fileInput.value = '';
  if (!file) return;
  let st = null;
  try { st = sanitizeImport(JSON.parse(await file.text())); } catch { st = null; }
  if (!st) { toast = L().intro.importError; render(); return; }
  state = st;
  save();
  toast = L().intro.importOk;
  demo = null;
  if (state.done) go('report'); else render();
});

document.getElementById('langGroup').addEventListener('click', e => {
  const b = e.target.closest('[data-lang]');
  if (b && b.dataset.lang !== lang) setLang(b.dataset.lang);
});

main.addEventListener('click', e => {
  const b = e.target.closest('[data-action]');
  if (!b) return;
  switch (b.dataset.action) {
    case 'start': state = fresh(state.name); save(); go('test'); break;
    case 'resume': state.page = Math.min(firstIncompletePage(state), PAGES.length - 1); go('test'); break;
    case 'report': demo = null; go('report'); break;
    case 'demo': demo = { ...demoState(), name: L().report.demoName }; go('report'); break;
    case 'import': fileInput.click(); break;
    case 'restart': confirmRestart = true; render(); break;
    case 'restart-no': confirmRestart = false; render(); break;
    case 'restart-yes': state = fresh(); save(); confirmRestart = false; render(); break;
    case 'next': next(); break;
    case 'back': back(); break;
    case 'print': window.print(); break;
    case 'download': download(); break;
    case 'edit': state.page = 0; go('test'); break;
    case 'home': demo = null; go('intro'); break;
  }
});

main.addEventListener('change', e => {
  const el = e.target;
  if (el.type === 'radio') {
    state.answers[el.name] = Number(el.value);
    const fs = el.closest('fieldset');
    fs.classList.add('done');
    fs.classList.remove('miss');
    fs.querySelectorAll('label').forEach(l => l.classList.toggle('on', l.contains(el)));
    const p = PAGES[state.page];
    const msg = document.getElementById('navMsg');
    if (msg && p.kind === 'items') {
      msg.innerHTML = `<span class="muted">${esc(L().test.answered(p.items.filter(it => state.answers[it.id]).length, p.items.length))}</span>`;
    }
    save();
  } else if (el.type === 'checkbox' && el.name === 'pick') {
    const set = new Set(state.picks);
    if (el.checked) set.add(el.value); else set.delete(el.value);
    state.picks = [...set].slice(0, 3);
    save();
    const y = window.scrollY;
    render();
    window.scrollTo(0, y);
  }
});

main.addEventListener('input', e => {
  if (e.target.tagName === 'TEXTAREA') { state.open[e.target.name] = e.target.value; save(); }
  else if (e.target.id === 'personName') { state.name = e.target.value.slice(0, MAX_NAME); save(); }
});

document.addEventListener('visibilitychange', () => {
  if (document.hidden && view === 'test') { leavePage(); save(); }
  else if (!document.hidden && view === 'test' && PAGES[state.page].kind === 'items') pageEnter = Date.now();
});

render();
