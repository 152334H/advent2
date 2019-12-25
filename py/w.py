import aoc, e
s = aoc.sread('i.23', int, ',')
computes = [e.runtime(s) for _ in range(50)]
for i in range(50): e.push(computes[i], i)

