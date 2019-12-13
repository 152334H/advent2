import aoc, e
from collections import defaultdict as dd
from getkey import getkey, keys
s = aoc.sread("i.13", int, ',')
MAP = {0:' ', 1:'#', 2:'@', 3:'H', 4:'o'}
c = 0
def toGrid(d):
    l = d.keys()
    xma, xmi = max(l)[0], min(l)[0]
    l = [t[1] for t in l]
    yma, ymi = max(l), min(l)
    s = ""
    for y in range(yma, ymi-1, -1):
        for x in range(xmi, xma+1):
            s+=MAP[d[(x,y)]]
        s += '\n'
    return s
def getGrid(r):
    grid = dd(lambda: 0)
    try:
        while 1:
            x = r.next()
            y = r.next()
            if (x,y) == (-1,0): print "score: %d" % r.next()
            else: grid[(x,y)] = r.next()
        return grid
    except Exception: return grid
grid = getGrid(e.construct(s))
print toGrid(grid).count('@')
def safeNext(r):
    v = r.next()
    if v == None:
        r.throw(IndexError)
        raise IndexError
    return v
s[0] = 2
r = e.construct(s)
prev = r.send(None)
joy = 0
ap = 1<<31
score = 0
while 1:
    try:
        while 1:
            if prev != None:
                x = prev
                prev = None
            else: x = safeNext(r)
            y = safeNext(r)
            if (x,y) == (-1,0): score = r.next() #score is always ascending
            else: grid[(x,y)] = safeNext(r)
    except StopIteration: pass
    except IndexError: pass
    #print toGrid(grid)
    if ap:
        ap -= 1
        k = '>'
    else: 
        k = getkey()
    if k == keys.UP or k == keys.DOWN: joy = 0
    elif k == keys.LEFT: joy = -1
    elif k == keys.RIGHT: joy = 1
    else:#autoplay
        if k.isdigit():#press 0-9 to plsy 10**k times
            ap += 10**int(k)
        ball = [p for p,v in grid.items() if v == 4][0][0]
        pad = [p for p,v in grid.items() if v == 3][0][0]
        if ball > pad: joy = 1
        elif ball < pad: joy = -1
        else: joy = 0
    try: prev = r.send(joy)
    except StopIteration: break
print score
