s = require('./aoc').sread('i.2', Number, ',');
const e = require('./e');
for (let n = 0; n < 100; n++) {
    for (let v = 0; v < 100; v++) {
	s[1] = n; s[2] = v;
	let cpy = s.slice(0);
	for (let _ of e.intcode(cpy)) continue;
	if (n === 12 && v === 2) console.log(cpy[0]);
        if (cpy[0] === 19690720) console.log(n*100+v);
    }
}
