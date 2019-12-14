const aoc = require('./aoc');
const e = require('./e');
s = aoc.sread('i.2', Number, ',');
for (let n = 0; n < 100; n++) {
    for (let v = 0; v < 100; v++) {
        s[1] = n; s[2] = v;
        let cpy = new aoc.defaultMap(()=>0);
        [...s].forEach((v,i) => cpy.set(i,v));
        for (let _ of e.intcode(cpy)) continue;
        if (n === 12 && v === 2) console.log(cpy.get(0));
        if (cpy.get(0) === 19690720) console.log(n*100+v);
    }
}
