module.exports = {
    sread : function(name, t=String, div) {
        const buf = require('fs').readFileSync('../input/'+name);
        let s = buf.toString().trim();
        if (div != null) s = s.split(div);
        if (t === Number) {
            if (div != null) s = s.map(Number);
            else s = Number(s);
        }
        return s;
    },
    sreadlines: function(name, t=String, div) {
        let s = module.exports.sread(name, String, '\n');
        if (div != null) s = s.map(l => l.split(div));
        if (t == Number) {
            if (div != null) s = s.map(l => l.map(Number));
            else s = s.map(Number);
        }
        return s;
    },
    toHashable: function(pos) { //ugly workaround to ensure no coordinate duplicates in grid
        return ((pos[0]+9999)<<16)|(pos[1]+9999);
    },
    toCoord: function(v) {
        return [(v>>16)-9999, (v&65535)-9999];
    },
    toGrid: function(d, MAP) {
        let xmi = ymi = 1<<24, xma = yma = -(1<<24);
        d.forEach((_,k) => {
            const c = module.exports.toCoord(k);
            if (c[0] < xmi) xmi = c[0];
            else if (c[0] > xma) xma = c[0]; //else is not strictly necessary,
            if (c[1] < ymi) ymi = c[1];
            else if (c[1] > yma) yma = c[1]; //and may break when d.len == 1
        });
        let s = "";
        for (let y = yma; y >= ymi; y--)
            for (let x = xmi; x < xma || !(s += '\n'); x++){
                s += MAP[d.get(module.exports.toHashable([x,y]))];
            }
        return s;
    },
    defaultMap: class defaultMap extends Map {
        get(k) { return super.get(k) || this.default() }
        constructor(f) {
        super();
        this.default = f;
        }
    },
    defaultdict: f => new Proxy({}, { get: (t,n) => t.hasOwnProperty(n) ? t[n] : f() }),
    binsearch: function(f, ma) {
        let c = ma, sign = true;
        for (let i = ma.toString(2).length; i--; sign = f(c))
            c += [1,-1][+sign]*(1<<i);
        if (sign) c--;
        return c;
    },
    range: function(mi, ma) {
        if (ma === undefined) ma = mi, mi = 0;
        return Array.from({length: ma-mi}, (_, i) => i + mi);
    },
    permute: function(arr) {
        //only 1 yield from permute() should be used at a time
        const tmp = arr.slice(0);
        return _permutations(tmp, 0);
    },
    max: (a,b) => a < b ? b : a,
    min: (a,b) => a > b ? b : a,
    sum: (x,y) => x+y,
    prod: (x,y) => x*y,
    islower: s => /^[a-z]*$/.test(s),
    isupper: s => /^[A-Z]*$/.test(s),
}
function* _permutations(arr, i) {
    if (arr.length === i) yield arr;
    else
        for (let j = i; j < arr.length; j++) {
            [arr[i], arr[j]] = [arr[j], arr[i]];
            yield* _permutations(arr, i+1);
            [arr[i], arr[j]] = [arr[j], arr[i]];
        }
}
