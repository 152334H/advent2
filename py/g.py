import itertools as it
import e, aoc   #e.py; day 5 code
s = aoc.sread('i.7', int, ',')
for r in (range(5), range(5,10)):   #both parts' code will terminate correctly
    final = []
    for t in it.permutations(r):
        gens, ls = [e.phaseinit(s, t[i])[0] for i in range(5)], []
        send, cont = 0, True
        while cont:
            for i in range(5):
                send = gens[i].send(send)
                try: gens[i].next()
                except Exception: cont = False
            ls.append(send) #for part 1, len(ls) == 1
        final.append(max(ls))
    print max(final)    #print answers
