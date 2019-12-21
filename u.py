import aoc, e
s = aoc.sread('i.21', int, ',')
def do(script):
    r = e.construct(s)
    e.getln(r)
    r.next()
    for l in script: e.sendl(r, l)
    try:
        while 1: e.getln(r),
    except ValueError as v: print v
#part 1
do(['NOT C J',  #if not C...
    'AND D J',  #and if D, then jump
    'NOT A T',  #T=!A...
    'OR T J',   #so if A is empty, just try to jump
    'WALK'])    #end of program
#part 2
do(['OR C J',   #if J=C...
    'AND B J',  #and B, J=true
    'NOT J J',  #invert J to !C || !B...
    'AND D J',  #and if D, then...
    'OR I T',   #if T=I...
    'AND E T',  #and E...
    'OR H T',   #or H...
    'AND T J',  #then jump
    'NOT A T',  #like part 1,
    'OR T J',   #just try to jump
    'RUN'])
