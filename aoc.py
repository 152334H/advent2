def sread(name, t=str, div=None):
    with open(name) as f: s = f.read()
    if s[-1] == '\n': s = s[:-1]
    if div != None: s = s.split(div)
    if t == int:
        if div != None:
            s = map(int, s)
        else: s = int(s)
    return s

def sreadlines(name, t=str, div=None):
    s = sread(name).split('\n')
    if div != None:
        s = map(lambda l: l.split(div), s)
    if t == int:
        if div != None:
            s = [map(int, l) for l in s]
        else:
            s = map(int, s)
    return s

def toGrid(d, MAP):
    l = d.keys()
    xma, xmi = max(l)[0], min(l)[0]
    l = [t[1] for t in l]
    yma, ymi = max(l), min(l)
    s = ""
    for y in range(yma, ymi-1, -1):
        for x in range(xmi, xma+1):
            s+=MAP[d[(x,y)]]
        s += '\n'
    return s
