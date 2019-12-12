'use strict';
const buf = require('fs').readFileSync('i.1');
const fuels = buf.toString().trim().split('\n');
const f = m => m/3-2|0;
const sum = (a,b) => a+b;
function f2(m){
	let t = 0;
	while (m > 8) {
		m = f(m);
		t += m;
	}
	return t;
}
console.log(fuels.map(f).reduce(sum));
console.log(fuels.map(f2).reduce(sum));
