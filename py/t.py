from collections import defaultdict as dd
import aoc
s = aoc.sreadlines('i.20')
yma, xma = len(s), len(s[0])
grid = aoc.makeGrid(s, xma, yma)
ports = dd(lambda: [None, None])
#read the input
for c in grid:
    v = grid[c]
    others = aoc.adj(*c)
    if v == '.':
        for direct in range(4):
            adj_c = others[direct]
            if grid[adj_c].isupper():
                lbl = grid[adj_c]
                tmplbl = grid[aoc.adj(*adj_c)[direct]]
                if direct%2: lbl = tmplbl + lbl
                else: lbl += tmplbl
                x, y = c
                if direct < 2: #up or down
                    if y < 3 or y+5 >= yma: inner = 0
                    else: inner = 1
                else:
                    if x < 3 or x+5 >= xma: inner = 0
                    else: inner = 1
                ports[lbl][inner] = c
                break
#
nodes = {}  #dict of portal label:coord pairs
#generate nodes
for p in ports:
    nodes[p] = ports[p][0]
    if ports[p][1]: nodes[p+'1'] = ports[p][1]
dists = dd(lambda:{}) #dict of edges
#generate edges
def portal_dest(p):
    if p == 'AA' or p == 'ZZ': return
    if p[-1] == '1': return p[:-1]
    return p+'1'

for self in nodes:
    dmap = aoc.distance_map(nodes[self], grid, lambda c,g,d: g[c] == '.')
    dist = {}
    for p,c in nodes.items():
        if c in dmap and p != self: dist[p] = dmap[c]
    out = portal_dest(self) #create a sepearate edge to the portal's mirror
    if out: dist[out] = 1
    dists[self] = dist
#search for part1 exit
print aoc.dijkstra(nodes,
                   dists,
                   lambda seen, _: 'ZZ' in seen,
                   reachable=lambda self, other: other in dists[self],
                   start='AA')
#part 2
width = max(nodes[k] for k in nodes if nodes[k][0]<xma/2 and nodes[k][1]<yma/2)[1]-2
def new_dijkstra(nodes, edges):
    states = set()  #keeps track of paths traversed
    visited = set()
    q = aoc.PQ([(0, 'AA', 0)])
    while len(q): #while condition should never break
        moved, self, depth = q.next()
        if moved == -1: #when algo fully leaves current point
            visited.add((self, depth))  #never return to this point
            continue
        #heuristic #1: prioritise searches closer to depth 0
        moved -= depth*width
        #heuristic #2: ignore searches that are too low to be efficient
        if depth > len(nodes): continue
        #verify that current path is new
        if (self, depth) in visited: continue
        #break if search is finished
        if self == 'ZZ' and not depth: break
        #otherwise, branch out
        for k in nodes:
            if k not in edges[self]: continue
            ndepth = depth
            if edges[self][k] == 1: #if moving through portal
                if k[-1] == '1': ndepth -= 1
                else: ndepth += 1
                if ndepth < 0: continue
            q.push((edges[self][k]+moved + ndepth*width, k, ndepth))
        q.push((-1,self,depth))
    return moved
print new_dijkstra(nodes, dists)
