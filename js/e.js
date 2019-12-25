const SIZE = new Map([[1,3], [2,3], [99,0], [3,1], [4,1], [5,2], [6,2], [7,3], [8,3], [9,1]])
function instr(n) {
    const op = n % 100;
    n /= 100; n|=0;
    let modes = [];
    for (let i = 0; i < SIZE.get(op); i++) {
	const m = n % 10;
	n /= 10; n|=0;
	modes.push(m);
    }
    return [op, modes];
}
function* intcode(s) {
    let i = 0;
    let rb = 0;
    while (s.get(i) !== 99) { 
        const [op, md] = instr(s.get(i));
        const pargv = Array.from(Array(SIZE.get(op)),(_, j) => [s.get(i+j+1), i+j+1, s.get(i+j+1)+rb][md[j]]);
        switch (op) {
            case 1: 
                s.set(pargv[2], s.get(pargv[0]) + s.get(pargv[1]));
                break;
            case 2: 
                s.set(pargv[2], s.get(pargv[0]) * s.get(pargv[1]));
                break;
            case 3:
                s.set(pargv[0], yield);
                break;
            case 4:
                yield s.get(pargv[0]);
                break;
            case 5:
                if (s.get(pargv[0])) i = s.get(pargv[1])-md.length-1;
                break;
            case 6:
                if (!s.get(pargv[0])) i = s.get(pargv[1])-md.length-1;
                break;
            case 7: 
                s.set(pargv[2], s.get(pargv[0]) < s.get(pargv[1]));
                break;
            case 8: 
                s.set(pargv[2], s.get(pargv[0]) == s.get(pargv[1]));
                break;
            case 9: 
                rb += s.get(pargv[0])
                break;
            default:
                console.log("???");
        }
        i += md.length+1;
    }
}
function construct(s) {
    const aoc = require('./aoc'); //strangely, this require() cannot be chained together with the next line of code
    const d = new aoc.defaultMap(()=>0);
    [...s].forEach((v,i) => d.set(i,v));
    return intcode(d);
}
function runtime(s) {
    const r = construct(s);
    const v = r.next();
    //if (v) console.log(`intcode returned something (${v}) on init.`);
    return r
}
function phaseInit(s, v) {
    const r = runtime(s);
    return [r, r.next(v)];
}
module.exports.intcode = intcode;
module.exports.runtime = runtime;
if (require.main === module) {
    const s = require('./aoc').sread('i.5', Number, ',');
    let ans = 0;
    for (ans of phaseInit(s, 1)[0]);
    console.log(ans);
    console.log(phaseInit(s,5)[1].value);
}
