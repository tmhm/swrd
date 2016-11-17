print "this is in file A."

class clA:
	menber_a = '''
				test a
				value
				'''
	   
	"""
		this is function
	"""
	def	__init__(self,value):
		print "this is class A init %s " % value

	def test(self):
		print "this is in class A test"

if __name__ == "__main__":
	ta = clA(1)
	ta.test()
