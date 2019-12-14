import aoc
from collections import defaultdict as dd
#read input
s = aoc.sreadlines('i.14',div=' => ')
def getChemPair(p): #splits apart e.g. "5 ORE" into (5, "ORE")
    return (lambda n, cpd: (int(n), cpd))(*p.split(' '))
requires = {} #mapping of products to their requirements
for react, prod in s:
    n, cpd = getChemPair(prod)
    requires[cpd] = (n,tuple(map(getChemPair, react.split(', '))))
#functions for part 1/2
def getReq(cpd, coeff, extra): #where extra is a dict of leftover reactants
    n, react = requires[cpd]
    coeff -= extra[cpd] #use extra
    extra[cpd] = 0      #and reset
    stio = coeff/n
    if coeff % n: #if there are leftovers
        stio += 1
        extra[cpd] += n-(coeff%n)
    return sum(num*stio if sub == 'ORE' else getReq(sub, num*stio, extra) for num, sub in react) #recurse until ORE
def getFuelReq(coeff):  #wrapper call to localise extra
    extra = dd(lambda: 0)
    return getReq('FUEL', coeff, extra)
#part 1
print getFuelReq(1)
#part 2: binary search
for i in range(50): #find appropriate i to start binary search on
    if getFuelReq(1<<i) > 10**12: break
else: "err: maxmimum i not found. Please increase the range of this for loop"
c = 1<<i    #c is the test value for getFuelReq(c)
sign = True #start by decreasing c
while i:
    i -= 1  #decrease the exponent
    c += [1,-1][sign]*(1<<i)    #increase/reduce c
    sign = getFuelReq(c) > 10**12
if sign: c-=1 #if binary search ended off-by-one
print c
