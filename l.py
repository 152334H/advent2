import aoc, re
from fractions import gcd
s = aoc.sreadlines('i.12')
moons = [map(int,re.findall(r"[-\d]+", l)) for l in s]
vel = [[0 for _ in range(3)] for __ in range(4)]
coincidences = [None, None, None]
init = [l[:] for l in moons]
i = 0
while 1:
    if i == 1000:
        ke = [sum(map(abs, l)) for l in vel]
        pe = [sum(map(abs, l)) for l in moons]
        print sum(map(lambda t: t[0]*t[1], zip(ke, pe)))
    if i % 10000 == 0: print moons,vel
    mcp = [l[:] for l in moons]
    for a in range(len(moons)):
        for b in range(4):
            if a == b: continue
            for ax in range(3):
                if moons[a][ax] < moons[b][ax]:
                    vel[a][ax] += 1
                elif moons[a][ax] > moons[b][ax]:
                    vel[a][ax] -= 1
        for ax in range(3): mcp[a][ax] += vel[a][ax]
    moons = mcp
    i += 1
    for ax in range(3):
        if coincidences[ax]: continue
        if [l[ax] for l in moons] == [l[ax] for l in init]:
            if [l[ax] for l in vel] == [0 for _ in range(4)]:
                coincidences[ax] = i
    if None not in coincidences: break
print reduce(lambda a,b: a*b/gcd(a,b), coincidences)
