from collections import deque as dq, defaultdict as dd
import aoc
s = aoc.sreadlines("i.18")
YMA = len(s)
XMA = len(s[0])
#find the location of each key, and also build a grid for later
kpos = {}
grid = {}
for y in range(YMA):
    for x in range(XMA):
        k = grid[(x,y)] = s[y][x]
        if k.islower() or k == '@': kpos[k] = (x,y)

def key_depdist_list(nodes, grid):
    '''for every key, find the doors blocking the fastest path to other keys
    `nodes` is a dict of label:coordinate pairs'''
    def can_walk(c, g, d):
        #requires outer functions refs{} and dep{}
        b = aoc.back_adj(c, d)
        refs[c] = refs[b]
        k = g[c]
        if k in '.@': pass
        elif k.isupper(): refs[c] += (k.lower(),)
        elif k.islower(): dep[k] = set(refs[c])
        else: return False
        return True
    deps = dd(lambda:{})
    dists = dd(lambda:{})
    for self in nodes:
        refs = {nodes[self]:()}
        dep = {}
        dmap = aoc.distance_map(nodes[self], grid, can_walk)
        for other in nodes:
            if other not in dep: continue
            deps[self][other] = set(dep[other])
            dists[self][other] = dmap[nodes[other]]
    return deps, dists

import heapq
class PQ(list):
    def push(self, v):
        return heapq.heappush(self, v)
    def next(self):
        return heapq.heappop(self)
def dijkstra(nodes, deps, dists):
    states = set()  #keeps track of paths traversed
    q = PQ(((0, '@', set('@')),))
    while len(q): #while condition should never break
        moved, self, seen = q.next()
        #verify that current path is new
        check = frozenset(seen|set(['!'+self]))
        if check in states: continue
        states.add(check)
        #break if search is finished
        if len(seen) == len(nodes): break
        #otherwise, branch out
        for k in nodes:
            if k in seen: continue
            if deps[self][k].issubset(seen):
                q.push((dists[self][k]+moved, k, seen|set([k])))
    return moved
#solve part 1
deps, dists = key_depdist_list(kpos, grid)
print dijkstra(kpos, deps, dists)
#adjust the grid for part 2
central = kpos['@']
grid[central] = '#'
for c in aoc.adj(*central): grid[c] = '#'
for c in aoc.diag(*central): grid[c] = '@'
ans2 = 0
#for every quadrant of the map
for quad in range(4):
    #find the x,y borders of the quadrant
    yma = YMA if quad%3 else central[1]+1
    ymi = central[1] if quad%3 else 0
    xma = XMA if quad<2 else central[0]+1
    xmi = central[0] if quad<2 else 0
    #get new kpos, deps, dists
    qa_kpos = dict((k,v) for k,v in kpos.items() if aoc.valid(v, xmi, xma, ymi, yma))
    qa_kpos['@'] = aoc.diag(*central)[quad]
    qa_deps, qa_dists = key_depdist_list(qa_kpos, grid)
    for k in qa_deps: #extreme assumption: doors will unlock optimally
        for o in qa_deps[k]:
            qa_deps[k][o] = set()
    #calculate and add the robot's movement
    ans2 += dijkstra(qa_kpos, qa_deps, qa_dists)
print ans2
