with open('i.2') as f: o=map(int,f.read().split(','))
for n in range(100): #small enough to bruteforce
	for v in range(100):
		i = 0
		s = o[:]
                s[1:3] = n, v
		while s[i] != 99:
			if s[i] == 1:
				s[s[i+3]] = s[s[i+1]] + s[s[i+2]]
			elif s[i] == 2:
				s[s[i+3]] = s[s[i+1]] * s[s[i+2]]
			else: print "PANIC"
			i+=4
		if n == 12 and v == 2: print s[0]
		if s[0] == 19690720: print n*100+v
