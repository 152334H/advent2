import aoc
s = aoc.sreadlines('i.1', int)
def fuel(m): return m/3-2
print sum(map(fuel,s))
a2 = 0
for i in s:
  i = fuel(i)
  while i > 0: #dumb, working solution
    a2 += i
    i = fuel(i)
print a2
