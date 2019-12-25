import aoc, e
from collections import defaultdict as dd, deque as dq
s = aoc.sread('i.15', int, ',')
grid = dd(lambda: -1)
WALKABLE = (1,2)
def checkMove(adj_c, grid, *_): return grid[adj_c] in WALKABLE
def plotCheckMove(adj_c, grid, move, internal_border=dq([e.runtime(s).throw(RuntimeError)]), prev=[(0,0)]): #note that the dq() is only spawned on the first function call
    back = aoc.back_adj(adj_c, move)
    if prev[0] != back:
        prev[0] = back
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

dmap = aoc.distance_map((0,0), grid, plotCheckMove) #build & measure map distance via BFS
opos = [k for k in grid if grid[k] == 2][0] #position of oxygen
print dmap[opos]    #part 1: distance of opos to centre
print max(aoc.distance_map(opos, grid, checkMove).values()) #part 2: measure furthest point from opos
