import aoc
from textwrap import wrap
from collections import Counter as C
H = 6
W = 25
PX = H*W
s = wrap(aoc.sread('i.8'), PX)

line = C(min((C(t)['0'],t) for t in s)[1])
print line['1']*line['2']

im = ['2']*PX
for l in s:
    im = [l[i] if im[i] == '2' else im[i] for i in range(len(l))]
print '\n'.join([''.join([['.','@',' '][int(im[y*W+x])] for x in range(W)]) for y in range(H)])
