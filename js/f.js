const aoc = require('./aoc');
const s = aoc.sreadlines('i.6', String, ')');
const loc = {'COM': []}, ptr = {'COM': {}};
while (s.length) {
    let i = 0;
    s.slice(0).forEach(orb => {
        if (!loc.hasOwnProperty(orb[0])) i++;
        else {
            loc[orb[1]] = loc[orb[0]].concat(orb[1]);
            ptr[orb[1]] = ptr[orb[0]][orb[1]] = {};
            s.splice(i, 1);
        }
    });
}
console.log(Object.values(loc).map(v => v.length).reduce(aoc.sum));
const san = loc['SAN'], you = loc['YOU'];
let i = 0;
while (san[i] === you[i]) i++;
console.log(san.length-i+you.length-i-2);
