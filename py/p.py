import aoc
s = [int(c) for c in aoc.sread('i.16')] #, int, '')
#s = []
#for _ in range(10000): s += inp[:]
#s = reduce(lambda a,b: a+b, [inp[:] for _ in range(10000)])
#s = [int(c) for c in aoc.sread('i.16')]*10000
offset = int(''.join(map(str, s[:7])))
print offset
#s = [1,2,3,4,5,6,7,8]
le = len(s)
#print s, le
pat = [0,1,0,-1]
for p in range(100):
    o = []
    for i in range(len(s)):
        su = 0
        for j in range(len(s)):
            v = ((j+1)/(i+1))%4
            if v == 1: su += s[j]
            elif v == 3: su -= s[j]
        o.append(abs(su)%10)
        #o.append(abs(sum(pat[((j+1)/(i+1))%4]*s[j] for j in range(len(s))))%10)
    s = o
    print ''.join(map(str, s))
    #print p
#print ''.join(map(str,s[offset:offset+8]))
