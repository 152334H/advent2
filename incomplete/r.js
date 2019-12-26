const aoc = require("./aoc")
const Denque = require("denque")
let s = aoc.sreadlines("../i.18")
const YMA = s.length
const XMA = s[0].length
const kpos = {}
const grid = {}
for (let y = 0; y < YMA; y++)
    for (let x = 0; x < XMA; x++) {
        const c = x+','+y
        const k = grid[c] = s[y][x];
        if (aoc.islower(k) || k === '@')
            kpos[k] = c;
    }
function key_depdist_list(nodes, grid) {
}

