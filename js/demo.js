import { MODULES, PAGES, ANCHOR_ITEMS } from './model.js?v=4';

// A plausible example profile (I-C-R, technical expert) used for the clearly marked sample report.
const TARGET = {
  int: { R: 3.6, I: 4.5, A: 2.3, S: 2.3, E: 2.7, C: 3.9 },
  conf: { R: 3.8, I: 4.4, A: 2.2, S: 2.9, E: 2.8, C: 4.2 },
  anc: { TF: 4.6, GM: 2.2, AU: 4.0, SE: 3.6, EC: 2.4, SV: 2.6, CH: 3.3, LS: 4.1 },
  b5: { E: 2.4, A: 3.6, C: 4.1, N: 2.6, O: 4.0 },
  sdt: [2.0, 3.6, 3.0],
  ctx: [2, 2, 2, 1, 2, 3, 2, 2, 2, 1],
  ad: [3.4, 4.0, 2.8, 4.2],
};

export function demoState(open) {
  let seed = 7;
  const noise = () => { seed = (seed * 9301 + 49297) % 233280; return seed / 233280 - 0.5; };
  const clamp = v => Math.max(1, Math.min(5, Math.round(v)));
  const answers = {};
  for (const m of MODULES) {
    for (const it of m.items) {
      if (it.att) { answers[it.id] = it.expect; continue; }
      if (m.id === 'int') answers[it.id] = clamp(TARGET.int[it.t] + noise() * 1.4);
      else if (m.id === 'conf') answers[it.id] = clamp(TARGET.conf[it.t] + noise() * 1.2);
      else if (m.id === 'anc') answers[it.id] = clamp(TARGET.anc[it.anchor] + noise() * 1.2);
      else if (m.id === 'b5') {
        const target = TARGET.b5[it.trait] + noise();
        answers[it.id] = clamp(it.rev ? 6 - target : target);
      } else if (m.id === 'sdt') answers[it.id] = clamp(TARGET.sdt[it.need] + noise());
      else if (m.id === 'ctx') answers[it.id] = TARGET.ctx[it.k];
      else if (m.id === 'ad') answers[it.id] = clamp(TARGET.ad[it.dim] + noise());
    }
  }
  const picks = ANCHOR_ITEMS.slice()
    .sort((x, y) => answers[y.id] - answers[x.id] || (y.anchor === 'TF') - (x.anchor === 'TF'))
    .slice(0, 3).map(it => it.id);
  const times = {};
  PAGES.forEach((p, i) => { if (p.kind === 'items') times[i] = p.items.length * 6500; });
  return { answers, picks, open: open || {}, times, page: PAGES.length, done: true, demo: true };
}
