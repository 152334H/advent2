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
    while (s[i] !== 99) { 
        const [op, md] = instr(s[i]);
        const pargv = Array.from(Array(SIZE.get(op)),(_, j) => [s[i+j+1], i+j+1, s[i+j+1]+rb][md[j]]);
        /*console.log(pargv, pargv.map(v=>s[v]))
        console.log(`[${i}] code: ( ${s[i+0]}, ${s[i+1]}, ${s[i+2]}, ${s[i+3]}, ) op: ${op}, modes: ${md}`);*/
        switch (op) {
            case 1: 
                s[pargv[2]] = s[pargv[0]] + s[pargv[1]];
                break;
            case 2: 
                s[pargv[2]] = s[pargv[0]] * s[pargv[1]];
                break;
            case 3:
                s[pargv[0]] = yield;
                break;
            case 4:
                yield s[pargv[0]];
                break;
            case 5:
                if (s[pargv[0]]) i = s[pargv[1]]-md.length-1;
                break;
            case 6:
                if (!s[pargv[0]]) i = s[pargv[1]]-md.length-1;
                break;
            case 7: 
                s[pargv[2]] = s[pargv[0]] < s[pargv[1]];
                break;
            case 8: 
                s[pargv[2]] = s[pargv[0]] == s[pargv[1]];
                break;
            case 9: 
                rb += s[pargv[0]];
                break;
            default:
                console.log("???");
        }
        i += md.length+1;
    }
}
function init(s) {
    const aoc = require('./aoc'); //strangely, this require() cannot be chained together with the next line of code
    const d = aoc.defaultdict(()=>0);
    [...s].forEach((v,i) => d[i] = v);
    //const d = new aoc.defaultMap(()=>0);
    //[...s].forEach((v,i) => d.set(i,v));
    return [intcode(d), d];
}
function construct(s) {
    return init(s)[0];
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
module.exports.construct = construct;
module.exports.phaseInit = phaseInit;
module.exports.init = init;
if (require.main === module) {
    const s = require('./aoc').sread('i.5', Number, ',');
    let ans = 0;
    for (ans of phaseInit(s, 1)[0]);
    console.log(ans);
    console.log(phaseInit(s,5)[1].value);
}
