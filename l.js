let s = require('./aoc').sreadlines('i.12').map(s => s.match(/[-\d]+/g).map(Number));
let v = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
let T = Array(3).fill(null);
const init = new Set()
for (let i = 0; i < 3; i++)
  init.add(i+String(s.map(l => l[i])));
init.add('v'+String([0,0,0,0]))
for (let i = 0; T.includes(null); i++) {
	if (i === 1000) {
		const f = l => l.map(Math.abs).reduce((_,$) => $+_), ke = v.map(f), pe = s.map(f);
		let total = 0;
		for (let j = 0; j < 4; j++) {
			total += ke[j]*pe[j];
		}
		console.log(total);
	}
	for (let me = 0; me < 4; me++) {
		for (let oth = 0; oth < 4; oth++) {
			if (oth === me) continue;
			for (let ax = 0; ax < 3; ax++) {
				if (s[me][ax] < s[oth][ax]) v[me][ax] += 1;
				else if (s[me][ax] > s[oth][ax]) v[me][ax] -= 1;
			}
		}
	}
	for (let me = 0; me < 4; me++) {
		for (let ax = 0; ax < 3; ax++) s[me][ax] += v[me][ax];
	}
	for (let ax = 0; ax < 3; ax++) {
		if (T[ax] === null){
      if (init.has('v'+String(v.map(l => l[ax]))) && init.has(ax+String(s.map(l => l[ax])))) T[ax] = i+1;
    }
	}
}
const gcd = (a,b) => b ? gcd(b, a%b) : a;
console.log(T.reduce((a,b) => a*b/gcd(a,b)))
