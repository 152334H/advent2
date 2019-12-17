const aoc = require('./aoc');
const s = aoc.sread("i.16", Number, '');
let cur = a = Array.from(s, v => v);
let tmp = b = Array(650);
let S = Array(651);
const offset = s.slice(0,8).map(String).reduce(aoc.sum);
for (let p = 0; p < 100; p++) {
    S[0] = 0;
    for (let i = 0; i < 650; i++) S[i+1] = cur[i] + S[i];
    for (let i = 0; i < 650; i++) {
        let sum = 0, start = i;
        let m = 1;
        for (let end = 2*i+1; end <= 650; end+=i+1, start+=i+1) {
            switch (m++) {
                case 1: sum += S[end]-S[start]; break;
                case 3: sum += S[start]-S[end]; break;
            }
            m %= 4;
        }
        switch (m) {
            case 1: sum += S[650]-S[start]; break;
            case 3: sum += S[start]-S[650]; break;
        }
        tmp[i] = Math.abs(sum%10);
    }
    const swap = tmp
        tmp = cur, cur = swap;
}
console.log(cur.slice(0,8).map(String).reduce(aoc.sum));
