import { TYPES } from './model.js';
import { prediger } from './scoring.js';

const f = n => n.toFixed(1);
export const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

export function radar(int, conf, title) {
  const W = 360, H = 340, cx = 180, cy = 170, R = 112;
  const ang = i => ((-90 + i * 60) * Math.PI) / 180;
  const pt = (i, v) => [cx + (R * v / 100) * Math.cos(ang(i)), cy + (R * v / 100) * Math.sin(ang(i))];
  const poly = vals => vals.map((v, i) => pt(i, v).map(f).join(',')).join(' ');
  let s = `<svg viewBox="0 0 ${W} ${H}" class="chart" role="img" aria-label="${esc(title)}">`;
  for (const r of [25, 50, 75, 100]) s += `<polygon points="${poly(TYPES.map(() => r))}" style="fill:none;stroke:var(--line);stroke-width:1"/>`;
  TYPES.forEach((_, i) => { const [x, y] = pt(i, 100); s += `<line x1="${cx}" y1="${cy}" x2="${f(x)}" y2="${f(y)}" style="stroke:var(--line);stroke-width:1"/>`; });
  const iv = TYPES.map(t => int[t] ?? 0), cv = TYPES.map(t => conf[t] ?? 0);
  s += `<polygon points="${poly(iv)}" style="fill:var(--accent);fill-opacity:.22;stroke:var(--accent);stroke-width:2.2;stroke-linejoin:round"/>`;
  s += `<polygon points="${poly(cv)}" style="fill:none;stroke:var(--needle);stroke-width:2;stroke-dasharray:5 4;stroke-linejoin:round"/>`;
  iv.forEach((v, i) => { const [x, y] = pt(i, v); s += `<circle cx="${f(x)}" cy="${f(y)}" r="3.5" style="fill:var(--accent)"/>`; });
  TYPES.forEach((t, i) => {
    const [x, y] = pt(i, 124);
    const c = Math.cos(ang(i));
    const anchor = Math.abs(c) < 0.2 ? 'middle' : c > 0 ? 'start' : 'end';
    const dy = Math.sin(ang(i)) > 0.5 ? 12 : Math.sin(ang(i)) < -0.5 ? -8 : 4;
    s += `<text x="${f(x)}" y="${f(y + dy)}" text-anchor="${anchor}" class="axis-letter" style="fill:var(--${t})">${t}</text>`;
    s += `<text x="${f(x)}" y="${f(y + dy + 15)}" text-anchor="${anchor}" class="axis-val">${Math.round(iv[i])} · ${Math.round(cv[i])}</text>`;
  });
  return s + '</svg>';
}

export function worldMap(personVec, occs, highlight, labels) {
  const W = 500, H = 400, cx = 250, cy = 200, r = 160;
  const person = prediger(personVec);
  const pts = [person, ...occs.map(o => o.pos)];
  const scale = Math.max(1, ...pts.flatMap(p => [Math.abs(p.x), Math.abs(p.y)])) * 1.08;
  const X = x => cx + (x / scale) * r, Y = y => cy - (y / scale) * r;
  const c = cx;
  let s = `<svg viewBox="0 0 ${W} ${H}" class="chart wide-chart" role="img" aria-label="${esc(labels.title)}">`;
  s += `<circle cx="${cx}" cy="${cy}" r="${r}" style="fill:var(--soft);stroke:var(--line)"/>`;
  s += `<line x1="${cx - r}" y1="${cy}" x2="${cx + r}" y2="${cy}" style="stroke:var(--line)"/><line x1="${cx}" y1="${cy - r}" x2="${cx}" y2="${cy + r}" style="stroke:var(--line)"/>`;
  s += `<text x="${cx}" y="${cy - r - 12}" text-anchor="middle" class="axis-name">${esc(labels.data)}</text>`;
  s += `<text x="${cx}" y="${cy + r + 24}" text-anchor="middle" class="axis-name">${esc(labels.ideas)}</text>`;
  s += `<text x="${cx + r + 8}" y="${cy + 4}" text-anchor="start" class="axis-name">${esc(labels.people)}</text>`;
  s += `<text x="${cx - r - 8}" y="${cy + 4}" text-anchor="end" class="axis-name">${esc(labels.things)}</text>`;
  TYPES.forEach(t => {
    const p = prediger(TYPES.map(x => (x === t ? 100 : 0)));
    const len = Math.hypot(p.x, p.y);
    const x = cx + (p.x / len) * (r - 16), y = cy - (p.y / len) * (r - 16);
    s += `<text x="${f(x)}" y="${f(y + 5)}" text-anchor="middle" class="map-letter" style="fill:var(--${t})">${t}</text>`;
  });
  occs.forEach(o => {
    if (highlight.has(o.i)) return;
    s += `<circle cx="${f(X(o.pos.x))}" cy="${f(Y(o.pos.y))}" r="3" style="fill:var(--muted);fill-opacity:.45"><title>${esc(o.name)}</title></circle>`;
  });
  const placed = [];
  occs.filter(o => highlight.has(o.i)).forEach(o => {
    const x = X(o.pos.x); let y = Y(o.pos.y);
    s += `<circle cx="${f(x)}" cy="${f(y)}" r="4.5" style="fill:var(--accent)"><title>${esc(o.name)}</title></circle>`;
    let ly = y + 4;
    while (placed.some(p => Math.abs(p.y - ly) < 12 && Math.abs(p.x - x) < 120)) ly += 12;
    placed.push({ x, y: ly });
    const right = x < c;
    s += `<text x="${f(x + (right ? 8 : -8))}" y="${f(ly)}" text-anchor="${right ? 'start' : 'end'}" class="map-label">${esc(o.short)}</text>`;
  });
  s += `<circle cx="${f(X(person.x))}" cy="${f(Y(person.y))}" r="9" style="fill:var(--needle);stroke:var(--panel);stroke-width:2.5"/>`;
  s += `<text x="${f(X(person.x) - 13)}" y="${f(Y(person.y) - 10)}" text-anchor="end" class="map-you">${esc(labels.you)}</text>`;
  return s + '</svg>';
}

export function quadrant(int, conf, thrI, thrC, labels) {
  const W = 360, H = 360, p = 46, w = W - p - 14, h = H - p - 14;
  const X = v => p + (v / 100) * w, Y = v => 14 + h - (v / 100) * h;
  let s = `<svg viewBox="0 0 ${W} ${H}" class="chart" role="img" aria-label="${esc(labels.title)}">`;
  s += `<rect x="${p}" y="14" width="${w}" height="${h}" style="fill:var(--soft);stroke:var(--line)"/>`;
  for (const v of [0, 50, 100]) {
    s += `<text x="${f(X(v))}" y="${14 + h + 16}" text-anchor="middle" class="tick">${v}</text>`;
    s += `<text x="${p - 8}" y="${f(Y(v) + 4)}" text-anchor="end" class="tick">${v}</text>`;
  }
  s += `<line x1="${f(X(thrI))}" y1="14" x2="${f(X(thrI))}" y2="${14 + h}" style="stroke:var(--muted);stroke-dasharray:4 4"/>`;
  s += `<line x1="${p}" y1="${f(Y(thrC))}" x2="${p + w}" y2="${f(Y(thrC))}" style="stroke:var(--muted);stroke-dasharray:4 4"/>`;
  s += `<text x="${p + w - 6}" y="28" text-anchor="end" class="quad-name">${esc(labels.own)}</text>`;
  s += `<text x="${p + 6}" y="28" class="quad-name">${esc(labels.skill)}</text>`;
  s += `<text x="${p + w - 6}" y="${14 + h - 8}" text-anchor="end" class="quad-name">${esc(labels.conquer)}</text>`;
  s += `<text x="${p + 6}" y="${14 + h - 8}" class="quad-name">${esc(labels.off)}</text>`;
  s += `<text x="${p + w / 2}" y="${H - 6}" text-anchor="middle" class="axis-name">${esc(labels.x)}</text>`;
  s += `<text transform="translate(12 ${14 + h / 2}) rotate(-90)" text-anchor="middle" class="axis-name">${esc(labels.y)}</text>`;
  const placed = [];
  TYPES.forEach(t => {
    let x = X(int[t] ?? 0), y = Y(conf[t] ?? 0);
    for (let k = 0; k < 6 && placed.some(q => Math.hypot(q.x - x, q.y - y) < 26); k++) { x += 14; y -= 10; }
    placed.push({ x, y });
    s += `<circle cx="${f(x)}" cy="${f(y)}" r="13" style="fill:var(--${t})"/>`;
    s += `<text x="${f(x)}" y="${f(y + 5)}" text-anchor="middle" class="dot-letter">${t}</text>`;
  });
  return s + '</svg>';
}
