from collections import defaultdict as dd
import aoc
s = [map(lambda m: (int(m[1:])*(lambda c: -1 if c in "DL" else 1)(m[0]), m[0]), l) for l in aoc.sreadlines('i.3', div=',')]
inv={'x':'y', 'y':'x'}

lines = []
for snake in s:
  paths = { 'x': dd(lambda:[]), 'y': dd(lambda:[])}
  coord = {'x':0, 'y':0} #tracks current position
  dist = 0
  for m in snake: #for each move
    dir = m[1] in "RL" and 'y' or 'x'
    paths[dir][coord[dir]].append((dist,
    (coord[inv[dir]],coord[inv[dir]]+m[0]),m[1]))
    coord[inv[dir]]+=m[0]
    dist+=abs(m[0])
  lines.append(paths)

def fdist(l, ol, ok, k):
  dist = l[0] + ol[0]
  if l[2] in "RU": dist += ok-min(l[1])
  else: dist += max(l[1])-ok
  if ol[2] in "RU": dist += k-min(ol[1])
  else: dist += max(ol[1])-k
  return dist

icepts = set()
for dir in ('x','y'):
  d = lines[0][dir]
  for k in d:
    for l in d[k]: #usually only 1 member
      for ok in lines[1][inv[dir]]:
        if ok >= min(l[1]) and ok <= max(l[1]):
          for ol in lines[1][inv[dir]][ok]:
            if k >= min(ol[1]) and k <= max(ol[1]):
              icepts.add((dir == 'y' and (ok, k) or (k, ok)) + (fdist(l,ol,ok,k),))
      if k in lines[1][dir]: #prevent generation of k:[]
        for ol in lines[1][dir][k]: #in the event that two lines running on the same axis overlap
          for i in range(max(min(l[1]),min(ol[1])),min(max(l[1]),max(ol[1]))+1):
            icepts.add((dir == 'y' and (i, k) or (k, i)) + (fdist(l,ol,i,i),))
icepts.remove((0,0,0))

print min([sum(map(abs,t[:2])) for t in icepts])
print min([t[2] for t in icepts])
