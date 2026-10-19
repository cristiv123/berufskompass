import { DATA } from './data.js';
import { UI } from './i18n.js';
import { computeResults, band } from './scoring.js';
import { TYPES, OCC, MODULES, itemText } from './model.js';
import { radar, worldMap, quadrant, esc } from './charts.js';

const fmt = (v, d = 1) => (v == null ? '–' : v.toFixed(d).replace('.', ','));

function bar(label, value, min, max, color, valText) {
  const pct = value == null ? 0 : Math.max(0, Math.min(100, ((value - min) / (max - min)) * 100));
  return `<div class="bar-row"><span class="bar-label">${label}</span><span class="track"><span class="fill" style="width:${pct.toFixed(1)}%;background:${color}"></span></span><span class="bar-val">${valText}</span></div>`;
}

function section(id, title, lead, body) {
  return `<section class="panel" id="${id}"><h2>${esc(title)}</h2>${lead ? `<p class="lead-small">${esc(lead)}</p>` : ''}${body}</section>`;
}

export function renderReport(st, lang) {
  const L = UI[lang], R = L.report, D = DATA[lang];
  const r = computeResults(st);
  const occName = i => (lang === 'ro' ? OCC[i].ro : OCC[i].de);
  const typeLabel = t => `${t} · ${D.typeName[t]}`;
  const anchorOf = code => D.anchors.find(a => a.code === code);
  const locale = lang === 'ro' ? 'ro-RO' : 'de-CH';
  const out = [];

  out.push(`<header class="report-head">
    <div><p class="eyebrow">${esc(L.appName)}</p><h1>${esc(R.title)}</h1><p class="muted">${esc(R.generated(new Date().toLocaleDateString(locale, { day: 'numeric', month: 'long', year: 'numeric' })))}</p></div>
    <div class="actions no-print">
      <button class="btn" data-action="print">${esc(R.print)}</button>
      ${st.demo ? '' : `<button class="btn ghost" data-action="download">${esc(R.download)}</button><button class="btn ghost" data-action="edit">${esc(R.editAnswers)}</button>`}
      <button class="btn ghost" data-action="home">${esc(R.backHome)}</button>
    </div></header>`);
  if (st.demo) out.push(`<p class="demo-banner">${esc(R.demoBanner)}</p>`);

  // Summary
  const mainAnchor = anchorOf(r.anchors[0].code);
  out.push(`<section class="summary">
    <div class="sum-block"><p class="label">${esc(R.codeLabel)}</p><div class="code">${r.code.map(t => `<span class="tile" style="background:var(--${t})"><b>${t}</b><small>${esc(D.typeName[t])}</small></span>`).join('')}</div></div>
    <div class="sum-block"><p class="label">${esc(R.anchorLabel)}</p><p class="big">${esc(mainAnchor.name)}</p>
      <p class="label">${esc(R.topJobs)}</p><ol class="toplist">${r.matches.slice(0, 3).map(m => `<li>${esc(occName(m.i))} <span class="num">${m.index}</span></li>`).join('')}</ol>
      <p class="label">${esc(R.qualityLabel)}</p><p><span class="chip ${r.quality.verdict}">${esc(R.verdict[r.quality.verdict])}</span></p></div>
  </section>`);

  // Interests
  const diffBand = r.differentiation >= 45 ? 'high' : r.differentiation >= 25 ? 'mid' : 'low';
  const elev = r.elevation >= 65 ? R.elev.high : r.elevation <= 30 ? R.elev.low : '';
  const rows = r.order.map(t => `<tr><td><span class="dot" style="background:var(--${t})"></span>${esc(typeLabel(t))}<div class="muted small">${esc(D.typeDesc[t])}</div></td><td class="num">${Math.round(r.int[t])}</td><td class="num">${Math.round(r.conf[t])}</td></tr>`).join('');
  out.push(section('interests', R.interests, R.interestsLead, `<div class="two">
    <figure>${radar(r.int, r.conf, R.interests)}<figcaption class="legend"><span><i class="sw" style="background:var(--accent)"></i>${esc(R.legendInt)}</span><span><i class="sw dash"></i>${esc(R.legendConf)}</span></figcaption></figure>
    <div><p>${esc(R.diff[diffBand](Math.round(r.differentiation)))}</p><p>${esc(R.cons[r.consistency] || R.cons[1])}</p>${elev ? `<p>${esc(elev)}</p>` : ''}
    <div class="tbl"><table><thead><tr><th>${esc(R.type)}</th><th class="num">${esc(R.interest)}</th><th class="num">${esc(R.confidence)}</th></tr></thead><tbody>${rows}</tbody></table></div></div></div>`));

  // World-of-work map
  const occs = r.matches.map(m => ({ i: m.i, pos: m.pos, name: occName(m.i), short: occName(m.i).length > 28 ? occName(m.i).slice(0, 26) + '…' : occName(m.i) }));
  const highlight = new Set(r.matches.slice(0, 6).map(m => m.i));
  out.push(section('map', R.map, R.mapLead, `<figure class="center">${worldMap(TYPES.map(t => r.int[t]), occs, highlight, { ...R.axes, you: R.you, title: R.map })}</figure>`));

  // Interest x confidence
  const byQ = q => TYPES.filter(t => r.quadrants[t] === q);
  const quadList = ['own', 'conquer', 'skill', 'off'].map(q => `<li><b>${esc(R.quadNames[q])}:</b> ${byQ(q).length ? byQ(q).map(t => esc(D.typeName[t])).join(', ') : esc(R.none)}. <span class="muted">${esc(R.quadAdvice[q])}</span></li>`).join('');
  out.push(section('quadrant', R.quad, R.quadLead, `<div class="two"><figure>${quadrant(r.int, r.conf, r.thrI, r.thrC, { ...R.quadNames, x: R.interest, y: R.confidence, title: R.quad })}</figure><ul class="plain">${quadList}</ul></div>`));

  // Anchors
  const anchorBars = r.anchors.map(a => bar(esc(anchorOf(a.code).name), a.score, 1, 9, 'var(--accent)', fmt(a.score))).join('');
  const anchorTop = r.anchors.slice(0, 2).map(a => `<div class="note"><h3>${esc(anchorOf(a.code).name)}</h3><p>${esc(anchorOf(a.code).desc)}</p></div>`).join('');
  out.push(section('anchors', R.anchors, R.anchorsLead, `<div class="two"><div class="bars">${anchorBars}</div><div><p class="label">${esc(R.anchorWhat)}</p>${anchorTop}</div></div>`));

  // Big Five
  const b5 = ['E', 'A', 'C', 'ES', 'O'].map(k => {
    const v = r.b5[k], b = band(v, 2.5, 3.5);
    return `<div class="trait"><div class="trait-head"><b>${esc(R.b5Names[k])}</b><span class="chip soft">${esc(R.bands[b])} · ${fmt(v)}</span></div>
      <div class="scale5"><span class="marker" style="left:${(((v - 1) / 4) * 100).toFixed(1)}%"></span></div><p class="small">${esc(R.b5Text[k][b])}</p></div>`;
  }).join('');
  out.push(section('style', R.b5, R.b5Lead, `<div class="traits">${b5}</div>`));

  // Needs
  const needBars = D.sdt.map((n, i) => bar(esc(n.name), r.needs[i], 1, 5, r.needs[i] < 3 ? 'var(--warn)' : 'var(--good)', fmt(r.needs[i]))).join('');
  const gaps = D.sdt.map((n, i) => (r.needs[i] < 3 ? `<li>${esc(R.needGap(n.name))}</li>` : '')).join('');
  out.push(section('needs', R.needs, R.needsLead, `<div class="two"><div class="bars">${needBars}</div><div>${gaps ? `<ul class="plain">${gaps}</ul>` : `<p>${esc(R.needsOk)}</p>`}</div></div>`));

  // Context
  const ctxRows = D.ctx.map(([l, rt], k) => {
    const v = r.ctx[k];
    return `<div class="bi-show"><span class="pole l${v <= 2 ? ' strong' : ''}">${esc(l)}</span><span class="bi-track"><span class="marker" style="left:${v == null ? 50 : ((v - 1) / 4) * 100}%"></span></span><span class="pole r${v >= 4 ? ' strong' : ''}">${esc(rt)}</span></div>`;
  }).join('');
  const strong = D.ctx.map(([l, rt], k) => (r.ctx[k] <= 2 ? l : r.ctx[k] >= 4 ? rt : null)).filter(Boolean);
  out.push(section('context', R.ctx, R.ctxLead, `<div class="bi-list">${ctxRows}</div><p class="label">${esc(R.ctxSummary)}</p><p>${strong.length ? strong.map(esc).join(' · ') : esc(R.ctxNone)}</p>`));

  // Adaptability
  const adBars = D.adapt.map((d, i) => bar(esc(d.name), r.adapt[i], 1, 5, 'var(--accent)', fmt(r.adapt[i]))).join('');
  const weakest = r.adapt.indexOf(Math.min(...r.adapt));
  out.push(section('adapt', R.adapt, R.adaptLead, `<div class="two"><div class="bars">${adBars}</div><div class="note"><h3>${esc(R.adaptWeakest(D.adapt[weakest].name))}</h3><p>${esc(R.adaptAction[weakest])}</p></div></div>`));

  // Jobs
  const jb = v => (v >= 80 ? 'vh' : v >= 65 ? 'h' : v >= 50 ? 'p' : 'l');
  const showDe = lang !== 'de';
  const jobRows = r.matches.slice(0, 15).map((m, k) => `<tr><td class="num">${k + 1}</td><td>${esc(occName(m.i))}</td>${showDe ? `<td class="muted">${esc(OCC[m.i].de)}</td>` : ''}
    <td class="codecell">${m.code.split('').map(t => `<span style="color:var(--${t})">${t}</span>`).join('')}</td>
    <td><span class="mini-track"><span class="fill" style="width:${m.index}%"></span></span> <span class="num">${m.index}</span> <span class="muted small">${esc(R.jobBands[jb(m.index)])}</span></td></tr>`).join('');
  const cols = R.jobCols;
  out.push(section('jobs', R.jobs, R.jobsLead, `<div class="tbl"><table class="jobs"><thead><tr><th class="num">${cols[0]}</th><th>${cols[1]}</th>${showDe ? `<th>${cols[2]}</th>` : ''}<th>${cols[3]}</th><th>${cols[4]}</th></tr></thead><tbody>${jobRows}</tbody></table></div>`));

  // Plan
  const plan = [R.planType[r.code[0]], R.planType[r.code[1]]];
  r.matches.slice(0, 2).forEach(m => plan.push(R.planInterview(occName(m.i), OCC[m.i].de)));
  TYPES.filter(t => r.quadrants[t] === 'conquer').slice(0, 2).forEach(t => plan.push(R.planConquer(D.typeName[t])));
  out.push(section('plan', R.plan, R.planLead, `<ol class="steps">${plan.map(p => `<li>${esc(p)}</li>`).join('')}</ol>`));

  // Story
  const openItems = MODULES.find(m => m.id === 'open').items;
  const stories = openItems.map(it => {
    const txt = (st.open || {})[it.id];
    if (!txt || !txt.trim()) return '';
    const o = D.open[it.k];
    return `<div class="note"><h3>${esc(o.name)}</h3><p class="quote">${esc(txt)}</p><p class="muted small">${esc(o.what)}</p></div>`;
  }).join('');
  out.push(section('story', R.story, stories ? R.storyLead : '', stories ? `<div class="notes">${stories}</div>` : `<p class="muted">${esc(R.storyEmpty)}</p>`));

  // Quality
  const q = r.quality;
  const qList = q.issues.map(i => `<li>${esc(R.qualityMsg[i.key](i.n))}</li>`).join('');
  out.push(section('quality', R.quality, '', `<p><span class="chip ${q.verdict}">${esc(R.verdict[q.verdict])}</span></p>${qList ? `<ul class="plain">${qList}</ul>` : `<p>${esc(R.qualityOk)}</p>`}`));

  out.push(section('limits', R.limits, '', `<p>${esc(R.limitsText)}</p>`));

  // Answers
  const scaleLabel = (m, v) => {
    if (v == null) return '–';
    if (m.scale === 'bi') return `${v} / 5`;
    const lab = D.scales[m.scale][v - 1];
    return `${v} · ${lab}`;
  };
  const ans = MODULES.filter(m => !m.open).map(m => {
    const list = m.items.map(it => {
      const t = itemText(it, lang, L);
      const txt = Array.isArray(t) ? `${t[0]} ↔ ${t[1]}` : t;
      return `<tr><td>${esc(txt)}</td><td class="nowrap">${esc(scaleLabel(m, st.answers[it.id]))}</td></tr>`;
    }).join('');
    return `<h3>${esc(L.modules[m.id].title)}</h3><div class="tbl"><table class="answers"><tbody>${list}</tbody></table></div>`;
  }).join('');
  out.push(`<section class="panel" id="answers"><details><summary>${esc(R.answersShow)}</summary>${ans}</details></section>`);

  return `<div class="report">${out.join('')}</div>`;
}
