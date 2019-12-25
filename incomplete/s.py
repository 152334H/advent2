import aoc, e
from collections import defaultdict as dd
s = aoc.sread('i.19', int, ',')
grid = dd(lambda: -1)
PART1MAGIC = 25
PART2MAGIC = 100-1
def query(x,y): #calls the intcode program
    r = e.runtime(s)
    r.send(x)
    grid[(x,y)] = r.send(y)
    return grid[(x,y)]
#build initial grid
ans1 = sum(query(_,y) for y in range(PART1MAGIC) for _ in range(PART1MAGIC))
#get init y maxima and minima
x = PART1MAGIC-1
ls = [k for k in grid if k[0] == x and grid[k]]
ymi, yma = min(ls)[1], max(ls)[1]
ymax_d = {x:yma}
def find_edge(start, f):
    go = True
    while go:
        go = f(x,start)
        start += 1
    return start-1
#do part 2
while 1:
    x+=1
    yma = find_edge(yma, query)-1
    ymi = find_edge(ymi, lambda x,y: not query(x,y))
    if x < 50: ans1 += yma-ymi+1
    ymax_d[x] = yma
    
    if x >= PART1MAGIC+PART2MAGIC:
        if ymax_d[x-PART2MAGIC] - ymi >= PART2MAGIC:
            break
print ans1
print (x-PART2MAGIC)*10000 + ymi
