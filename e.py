def instr(n):
    SIZE = {1:3, 2:3, 99:0, 3:1, 4:1, 5:2, 6:2, 7:3, 8:3}
    op = n%100
    n /= 100
    modes = ()
    for i in range(SIZE[op]):
        mode = n%10
        n /= 10
        modes += (mode,)
    return (op, modes)

def intcode(s):
    i = 0
    while s[i] != 99:
        op, md = instr(s[i])
        argv = ()
        for j in range(len(md)):
            argv += ((lambda m: s[i+j+1] if md[j] else s[s[i+j+1]])(md[j]),)
        if op == 1: s[s[i+3]] =  sum(argv[:2])
        elif op == 2: s[s[i+3]] =  argv[0] * argv[1]
        elif op == 3: s[s[i+1]] = yield#int(raw_input())
        elif op == 4: yield argv[0]#print argv[0]
        elif op == 5:
            if argv[0]: i = argv[1]-len(md)-1
        elif op == 6:
            if not argv[0]: i = argv[1]-len(md)-1
        elif op == 7: s[s[i+3]] = int(argv[0] < argv[1])
        elif op == 8: s[s[i+3]] = int(argv[0] == argv[1])
        else: print "PANIC"
        i+=len(md)+1

def runtime(s):
    r = intcode(s[:])   #deep copy to prevent s[] modification
    r.next()    #initiates code execution
    return r

def phaseinit(s, v):
    r = runtime(s)
    return r, r.send(v)

if __name__ == "__main__":
    import aoc
    s = aoc.sread('i.5', int, ',')
    r = phaseinit(s, 1)[0]
    for rtr in r: pass  #seek to end of generator
    print rtr   #print last value
    print phaseinit(s, 5)[1]    #print sole value of input 5
