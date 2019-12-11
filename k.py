import aoc, e
s = aoc.sread('i.11', int, ',')
def toGrid(d):
    l = d.keys()
    xma, xmi = max(l)[0], min(l)[0]
    l = [t[1] for t in l]
    yma, ymi = max(l), min(l)
    s = ""
    for y in range(yma, ymi-1, -1):
        for x in range(xmi, xma+1):
            if d.get((x,y), 0): s += '#'
            else: s += '.'
        s += '\n'
    return s
def do(grid, f):
    r = e.runtime(s)
    pos = [0,0]
    direct = 0
    while 1:
        try:
            po = tuple(pos) #lists cannot be hashed
            v = grid.get(po, 0)
            grid[po] = r.send(v)
            turn = r.next()
            r.next()
            #speedcode for turning & moving
            if turn: direct += 1
            else: direct -= 1
            if direct < 0: direct += 4
            if direct > 4: direct -= 4
            if direct == 1:
                pos[0] += 1
            elif direct == 2:
                pos[1] -= 1
            elif direct == 3:
                pos[0] -= 1
            else:
                pos[1] += 1
        except Exception:
            print f(grid)
            return
do({}, len)
do({(0,0):1}, toGrid)
