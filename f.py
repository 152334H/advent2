import aoc
s = aoc.sreadlines('i.6', div=')')
loc = {'COM':()}    #path of root to node
ptr = {'COM':{}}   #pointer to node
while len(s): #s is gradually shrunk
    i = 0
    for orb in s[:]: #make a copy
        if orb[0] not in loc: i+=1
        else: #if orbit can be attached to cur tree
            loc[orb[1]] = loc[orb[0]]+(orb[1],)
            ptr[orb[1]] = ptr[orb[0]][orb[1]] = {}
            del s[i]
print sum(len(v) for v in loc.values())
san, you = loc['SAN'], loc['YOU']
while san[i] == you[i]: i += 1 #i starts at 0
print len(san)-i+len(you)-i-2 #-2 to exclude SAN & YOU
'''
from networkx import *
#for a in (lambda g:(sum(len(ancestors(g,h)) for h in g.node),len(shortest_path(g.to_undirected(),'YOU','SAN'))-3))(read_edgelist('i.6','#',')',DiGraph())):print a
g = read_edgelist('i.6','#',')',DiGraph())
'''
