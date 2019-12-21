import operator as O
from collections import defaultdict as dd
def instr(n):
    SIZE = {1:3, 2:3, 99:0, 3:1, 4:1, 5:2, 6:2, 7:3, 8:3, 9:1}
    op = n%100
    n /= 100
    modes = ()
    for i in range(SIZE[op]):
        mode = n%10
        n /= 10
        modes += (mode,)
    return (op, modes)
DEBUG = 0
def intcode(s, rb=0, i=0):
    try: 
        while s[i] != 99:
            op, md = instr(s[i])
            pargv = tuple([[s[i+j+1], i+j+1, s[i+j+1]+rb][md[j]] for j in range(len(md))])
            argv = tuple([s[pargv[j]] for j in range(len(md))])
            if DEBUG:
                    print "[%d] code: (" % i,
                    for j in range(4): print "%d," % s[i+j],
                    print ") op: %d," % op,
                    print "rb: %d," % rb,
                    print "modes: %r" % zip(md, pargv)
            if op == 1:
                s[pargv[2]] = sum(argv[:2])
            elif op == 2:
                s[pargv[2]] = reduce(O.imul, argv[:2])
            elif op == 3:
                s[pargv[0]] = yield
            elif op == 4:
                try: yield argv[0]#print argv[0]
                except ValueError:
                    yield None
                    yield argv[0]
            elif op == 5:
                if argv[0]: i = argv[1]-len(md)-1
            elif op == 6:
                if not argv[0]: i = argv[1]-len(md)-1
            elif op == 7:
                s[pargv[2]] = reduce(O.lt, argv[:2])
            elif op == 8:
                s[pargv[2]] = reduce(O.eq, argv[:2])
            elif op == 9:
                rb += argv[0]
            else: print "PANIC"
            i+=len(md)+1
    except RuntimeError: yield (s, rb, i)
def construct(s):
    d = dd(lambda: 0, enumerate(s))
    return intcode(d)

def cont(t):
    r = intcode(*t)
    r.next()
    return r

def runtime(s):
    r = construct(s)#s[:] + [0]*999999)   #deep copy to prevent s[] modification; [0]*999999 because of day 9
    v = r.next()    #initiates code execution
    if v: print "Warn: intcode initalisation returned %d" % v
    return r

def push(r,v): #send, but don't get next()
    if r.send(v) != None: r.throw(ValueError)

def safeNext(r):
    v = r.next()
    if v == None: raise ValueError
    return v

def phaseinit(s, v):
    r = runtime(s)
    return r, r.send(v)

def sendl(r, l): #sends an ASCII line to intcode, terminated with '\n'
    for c in l: r.send(ord(c))
    push(r, 10)

def getln(r): #gets an ASCII line from intcode
    t = ''
    while 1:
        v = r.next()
        try: t+=chr(v)
        except ValueError:
            raise ValueError, v
        if v == ord('\n'): break
    return t

if __name__ == "__main__":
    import aoc
    s = aoc.sread('i.5', int, ',')
    for rtr in phaseinit(s, 1)[0]: pass  #seek to end of generator
    print rtr   #print last value
    print phaseinit(s, 5)[1]    #print sole value of input 5
