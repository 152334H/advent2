import aoc, e
from collections import defaultdict as dd
s = aoc.sread("i.13", int, ',')
PLAY = 0 #change this to simulate the game

def safeNext(r):
    v = r.next()
    if v == None: raise ValueError
    return v
def push(r,v): #send, but don't get next()
    if r.send(v) != None: r.throw(ValueError)
def getGrid(r, grid):
    global score
    try:
        while 1:
            x, y, v = safeNext(r), safeNext(r), safeNext(r)
            if (x,y) == (-1,0): score = v
            else: grid[(x,y)] = v
    except Exception: return grid
grid = getGrid(e.construct(s), dd(lambda: 0))
print len([0 for v in grid.values() if v == 2]) #part 1

def predict(grid):
    ball = [p for p,v in grid.items() if v == 4][0][0]
    pad = [p for p,v in grid.items() if v == 3][0][0]
    if ball > pad: return 1
    elif ball < pad: return -1
    return 0
s[0] = 2
score = 0
r = e.construct(s)
push(r, None)
while 1:
    getGrid(r, grid)
    if PLAY:
        from mplay import joystick
        joy = joystick(grid)
    if not PLAY or joy == None:
        joy = predict(grid)
    try: push(r,joy)
    except StopIteration: break
print score
