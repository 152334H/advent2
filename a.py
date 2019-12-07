def fuel(m): return m/3-2
with open('i.1') as f: s=map(int,f.read().split('\n')[:-1])
print sum(map(fuel,s))
a2 = 0
for i in s:
  i = fuel(i)
  while i > 0: #dumb, working solution
    a2 += i
    i = fuel(i)
print a2
