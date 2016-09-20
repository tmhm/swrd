def Eval(N):
	c = [0]*(N+1)
	c[0] = 1.0
	for i in xrange(1,N+1,1):
		s = 0.0
		for j in xrange(i):
			s += c[j]
		c[i] = 2.0*s/i + i
	return c[N]

def Eval_N(N):
	s, tmp =  1.0, 1.0
	for i in xrange(1,N+1,1):
		s = 2.0*tmp/i + i
		tmp += s
	return s

def Fibonacci_l(N):
	a,b = 1, 1
	for i in xrange(N):
		print (i,a)
		a,b = b, a+b
	
def Fibonacci_list(N):
	ret = [1,1]
	if N < 2:
		return ret[:N+1]
	else:
		for i in xrange(2,N,1):
			ret.append(ret[-1]+ret[-2])
	return ret

