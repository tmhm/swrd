from clA import clA

print "this is in file B."

class clB:
	def	__init__(self,value):
		print "this is class B init %s " % value

	def test(self):
		print "this is in class B test"

if __name__ == "__main__":
	tb = clB(2)
	tb.test()
	ta = clA(10)
	ta.test()
