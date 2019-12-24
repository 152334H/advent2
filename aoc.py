from collections import defaultdict as dd
def sread(name, t=str, div=None):
    '''read file NAME, split it with DIV and convert it to type T'''
    with open(name) as f: s = f.read()
    if s[-1] == '\n': s = s[:-1]
    if div != None: s = s.split(div)
    if t == int:
        if div != None:
            s = map(int, s)
        else: s = int(s)
    return s

def sreadlines(name, t=str, div=None):
    '''sread, but split across newlines first'''
    s = sread(name).split('\n')
    if div != None:
        s = map(lambda l: l.split(div), s)
    if t == int:
        if div != None:
            s = [map(int, l) for l in s]
        else:
            s = map(int, s)
    return s

def makeGrid(s, xma, yma):
    '''creates a grid of (x,y):val pairs from a sreadlines() string-list'''
    grid = {}
    for y in range(yma):
        for x in range(xma):
            grid[(x,y)] = s[y][x]
    return grid
def toGrid(d, MAP=type('',(object,),{'__getitem__':lambda _,v:v})()):
    '''converts a dictionary grid D to a printable representation using the value-to-char mapping MAP
    if MAP is not given, it is assumed that each value of D is a single char'''
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

def binsearch(f, ma): #thus far, only tested on `ma=2**i`
    '''binary search across an arbitrary function F(x), with a maximal value of MA (and a minimal value of 0)'''
    c = ma
    sign = True
    i = len(bin(ma))-2
    while i:
        i -= 1  #decrease the exponent
        c += [1,-1][sign]*(1<<i)    #increase/reduce c
        sign = f(c) #true/false -> should decrease/increase
    if sign: c-=1 #if binary search ended off-by-one
    return c

def adj(x,y):
    '''returns an array of the 4 (x,y) coordinates adjacent to the input coordinate'''
    return [(x,y+1), (x,y-1), (x+1,y), (x-1,y)]

def diag(x,y):
    '''clockwise'''
    return [(x+1,y-1), (x+1,y+1), (x-1,y+1), (x-1,y-1)]

def valid(p, xmi, xma, ymi, yma):
    return p[0] >= xmi and p[0] < xma and p[1] >= ymi and p[1] < yma

def back_adj(adj_c, i):
    '''given a coordinate from adj(), get back the original (x,y)'''
    return adj(*adj_c)[{0:1, 1:0, 2:3, 3:2}[i]]

def distance_map(start, grid, func, optional=lambda:0):
    '''returns a dict containing a grid's (coord:manhatten-distance-to-start) pairings
    `grid` must be a dict with (x,y) tuples as keys, and with its corresponding traversable values within `walkable`
    `func()` is to determine if a point is legally traversable on the grid
    `optional()` runs once for each point on the grid'''
    from collections import defaultdict as dd
    d = dd(lambda: 0)   #start counting distance from 0
    border = [start]    #an expanding border (coord, traversal-history) of the traversed portion of the grid.
    for coord in border:
        adjacent = adj(*coord)  #list of directly (taxicab) adjacent coordinates
        for direct in range(4): #loop numerically, rather than by *adj(), to provide direction info to func()
            adj_c = adjacent[direct]    #unnecessary variable for clarity
            if adj_c not in d:
                if func(adj_c, grid, direct):
                    border.append(adj_c)    #update border
                    d[adj_c] = d[coord]+1   #add to distance dict
        optional()  #do something after each iteration
    return d

import heapq
class PQ(list):
    def push(self, v):
        return heapq.heappush(self, v)
    def next(self):
        return heapq.heappop(self)

def dijkstra(nodes, edges, cond, deps=dd(lambda:dd(lambda:set())), reachable=lambda *v: True, start='@'):
    states = set()  #keeps track of paths traversed
    q = PQ(((0, start, set(start)),))
    while len(q): #while condition should never break
        moved, self, seen = q.next()
        #verify that current path is new
        check = frozenset(seen|set(['!'+self]))
        if check in states: continue
        states.add(check)
        #break if search is finished
        if cond(seen, nodes): break
        #otherwise, branch out
        for k in nodes:
            if k in seen: continue
            if not reachable(self, k): continue
            if deps[self][k].issubset(seen):
                q.push((edges[self][k]+moved, k, seen|set([k])))
    return moved
