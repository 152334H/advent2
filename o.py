import aoc, e
from collections import defaultdict as dd, deque as dq
s = aoc.sread('i.15', int, ',')
grid = dd(lambda: -1)
WALKABLE = (1,2)
def checkMove(adj_c, grid, *_):
    return grid[adj_c] in WALKABLE
counter = 0
def incCount(v=1):
    global counter
    counter+=v
def plotCheckMove(adj_c, grid, move, internal_border=dq([e.runtime(s).throw(RuntimeError)])): #note that the dq() is only spawned on the first function call
    if counter:
        incCount(-1)
        internal_border.popleft()
    t = internal_border[0]
    t = dd(lambda:0, t[0].items()), t[1], t[2] #deepcopy the intcode runtime
    r = e.cont(t)
    grid[adj_c] = r.send(move+1)
    r.next()
    if checkMove(adj_c, grid):
        internal_border.append(r.throw(RuntimeError))
        return True
    return False

dmap = aoc.distance_map((0,0), grid, plotCheckMove, incCount)
opos = [k for k in grid if grid[k] == 2][0]
print dmap[opos]
print max(aoc.distance_map(opos, grid, checkMove).values())
