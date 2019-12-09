import aoc, e
from collections import defaultdict as dd
s = aoc.sread('i.2', int, ',')
for n in range(100): #small enough to bruteforce
    for v in range(100):
        s[1:3] = n,v
        cpy = s[:]
        for _ in e.intcode(cpy): pass
        if n == 12 and v == 2: print cpy[0]
        if cpy[0] == 19690720: print n*100+v
