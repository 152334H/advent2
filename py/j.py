import aoc
from math import atan2, pi
class Vect(tuple): #to overload '-' operator
    def __sub__(self, other):
        return Vect(x-y for x,y in zip(self, other))

ma = 0
s = aoc.sreadlines("i.10")
riods = [Vect([x,y]) for y in range(len(s)) for x in range(len(s[0])) if s[y][x] == '#']
def angle(x,y):
    #note: the axis of y is flipped
    a = atan2(y,x)
    if x < 0 and y < 0: a += 2*pi
    return a
for cur in riods: #each calculation here is repeated unnecessarily once
    angs = set()
    for comp in riods:
        if comp == cur: continue
        ang = angle(*comp-cur)
        if ang not in angs: #this does not find the closest '#', but it does count correctly
            angs.add(ang)
    v = len(angs)
    if ma < v:
        ma = v
        best = cur
print ma

def sqsum(t): sum(map(lambda v: v*v, t))
targets = set(riods)
targets.remove(best)
i = 0
while 1:
    angs = {}
    for comp in targets:
        ang = angle(*comp-best)
        if ang not in angs or sqsum(angs[ang]-best) > sqsum(comp-best):
            angs[ang] = comp
    v = len(angs)
    
    if i+v < 200:
        for k in angs: targets.remove(k)
        i += v
    else:
        ls = sorted(angs.items())
        _, ans = ls[199-i]
        print ans[0]*100+ans[1]
        break
