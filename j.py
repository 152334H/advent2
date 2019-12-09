import aoc, e
s = aoc.sread('i.9', int, ',')
r = e.runtime(s)
print r.send(1)
r = e.runtime(s)
print r.send(2)
