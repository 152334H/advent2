with open('i.5') as f: s=map(int,f.read().split(','))
size = { 1:3, 2:3, 99:0, 3:1, 4:1, 5:2, 6:2, 7:3, 8:3}
def instr(n):
    op = n%100
    n /= 100
    modes = ()
    for i in range(size[op]):
        mode = n%10
        n /= 10
        modes += (mode,)
    return (op, modes)
i = 0
while s[i] != 99:
    op, md = instr(s[i])
    argv = ()
    for j in range(len(md)):
        argv += ((lambda m: s[i+j+1] if md[j] else s[s[i+j+1]])(md[j]),)
    if op == 1: s[s[i+3]] =  sum(argv[:2])
    elif op == 2: s[s[i+3]] =  argv[0] * argv[1]
    elif op == 3: s[s[i+1]] = int(raw_input())
    elif op == 4: print argv[0]
    elif op == 5:
        if argv[0]: i = argv[1]-len(md)-1
    elif op == 6:
        if not argv[0]: i = argv[1]-len(md)-1
    elif op == 7: s[s[i+3]] = int(argv[0] < argv[1])
    elif op == 8: s[s[i+3]] = int(argv[0] == argv[1])
    else: print "PANIC"
    i+=len(md)+1

