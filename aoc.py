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
