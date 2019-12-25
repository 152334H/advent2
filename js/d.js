const aoc = require('./aoc');
s = aoc.sread('i.4', Number, '-');
function prange(mi, ma, e) {
    ma++;
    return e ?
        [].concat(...Array.from(aoc.range(mi, ma), i => prange(i, 9, e-1).map(x => x+(i*10**e)))) :
        aoc.range(mi, ma);
}
function fprange(s) {
    const e = 5;
    const [first, last] = s.map(v => v/10**e|0);
    return [].
        concat(prange(first, first, e).filter(v => v > s[0])).
        concat(prange(first+1, last-1, e)).
        concat(prange(last, last, e).filter(v => v < s[1]));
}
let ans1 = ans2 = 0;
fprange(s).forEach(v => {
    const set = new Set();
    let n = 1, prev = null;
    [...String(v)].forEach(c => {
        if (prev === c) n++;
        else {
            set.add(n);
            prev = c;
            n = 1;
        }
    });
    if (set.add(n).size > 1) {
        ans1++;
        ans2 += +!set.has(2);
    }
});
console.log(ans1);
console.log(ans1-ans2);
