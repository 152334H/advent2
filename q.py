import aoc, e
s = aoc.sread('i.17', int, ',')
#part 1: get the grid
r = e.construct(s)
grid = ''
rtr = r.next()
while rtr != None:
    grid += chr(rtr)
    try: rtr = r.next()
    except StopIteration: break
grid = grid.split('\n')
while grid[-1] == '': grid = grid[:-1]
grid = [list(l) for l in grid]
xma = len(grid[0])
yma = len(grid)
#test for intersections
def isSect(grid, x, y):
    adj = []
    if x: adj.append((x-1,y))
    if y: adj.append((x,y-1))
    if x+1 < xma: adj.append((x+1, y))
    if y+1 < yma: adj.append((x, y+1))
    return sum(1 for a, b in adj if grid[b][a] in '#') > 2 #in case an intersection appears on the map's borders
print sum(y*x for y in range(yma) for x in range(xma) if grid[y][x] == '#' and isSect(grid, x, y)) #print part 1
#for y in range(yma): print ''.join(grid[y])
#part 2: hardcoding
s[0] = 2
r = e.construct(s)
nlc = -1
while nlc < yma:
    if r.next() == 10: nlc+=1
def getln(): #gets a line from intcode
    t = ''
    while 1:
        v = r.next()
        try: t+=chr(v)
        except ValueError:
            print v #for part 2
            exit()
        if v == ord('\n'): break
    r.next()
    return t
for l in ['A,B,B,C,C,A,A,B,B,C', 'L,12,R,4,R,4', 'R,12,R,4,L,12', 'R,12,R,4,L,6,L,8,L,8', 'n']:
    getln()
    for c in l: r.send(ord(c))
    e.push(r, 10)
while 1: getln()
