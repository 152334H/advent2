const e = require('./e')
const s = require('./aoc').sread('i.9', Number, ',')
console.log(e.runtime(s).next(1).value)
console.log(e.runtime(s).next(2).value)
