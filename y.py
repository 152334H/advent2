import aoc, e
from collections import defaultdict as dd
s = aoc.sread("i.25", int, ',')
r = e.runtime(s)
def toNextCmd(r):
    recv = ''
    try:
        while 'Command?' not in recv: recv += e.getln(r)
        r.next()
    except StopIteration: pass
    return recv
def brute(r):
    import itertools as it
    items = ['ornament', 'hypercube', 'mug', 'prime number', 'astronaut ice cream', 'mouse', 'wreath', 'easter egg']
    for tup in it.chain.from_iterable(it.combinations(items, r) for r in range(len(items)+1)):
        #print tup
        for item in tup:
            e.sendl(r, 'take '+item)
            toNextCmd(r)
        e.sendl(r, 'north')
        #print toNextCmd(r)
        for item in tup:
            e.sendl(r, 'drop '+item)
            toNextCmd(r)
#step 1: manually collect all items, move to the room below the checkpoint, and drop all items
try:
    while 1:
        print toNextCmd(r)
        e.sendl(r, raw_input())
except KeyboardInterrupt: pass
#step 2: bruteforce combinations of items
brute(r)
