import aoc, re
s = aoc.sreadlines('i.12')
moons = [map(int,re.findall(r"[-\d]+", l)) for l in s]
vel = [[0 for _ in range(3)] for __ in range(4)]
print moons
for i in range(1000):
    print i
    for v in range(4):
        print moons[v], vel[v]
    mcp, vcp = [l[:] for l in moons], [l[:] for l in vel]
    for a in range(len(moons)):
        for b in range(4):
            if a == b: pass
            for ax in range(3):
                if moons[a][ax] < moons[b][ax]:
                    vel[a][ax] += 1
                elif moons[a][ax] > moons[b][ax]:
                    vel[a][ax] -= 1
        for ax in range(3): mcp[a][ax] += vel[a][ax]
    moons = mcp
print i+1
for v in range(4):
    print moons[v], vel[v]
ke = [sum(map(abs, l)) for l in vel]
pe = [sum(map(abs, l)) for l in moons]
print sum(map(lambda t: t[0]*t[1], zip(ke, pe)))

