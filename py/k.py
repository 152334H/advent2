import aoc, e
from collections import defaultdict as dd
s = aoc.sread('i.11', int, ',')
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
            if direct > 3: direct -= 4
            pos[direct%2==0] += [-1,1][direct<2]
        except Exception:
            print f(grid)
            return
do(dd(lambda: 0), len)
do(dd(lambda: 0, {(0,0):1}), lambda g: aoc.toGrid(g, {0:'.', 1:'#'}))
