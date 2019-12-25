const aoc = require('./aoc');
const s = aoc.sread("i.16", Number, '');
const textlen = s.length;
let cur = a = Array.from(s, v => v);
let tmp = b = Array(textlen);
let S = Array(textlen+1);
const offset = Number(s.slice(0,7).map(String).reduce(aoc.sum));
for (let p = 0; p < 100; p++) {
    S[0] = 0;
    for (let i = 0; i < textlen; i++) S[i+1] = cur[i] + S[i];
    for (let i = 0; i < textlen; i++) {
        let sum = 0, start = i;
        let m = 1;
        for (let end = 2*i+1; end <= textlen; end+=i+1, start+=i+1) {
            switch (m++) {
                case 1: sum += S[end]-S[start]; break;
                case 3: sum += S[start]-S[end]; break;
            }
            m %= 4;
        }
        switch (m) {
            case 1: sum += S[textlen]-S[start]; break;
            case 3: sum += S[start]-S[textlen]; break;
        }
        tmp[i] = Math.abs(sum%10);
    }
    const swap = tmp;
    tmp = cur, cur = swap;
}
console.log(cur.slice(0,8).map(String).reduce(aoc.sum));
//begin part 2
const REPEAT = 10000;
const size = textlen*REPEAT-offset; //the size of the signal that matters
cur = a = Array(size+1);
tmp = b = Array(size+1);
for (let i = a[size] = b[size] = 0; i < size; i++)
    a[i] = s[(offset+i)%textlen];
for (let p = 0; p < 100; p++) {
    for (let i = size; i; i--)
        tmp[i-1] = Math.abs((cur[i-1]+tmp[i])%10);
    const swap = tmp;
    tmp = cur, cur = swap;
}
console.log(cur.slice(0,8).map(String).reduce(aoc.sum));
