const aoc = require('./aoc')
s = aoc.sreadlines('i.14', String, ' => ')
requires = {}
s.forEach(([react, prod]) => {
    const [n, cpd] = prod.split(' ');
    requires[cpd] = [n, react.split(', ').map(l => l.split(' '))];
});
function knuthMod(a, n) { return a-n*Math.floor(a/n); } //js (C*) modulo is undesired for this day
function getReq(coeff, cpd='FUEL', extra=aoc.defaultdict(()=>0)) { //the default value of `extra` here will fail in Python
    const [n, react] = requires[cpd];
    coeff -= extra[cpd];
    extra[cpd] = 0;
    let stio = !!(coeff % n);
    if (stio) extra[cpd] = n-knuthMod(coeff,n);
    stio += Math.floor(coeff/n);
    return react.map(([num,sub]) => sub == 'ORE' ? num*stio : getReq(num*stio, sub, extra)).reduce((x,y) => x+y);
}
console.log(getReq(1)); //part 1 done
let i = 0;
while (getReq(1<<++i) <= 10**12);
console.log(aoc.binsearch(c => getReq(c) > 10**12, 1<<i));
