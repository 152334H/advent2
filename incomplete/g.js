const aoc = require("./aoc");
const e = require("./e");
const s = aoc.sread("i.7", Number, ',');
//part 2 not functional
[aoc.range(5), aoc.range(5, 10)].forEach(r => {
    const fin = [];
    for (let t of aoc.permute(r)) {
        const gens = Array.from(aoc.range(5), i => e.phaseInit(s, t[i])[0]);
        const ls = [];
        let cont = true;
        while (cont) {
            let send = 0;
            for (let i of aoc.range(5)) {
                send = gens[i].next(send).value;
                if (gens[i].next().done)
                    cont = false;
            }
            //if (send !== undefined)
            ls.push(send);
        }
        fin.push(ls.reduce(aoc.max));
    }
    console.log(fin.reduce(aoc.max));
});
