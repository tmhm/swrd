# http://www.hawstein.com/posts/dp-novice-to-advanced.html
# https://www.topcoder.com/community/data-science/data-science-tutorials/dynamic-programming-from-novice-to-advanced/

def coin_num(N,V):
	#minNum = [0]*(N+1)
	minNum = [i for i in xrange(N+1)]
	cla = len(V)

	for i in xrange(1,N+1,1):
		for j in xrange(cla):
			if V[j] <= i and minNum[i - V[j]] + 1 < minNum[i]:
				minNum[i] = minNum[i -V[j]] + 1
		#else:
		#	minNum[i] = minNum[i-1] + 1
	return minNum[1:]

def coin_test(N, V):
	tmp = coin_num(N,V)
	for idx, elem in enumerate(tmp):
		print ("total:%-5s coin num:%5d" %(idx+1,elem))

# solution : LIS --  time O(N^2)
# Longest increasing subsequence
def lis_solution_Ns(A, N):
	tmp = [1]*N
	retmax = 1
	for i in xrange(N):
		for j in xrange(i):
			if A[j] <= A[i] and tmp[j] + 1 > tmp[i]:
				tmp[i] = tmp[j] + 1
		if tmp[i] > retmax:
			retmax = tmp[i]
	print A
	print tmp
	return retmax

# solution_debug
'''
def lis_solution_Ns2(A, N):
	tmp = [1]*N
	retmax = 1
	for i in xrange(N):
		for j in xrange(i):
			if A[j] <= A[i] and tmp[j] + 1 > tmp[i]:
				tmp[i] = tmp[j] + 1
		if tmp[i] > retmax:
			retmax = tmp[i]
		else:
			tmp[i] =  retmax
	print A
	print tmp
	return retmax
'''

if __name__ == "__main__":
    coin_value = [1,2,5]
    coin_test(15, coin_value)

    listA = [5, 3, 4, 8, 6, 7]
    lis_solution_Ns(listA, len(listA))

