const aoc = require('./aoc');
const s = aoc.sread('i.11', Number, ',')
function paint(grid, f) {
    const r = require('./e').runtime(s);
    let pos = [0,0];
    let dir = 0;
    while (1) {
        grid.set(aoc.toHashable(pos.slice(0)), r.next(grid.get(aoc.toHashable(pos))).value);
        if (r.next().value) dir += 1;
        else    dir -= 1;
        if (log = r.next().done) break;
        if (dir > 3) dir -= 4;
        else if (dir < 0) dir += 4;
        pos[Number(dir%2==0)] += [-1,1][Number(dir < 2)];
    }
    console.log(f(grid));
}
paint(new aoc.defaultMap(()=>0), d => d.size);
paint(new aoc.defaultMap(()=>0).set(aoc.toHashable([0,0]),1), g => aoc.toGrid(g, {0:'.', 1:'#'}))
