const aoc = require('./aoc');
const fuels = aoc.sreadlines('i.1', Number);
const f = m => m/3-2|0;
function f2(m){
	let t = 0;
	while (m > 8) {
		m = f(m);
		t += m;
	}
	return t;
}
console.log(fuels.map(f).reduce(aoc.sum));
console.log(fuels.map(f2).reduce(aoc.sum));
