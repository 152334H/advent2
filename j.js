const aoc = require('./aoc');
const s = aoc.sreadlines("i.10");
function sub(p, t) {
  return { x: p.x-t.x, y: p.y-t.y };
}
let riods = [];
s.forEach((l,y) => riods = riods.concat(
  Array.from(l, (c,x) => c == '#' ? {x: x, y: y} : null).filter(v=>v)));
function angle(p) {
    const y = p.y, x = p.x;
    let a = Math.atan2(y,x);
    if (x < 0 && y < 0) a += 2*Math.PI;
    return a;
}
function Between(f, p, t) {
    const diff = sub(p,t);
    return f(diff);
}
let ma = 0, best;
riods.forEach(cur => {
  const angs = new Set();
  riods.forEach(comp => {
    if (comp === cur) return;
    const ang = Between(angle, comp, cur);
    if (!angs.has(ang)) angs.add(ang);
  });
  const v = angs.size;
  if (ma < v) {
    ma = v;
    best = cur;
  }
});
console.log(ma);
function sqsum(p) {
  return Object.values(p).map(v => v*v).reduce(aoc.sum);
}
const targets = new Set(riods);
targets.delete(best);
let angs = {}, i = 0;
for (let v = 0; i+v < 200;) {
  i += v;
  for (const k in angs) targets.delete(Number(k));
  for (const comp of targets) {
    const ang = Between(angle, comp, best);
    if (!angs.hasOwnProperty(ang) || Between(sqsum, angs[ang], best) > Between(sqsum, comp, best)) angs[ang] = comp;
  }
  v = angs.size;
}
let ls = Object.entries(angs);
ls.sort((a,b) => a[0] < b[0] ? -1 : 1);
const ans = ls[199-i][1];
console.log(ans.y+100*ans.x)
