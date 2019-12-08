import aoc
s = aoc.sread('i.4', int, '-')
s[1]+=1 #necessary for range()

def prange(mi, ma, e): #limited, non-descending range()
    return e and reduce(lambda a, b: a+b,
            ((lambda v: map(lambda x: x+v, prange(i, 9, e-1)))(i*10**e)
                for i in range(mi, ma+1))
            ) or range(mi, ma+1) #input is small enough for recursion
def fprange(s): #full non-desc range
    e = 5 #challenge range is always 6 digits
    first, last = map(lambda v:v/10**e,s)
    return [v for v in prange(first, first, e) if v > s[0]] + prange(first+1, last-1, e) + [v for v in prange(last, last, e) if v<s[1]]

ans1, ans2 = 0, 0
for i in fprange(s): #only adjacency check remaining
    enum, prev, c = set(), None, 1
    for cur in str(i):
        if prev != cur:
            enum.add(c)
            prev = cur
            c = 1
        else: c+=1
    enum.add(c)
    if len(enum) > 1:
        ans1+=1
        if 2 not in enum: ans2+=1
print ans1
print ans1-ans2
