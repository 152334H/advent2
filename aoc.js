module.exports = {
    sread : function (name, t=String, div){
	const buf = require('fs').readFileSync(name);
	let s = buf.toString().trim();
	if (div != null) s = s.split(div);
	if (t === Number){
	    if (div != null) s = s.map(Number);
	    else s = Number(s);
	}
	return s;
    },
    sreadlines: function (name, t=String, div){
	let s = module.exports.sread(name, String, '\n');
	if (div != null) s = s.map(l => l.split(div));
	if (t == Number) {
	    if (div != null) s = s.map(l => l.map(Number));
	    else s = s.map(Number);
	}
	return s;
    }
}

