const aoc = require('./aoc');
const e = require('./e');
s = aoc.sread('i.2', Number, ',');
for (let n = 0; n < 100; n++) {
    for (let v = 0; v < 100; v++) {
        s[1] = n; s[2] = v;
        const [r, d] = e.init(s)
        for (let _ of r) continue;
        if (n === 12 && v === 2) console.log(d[0]);
        if (d[0] === 19690720) console.log(n*100+v);
    }
}
