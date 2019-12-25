import aoc, re
#read input
s = aoc.sreadlines('i.22')
opls = []
for l in s:
    ls = re.findall('[-\d]+', l)
    if 'with' in l: opls.append(('inc', int(ls[0])))
    elif 'into' in l: opls.append(('deal', None))
    elif 'cut' in l: opls.append(('cut', int(ls[0])))
#part 1
SIZE = 10007
def deal(v): return SIZE-1-v
def cut(v, N): return v-N
def inc(v, N): return v*N %SIZE
def shuffle(p, ops):
    for op, val in ops:
        if op == 'inc': p = inc(p, val)
        elif op == 'deal': p = deal(p)
        elif op == 'cut': p = cut(p, val) %SIZE
    return p
print shuffle(2019, opls) #ignore the rest of the deck; just focus on position of card 2019
#part 2: working backwards
p = 2020
SIZE = 119315717514047
REPLAY = 101741582076661
def modinv(N): return pow(N, SIZE-2, SIZE) #since SIZE is prime, FLT implies invmod(a,p) == a**(p-2) (mod p)
#redefine the functions to be their reverse
def cut(newv, N): return (newv+N) %SIZE
#note: each return value of new_inc() is unique to its input
def inc(newv, N): return modinv(N)*newv %SIZE
y = shuffle(p, reversed(opls))
'''even when reversed, shuffle(p) is a linear transform of p -> a*p+b (mod SIZE)
hence, shuffle(p) repeated n times is equivalent to the expansion,
    pa^n + ba^{n-1} + ba^{n-2} + ... + b == pa^n + (a^{n-1} / (a-1)*b)'''
a = (y-shuffle(y, reversed(opls)))*modinv(p-y) %SIZE
#b == y-a*p
print (p*pow(a,REPLAY,SIZE) + (pow(a,REPLAY,SIZE)-1) * modinv(a-1)*(y-a*p))%SIZE
