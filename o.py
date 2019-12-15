import aoc, e
from collections import defaultdict as dd
s = aoc.sread('i.15', int, ',')
def ignore(r,v): #send r.next(v) and r.next(), checking that r.send() is true and r.next() == None
    if not r.send(v) or r.next() != None: raise "PANIC"
grid = dd(lambda: -1)
def adj(x,y): return [(x,y+1), (x,y-1), (x+1,y), (x-1,y)]
def checkMove(history, move, adj_c, grid):
    r = e.runtime(s)
    for m in history: ignore(r, m+1)
    grid[adj_c] = r.send(move+1)

def distance_map(start, grid, walkable, func=lambda *c,**v:None):
    '''returns a dict containing a grid's (coord:manhatten-distance-to-start) pairings
    `grid` must be a dict with (x,y) tuples as keys, and with its corresponding traversable values within `walkable`
    `func()` is an optional argument, useful if grid[] is to be retroactively plotted by distance_map()'''
    d = dd(lambda: 0)   #start counting distance from 0
    border = [(start, [])] #an expanding border (coord, traversal-history) of the traversed portion of the grid.
    while border:   #distance increases by 1 per loop
        new_border = []
        for coord, moves in border:
            adjacent = adj(*coord)  #list of directly (taxicab) adjacent coordinates
            for direct in range(4): #loop numerically, rather than by *adj(), to provide direction info to func()
                adj_c = adjacent[direct]    #unnecessary variable for clarity
                if adj_c not in d:
                    func(moves, direct, adj_c, grid)    #modify grid if necessary
                    if grid[adj_c] in walkable:
                        new_border.append((adj_c, moves[:]+[direct]))   #update border
                        d[adj_c] = d[coord]+1   #add to distance dict
        border = new_border
    return d
dmap = distance_map((0,0), grid, (1,2), checkMove)
opos = [k for k in grid if grid[k] == 2][0]
print dmap[opos]
print max(distance_map(opos, grid, (1,2)).values())
