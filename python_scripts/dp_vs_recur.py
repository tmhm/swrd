import time

def dpf(n):
	a, b = 1, 1
	if n < 2:
		return 1
	else:
		for i in xrange(n-1):
			a, b = b, a+b
	return b

def recf(n):
	if n < 2:
		return 1
	else:
		return recf(n-1)+recf(n-2)

if __name__ == "__main__":
	hint = 10
	ts = time.time()
	retdp = dpf(hint)
	te = time.time()
	dpt = te-ts
	
	ts = time.time()
	retre = recf(hint)
	te = time.time()
	rect = te - ts

	print retdp,retre


	print "calculate f(%s), \n dp time: %0.4f, rec time: %0.4f" %(hint, dpt, rect)

	hint = 30
	ts = time.time()
	retdp = dpf(hint)
	te = time.time()
	dpt = te-ts
	
	ts = time.time()
	retre = recf(hint)
	te = time.time()
	rect = te - ts

	print retdp,retre
	print "calculate f(%s), \n dp time: %0.4f, rec time: %0.4f" %(hint, dpt, rect)


	hint = 40
	ts = time.time()
	retdp = dpf(hint)
	te = time.time()
	dpt = te-ts
	
	ts = time.time()
	retre = recf(hint)
	te = time.time()
	rect = te - ts

	print retdp,retre
	print "calculate f(%s), \n dp time: %0.4f, rec time: %0.4f" %(hint, dpt, rect)
