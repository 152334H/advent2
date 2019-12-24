import aoc
s = aoc.sreadlines("i.24")
grid = aoc.makeGrid(s, 5, 5)
def within(c): return aoc.valid(c,0,5,0,5)
def nextState(g):
    new = {}
    for p in g:
        new[p] = g[p]
        around = sum([g[adj] == '#' for adj in aoc.adj(*p) if within(adj)])
        if g[p] == '.' and around in [1,2]: new[p] = '#'
        elif g[p] == '#' and around != 1: new[p] = '.'
    return new
seen = set()
while 1:
    v = sum(1<<(y*5+x) for y in range(5) for x in range(5) if grid[(x,y)] == '#')
    if v in seen: break
    seen.add(v)
    grid = nextState(grid)
print v
#p2
from collections import defaultdict as dd
grids = dd(lambda:dict(((x,y),'.') for y in range(5) for x in range(5)),
           {0:aoc.makeGrid(s, 5, 5)})
def nextRecur(g, peek):
    new = dd(lambda: {})
    if peek: r = range(min(g), max(g)+1)
    else: r = range(min(g)-1, max(g)+2)
    for d in r: #the grid grows by 2 layers per Recur
        for p in g[d]:
            new[d][p] = g[d][p]
            if p == (2,2): continue
            around = 0
            for c in aoc.adj(*p):
                if c == (2,2): #hardcoding
                    if p[1] == 2: yr = range(5)
                    else: xr = range(5)
                    if p[0] == 1: xr = [0]
                    elif p[0] == 3: xr = [4]
                    elif p[1] == 1: yr = [0]
                    elif p[1] == 3: yr = [4]
                    around += sum([g[d+1][(X,Y)] == '#' for Y in yr for X in xr])
                elif aoc.valid(c,0,5,0,5): around += g[d][c] == '#'
                else: #hardcoding
                    if c[0] == -1: around += g[d-1][(1,2)] == '#'
                    if c[0] == 5: around += g[d-1][(3,2)] == '#'
                    if c[1] == -1: around += g[d-1][(2,1)] == '#'
                    if c[1] == 5: around += g[d-1][(2,3)] == '#'
            if g[d][p] == '.' and around in [1,2]: new[d][p] = '#'
            elif g[d][p] == '#' and around != 1: new[d][p] = '.'
    return dd(lambda:dict(((x,y),'.') for y in range(5) for x in range(5)), new)
for i in range(200): grids = nextRecur(grids, i%2)
print len([v for d in grids for v in grids[d].values() if v == '#'])
