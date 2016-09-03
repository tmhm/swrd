
[codility lessons](#1)
 
* [lesson 1: *Iterations*](#1.1)
	* [1. BinaryGap](#1.1.1)
* [lesson 2: *Arrays*](#1.2)
	* [1. CyclicRotation](#1.2.1)
	* [2. OddOccurrencesInArray](#1.2.2)

* [lesson 3: *Time complexity*](#1.3)
	* [1. TapeEquilibrium](#1.3.1)
	* [2. FrogJmp](#1.3.2)
	* [3. PermMissingElem](#1.3.3)

* [lesson 4: *counting elements*](#1.4)
	* [1. FrogRiverOne](#1.4.1)
	* [2. PermCheck](#1.4.2)
	* [3. MissingInteger](#1.4.3)
	* [4. MaxCounters](#1.4.4)

* [lesson 5: *prefix sums*](#1.5)
	* [1. PassingCars](#1.5.1)
	* [2. CountDiv](#1.5.2)
	* [3. GenomicRangeQuery](#1.5.3)
	* [4. MinAvgTwoSlice](#1.5.4)

* [lesson 6: *sorting*](#1.6)
	* [1. Distinct](#1.6.1)
	* [2. MaxProductOfThree](#1.6.2)
	* [3. Triangle](#1.6.3)
	* [4. none](#1.6.4)

* [lesson 7: *stacks and queues*](#1.7)
	* [1. none](#1.7.1)
	* [2. Nesting](#1.7.2)
	* [3. none](#1.7.3)
	* [4. MaxCounters](#1.4.4)



<h1 id = "1"> 
codility lessons
</h1>

- 切记临界点， 比如一个最小，最大的值， len(0), max() 无数据等
- 仔细看好题意， 比如是要求从1 开始的list ，就不需要记最好的值，求长度了，只要记下最大值。

<h2 id = "1.1"> 
lesson 1：<i>Iterations</i>
</h2>

<h3 id = "1.1.1">
1. BinaryGap-----[100%]
</h3>

> Find longest sequence of zeros in binary representation of an integer.

A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps.


解题思路：

- 将整型数据转为二进制，然后利用python的split函数按‘1’分割，再用max函数找到最大的切片即可
- 注意二进制为全1，或者第一位为1，后面全为0的数，e.g. 1, 100, 11111, 用log次的循环判定下即可
- 满足于O(log(N))的时间复杂度


```
from math import log
def solution(N):
    # write your code in Python 2.7
    
    #if N == 1:   #can belong to the next for i = 0
    #    return 0
    for i in xrange(int(log(N,2))+1):
        
        tmp = 2**i
        #print tmp
        if tmp == N+1 or tmp == N:
            return 0 
            
    strb = bin(N).split("1")
    #print strb[1:-1]  
	#last one can't included. e.g.1001000->2, so [1:-1]
    if strb[1:-1] is None:
        #print "test"
        return 0
    return max([len(l) for l in strb[1:-1]])
```

<h2 id = "1.2"> 
lesson 2: <i>Arrays</i>
</h2>

- exercise:
- Problem: Given array A consisting of N integers, return the reversed array.


```
def myreverse(A):
    length = len(A)
    for i in xrange(length//2):
        A[i], A[length -i-1] = A[length - i-1], A[i]
    return A
    
```

<h3 id = "1.2.1"> 
1. CyclicRotation------[100%] 
</h3>

> Rotate an array to the right by a given number of steps.


A zero-indexed array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is also moved to the first place.

For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7]. The goal is to rotate array A K times; that is, each element of A will be shifted to the right by K indexes.

```
def re_enumerate(seq):
    n = -1
    length = len(seq)
    for elem in reversed(seq):
        yield length + n, elem
        n = n - 1

def solution(A, K):
    # write your code in Python 2.7
    length = len(A)
    if length < 2:
        return A
    shift_times = K%length
    #print shift_times
    tmp= A[-shift_times:]
    #print tmp
    tmp.extend(A[:- shift_times])
    return tmp
    #for idx, ai in re_enumerate(A):
    #    if idx >= shift_times:
    #        A[idx] = A[idx-shift_times]
    #        
    #    else:
    #        A[idx] = tmp[idx]
    #return A   

```

- 要注意边界条件，考虑数组的长度少于旋转的次数，以及只有一个元素和数组为空
- 当有除法的时候，注意是否除以零

```
def solution(A, K):
    # write your code in Python 2.7
    length = len(A)
    #print length
    #print K
    if K == 0 or length == 0 or length == 1:
        return A
    if K > length:
        K %= length 

    #print K
    tmp = [0]*K
    #print tmp
    for i in xrange(K):
        tmp[i] = A[length - K + i]
    tmp.extend(A[:-K])
    return tmp
```

<h3 id = "1.2.2"> 
2. OddOccurrencesInArray ---[100%]
</h3>

> Find value that occurs in odd number of elements.

A non-empty zero-indexed array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:

	  A[0] = 9  A[1] = 3  A[2] = 9
	  A[3] = 3  A[4] = 9  A[5] = 7
	  A[6] = 9
  
- the elements at indexes 0 and 2 have value 9,
- the elements at indexes 1 and 3 have value 3,
- the elements at indexes 4 and 6 have value 9,
- the element at index 5 has value 7 and is unpaired.


解题思路：

- 将数组排序，相同的数会在一起，比较前后两个数是否相同 
- 偶数个数的，继续测试下一个数，找到单独的一个数，返回
- 当直到数组最后，还有没有找到单独的一个元素，我们得返回最后一个元素，因为我们统计的一直的是last 元素
- 注意临界条件，只有一个元素
- O(N)时间复杂度

```
def solution(A):
    # write your code in Python 2.7
    if len(A) == 1:
        return A[0]
    A.sort()
    #print A
    last_a,cnt = A[0],1
    #print last_a
    for ai in A[1:]:
        if ai == last_a:
            cnt += 1
        else:
            if cnt%2 != 0:
                return last_a
            last_a,cnt = ai,1
        
    return A[-1]    
 
```
---------

```
def solution(A):
    # write your code in Python 2.7
    if len(A) < 2:
        return A[0]
    A.sort()
    last_a, cnt = A[0], 1
    for a in A[1:]:
        if last_a == a:
            cnt += 1
        else:
            if cnt%2 == 0 :
                last_a, cnt = a, 1
            else:
                return last_a
    return A[-1]      
 
```
 
 -----------
 

<h2 id = "1.3"> 
lesson 3: <i>Time complexity</i>
</h2>

- exercise:
- Problem: You are given an integer n. Count the total of 1+2+...+n.


```
def sumN(N):
    return N*(N+1)//2

```

<h3 id = "1.3.1"> 
1. TapeEquilibrium -----[100%] 
</h3>

> Minimize the value 
|(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.

A non-empty zero-indexed array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

**note:** 依次求sum

```
def solution(A):
    # write your code in Python 2.7
    
    #left,right =A[0], sum(A)-A[0]
    left,right =A[0], sum(A[1:])
    result = abs(right - left)
    
    for elem in A[1:-1]:
        left,right = left + elem, right - elem
        retmp = abs(right - left)
        if retmp < result:
            result = retmp
    return result
```

<h3 id = "1.3.2"> 
2. FrogJmp -----[100%] 
</h3>


>Count minimal number of jumps from position X to Y.

A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its target.


**note:** O(1) time complexity, 注意是否在边界上，否则加1即可。

```
def solution(X, Y, D):
    # write your code in Python 2.7
    if X == Y:
        return 0
    else:
        flag = (Y - X)%D
        ret = (Y - X)/D
        return ret if flag == 0 else ret + 1
```

<h3 id = "1.3.3"> 
3. PermMissingElem -----[100%] 
</h3>


>Find the missing element in a given permutation.

A zero-indexed array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

**note:**

- 简单思路是排序，然后依此比较是否是增1关系，也可以用求sum的方式
- 注意边界条件，N取值［0，100，000］， 元素取值［1，N+1］，
- 故当没有元素的时候，返回1；当只有一个元素的时候，需要考虑元素是否是1
- 当全部有序的时候，考虑最后元素＋1返回。

```
def solution(A):
    # write your code in Python 2.7
    if len(A) == 0:
        return 1
    elif len(A) == 1:
        return A[0]+1 if A[0] == 1 else A[0] -1
    A.sort()
    left = A[0]
    for elem in A[1:]:
        if elem == left + 1:
            left = elem    
            continue
        else:
            return left + 1
            
    return A[-1]+1 if A[0] == 1 else A[0]-1
```
--------



```
def solution(A):
    # write your code in Python 2.7
    length = len(A)
    if length < 1:
        return 1
    #elif length < 2:  # can belong to the next tatal_sum
    #    return 1 if A[0]==2 else 2
        
    tatal = sum([i for i in xrange(1,length+2,1) ])
    tmp = sum(A)
    return tatal - tmp
    
```



<h2 id = "1.4"> 
lesson 4: <i>counting elements</i>
</h2>

- exercise
- Problem: You are given an integer m (1 <= m <= 1,000,000) and two non-empty, zero-indexed arrays A and B of n integers, a0,a1,...,an−1 and b0,b1,...,bn−1 respectively (0 <= ai,bi <= m).

>For every element of array B, we assume that we will swap it with some element from array A. The difference d tells us the value from array A that we are interested in swapping, because only one value will cause the two totals to be equal. The occurrence of this value can be found in constant time from the array used for counting.

**NOTE:**

- 假设A中ai和B中的bj交换可以满足要求，则有：A＋bj－ai ＝＝ B＋ai－bj
- 假设 d ＝ bj － ai， 则有 A ＋ d ＝ B － d
- 故有A－B ＝ 2d， 因此，两个数组的差必须是2的整数倍，即偶数，否则不存在交换可以满足题意的元素
- 然后由d ＝ bj － ai，得到在A中存在元素ai ＝ bj － d。我们可以对每一个B中的元素bj，查找A中是否有bj－d 即可。

```
def counting(A, m):	n = len(A) 
	count=[0]*(m+1) 
	for k in xrange(n):		count[A[k]] += 1 
	return count
	
	
#from collections import Counter
def fast_solution(A, B, m):	n = len(A)	sum_a = sum(A)	sum_b = sum(B)	d = sum_b - sum_a 
	if d%2==1:		return False 
	d//=2	count = counting(A, m) 
	for i in xrange(n):		if 0 <= B[i] - d <= m and count[B[i] - d] > 0: 
			return True	return False

```
> 根本目的是找到A中存在元素ai ＝ bj － d， 前面的Bj －d 范围在 ［0，m］只是限定count的范围，防止越界！
> 
> 若使用collections 的Counter 函数计数，则可以直接查看是否存在bj－d这个元素即可，即count[bj-d] > 0要求。 
> 
> 我们也可以直接用for everyone B element， 判断if （bj － d） in A 也可以,但是这样的复杂度又变高了， 变成O(N^2)了。因为，每次查找（bj － d） 是否in A 的时候就要N次遍历查找。
> **因此，还是用计数的方式好，首先统计A中的元素，以后只要O(1)的时间查找是否存在我们需要的ai。** 

可以有如下解答：

**so,we can do it as follows:**

```
from collections import Counter
def fast_solution(A, B, m):	n = len(A)	sum_a = sum(A)	sum_b = sum(B)	d = sum_b - sum_a 
	if d%2==1:		return False 
	d//=2	count = Counter(A, m) 
	for i in xrange(n):		if count[B[i] - d] > 0: 
			return True	return False

```



<h3 id = "1.4.1"> 
1. FrogRiverOne----[100%] 
</h3>

> Find the earliest time when a frog can jump to the other side of a river.
> 
> The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.
> 
> **each element of array A is an integer within the range [1..X].**

- 鉴于元素的范围，所以，可以用list保存出现过的元素，比较list的长度跟X的关系，就可以得到第一次出现X的位置 
- 这里需要考虑的一个问题是，是第一次访问过所有的元素种类，停留的位置不要求必须是X元素；另一种情况是，不仅仅要求访问过所有的元素种类，还要最后停留在X元素上，再算达到要求。**本题解法是第一种情况。**
- 若是第二种情况的话，只需要在set的长度等于X后，多加一次判断，找到接下来第一次出现X的位置即好。

- 鉴于O(N) -time  O(X)-space ,每次在保存过的元素中查找费时间，可以直接用set保存，因为set加入新元素的时候，重复元素不会再次加入，这里应该看看[python源码set](http://svn.python.org/view/python/trunk/Objects/setobject.c?view=markup)怎么加入的。

```
def solution(X, A):
    # write your code in Python 2.7
    visited = set()
    for idx,elem in enumerate(A):
        visited.add(elem)
        if len(visited) == X: 
            return idx
    return -1  
```





<h3 id = "1.4.2"> 
2. PermCheck----[100%] 
</h3>


> Check whether array A is a permutation.

**note:**

思路一：

- 用最大值是否等于set的长度来测试.
仔细看好题意， 比如是要求从1 开始的list ，
就不需要记最小的值，求长度了，只要记下最大值。

```
def solution(A):
    # write your code in Python 2.7
    #A.sort() # Nlog(N)
    if len(A) == 1:
        return 1 if (A[0] == 1) else 0
    
    sigle = set()
    #maxelem, minelem = A[0], A[0]   #needless minelem,owing to from 1 !!
    maxelem = A[0]
    for elem in A:
        if elem not in sigle:
            sigle.add(elem)
            if elem > maxelem:
                maxelem = elem
        else:
            #print "test"
            return 0
    #print sigle
    return 1 if (len(sigle) == maxelem) else 0
    
    #return 1 if (A[-1]-A[0]+1) == len(A) else 0
```

思路二：

- 如果元素的取值是在N个范围内，即数组有N个元素，每个元素范围是[1,N] ,则我们可以用求sum的方式来做 ［score ：100%］


```
def solution(A):
    # write your code in Python 2.7
    set_a = set(A)
    
    length = len(set_a)
    total = length*(length+1)//2
    tmp = sum(A)
    return 1 if total == tmp else 0
    
```


<h3 id = "1.4.3"> 
3. MissingInteger----[100%] 
</h3>


> Find the minimal positive integer not occurring in a given sequence.

**note:**

- O(N) time & space complexity,if sort, will exceed. 
- 考虑到不能排序，从解空间出发考虑。返回解一定会在1~len(所给数组)+1的区间。用map记录这些数据是否都在，不在的话，找最小的空缺，都在的时候就是map/list最后一个数加1.

```
def solution(A):
    # write your code in Python 2.7
    length = len(A)
    tmp = [True]*(length + 1)       
    #print tmp
    for elem in A:
        if 0 < elem < length+1:
            tmp[elem-1] = False
    for idx,elem in enumerate(tmp):
        if elem == True:
            return idx+1
    return length +1    
```

```
def solution(A):
    # write your code in Python 2.7
    length = len(A)+1
    tmp = [True]*length
    for a in A:
        if 0 < a < length:
            tmp[a-1] = a
    for idx, a in enumerate(tmp):
        if a is True:
            return idx+1
    #return length
    
```
*将tmp数组增大一位，就不需要最后考虑全部是有序的，再return length ＋ 1了*

<h3 id = "1.4.4"> 
4. MaxCounters
</h3>


> Calculate the values of counters after applying all alternating operations:increase counter by 1; set value of all counters to current maximum. 


You are given N counters, initially set to 0, and you have two possible operations on them:

- increase(X) − counter X is increased by 1,
- max counter − all counters are set to the maximum value of any counter.

A non-empty zero-indexed array A of M integers is given. This array represents consecutive operations:

- if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
- if A[K] = N + 1 then operation K is max counter.

For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.


#### 解法一：

- Detected time complexity: O(N*M)
- Test score 66%
- Correctness 100%	Performance	60% 
- 计算正确，但是时间复杂度不满足要求。

```
def solution(N, A):
    # write your code in Python 2.7
    ret = [0]*N
    #print ret

    for elem in A:
        if elem < (N + 1):
            #print elem
            #print ret
            ret[int(elem -1)] += 1
        else:
            #tmp = max(ret)
            #print "tmp",tmp
            #ret = [tmp]*N
            ret = [max(ret)]*N
            #print "ret",ret
    return ret
```



#### 解法二 
[100%] MaxCounters
>
Calculate the values of counters after applying all alternating operations: increase counter by 1; set value of all counters to current maximum.


**note:**

 - 分别记录上次update的值，在update的基础上，再记录当前最大值。
 - 有点类似操作系统的内存管理，按需分配的味道， 当出现缺页中断的时候再去分配内存。
 - 这里是当出现N+1的时候，再去update 上次没有update的元素，并且在最后一次需要再检查一次update


- Detected time complexity:
O(N + M)

```
def solution(N, A):
    # write your code in Python 2.7
    ret = [0]*N

    maxOfArray = 0
    last_update = 0
    tn = N + 1
    for elem in A:
        if elem < tn:
            if ret[elem -1] < last_update:
                ret[elem -1] = last_update
                
            ret[elem -1] += 1
            if ret[elem -1] > maxOfArray:
                maxOfArray = ret[elem -1]
        else:
            last_update = maxOfArray
            #print "last_update",last_update
            #ret = [maxOfArray]*N
            
            #print "ret",ret
    for elem in xrange(N):
        if ret[elem] < last_update:
            ret[elem] = last_update
    return ret
```

```
def solution(N, A):
    # write your code in Python 2.7
    tn = N + 1
    maxOfCounter = 0
    lastUpdate = 0
    ret = [0]*N
    for a in A:
        if a < tn:
            if ret[a-1] < lastUpdate :
                ret[a-1] = lastUpdate
            ret[a-1] += 1
            if ret[a-1] > maxOfCounter: 
                # update max counter
                maxOfCounter = ret[a-1]
        else:
            lastUpdate = maxOfCounter
    for elem in xrange(N):
        if ret[elem-1] < lastUpdate:
            ret[elem-1] = lastUpdate
    return ret
```




<h2 id = "1.5"> 
lesson 5: <i>prefix sums</i>
</h2>


<h3 id = "1.5.1"> 
1. <i> PassingCars</i>
</h3>

- [100%] 
>
Count the number of passing cars on the road.

- Detected time complexity:
O(N)

```
def solution(A):
    # write your code in Python 2.7
    total = sum(A)
    ret = 0
    for elem in A:
        if elem == 0:
            ret += total
            if ret > 1000000000:
                return -1
        else:
            total -= elem
    return ret
```


<h3 id = "1.5.2"> 
2. <i> CountDiv </i>
</h3>

> Compute number of integers divisible by k in range [a..b].

#### CountDiv solution 1
- test score 67%

```
def solution(A, B, K):
    # write your code in Python 2.7
    ret = 0
    if A%K == 0:
        ret += 1
    if A != B and B%K == 0 :
        ret += 1
        
    if (B-A)%K == 0:
        if ret == 2:
            ret += ((B-A)/K - 1)
        else:
            ret += (B-A)/K
    else:
        ret += (B-A)/K
    return ret
```

 
#### CountDiv solution 2
- Test score 100%

```
def solution(A, B, K):
    # write your code in Python 2.7
    ret = 0
    ra = -1 if A == 0 else (A - 1)/K 
    rb = B/K
    
    return rb -ra
    
```
#### solution 3
- Test score 100%

```
def solution(A, B, K):
    # write your code in Python 2.7
    c = 1 if A%K == 0 else 0
    return B/K -A/K + c
    
```

<h3 id = "1.5.3"> 
3. GenomicRangeQuery
</h3>


> Find the minimal nucleotide from a range of sequence DNA.

#### 解法一：
- Test score  37%


```
def getMinFactor(S,l,i,j):
    if j == (l-1):
        tmp = set(S[i:-1])  # error ，should be s[i:]
    else:
        tmp = set(S[i:(j+1)])
    if 'A' in tmp:
        return 1
    elif 'C' in tmp:
        return 2
    elif 'G' in tmp:
        return 3
    else:
        return 4
        
def solution(S, P, Q):
    # write your code in Python 2.7
    length = len(S)
    result = []
    for x,y in zip(P,Q):
        #print x,y
        result.append(getMinFactor(S,length,x,y))
    return result
```


#### 解法二：
- Test score 100%
> used each list to save that states whether has element or not

```
def calcPrefixSum(s,l):
    category_a, category_c, category_g = [0]*(l+1), [0]*(l+1), [0]*(l+1)
    for i in xrange(l):
        a,c,g = 0,0,0
        if s[i] == 'A':
            a = 1
        elif s[i] == 'C':
            c = 1
        elif s[i] == 'G':
            g = 1
        category_a[i+1] += category_a[i] + a
        category_c[i+1] += category_c[i] + c
        category_g[i+1] += category_g[i] + g
        
    return category_a, category_c, category_g
        
def solution(S, P, Q):
    # write your code in Python 2.7
    
    length = len(S)
    result = []
    a, c, g =  calcPrefixSum(S,length)
    for x,y in zip(P,Q):
        #print x,y
        #result.append(getMinFactor(S,length,x,y))
        if a[y+1] - a[x] > 0:
            result.append(1)
        elif c[y+1] - c[x] > 0:
            result.append(2)
        elif g[y+1] - g[x] > 0:
            result.append(3)
        else:
            result.append(4)
            
    return result
```


<h3 id = "1.5.4"> 
4. MinAvgTwoSlice
</h3>


> Find the minimal average of any slice containing at least two elements.

- Test score 100%

**note:** transfer to 2/3 


```
def solution(A):
    # write your code in Python 2.7
    length = len(A)
    minStartPos = 0
    minSum = (A[0] + A[1])/2.0
    
    for i in xrange(length - 2):
        tmp = (A[i] + A[i+1])/2.0
        if tmp < minSum:
            minSum = tmp
            minStartPos = i
        tmp = (tmp*2 + A[i+2])/3.0
        if tmp < minSum:
            minSum = tmp
            minStartPos = i
    if (A[-1] + A[-2])/2.0 < minSum:
        minStartPos = length - 2
    
    return minStartPos
```

<h2 id = "1.6"> 
lesson 6: <i>sorting</i>
</h2>


<h3 id = "1.6.1"> 
1. Distinct
</h3>


> Compute number of distinct values in an array.
- Test score 100%


```
def solution(A):
    # write your code in Python 2.7
    Aset = set(A)
    return len(Aset)
```

<h3 id = "1.6.2"> 
2. MaxProductOfThree
</h3>


> 
Maximize A[P] * A[Q] * A[R] for any triplet (P, Q, R).

#### solution 1
- O(N) 
- Test score  100% OJ test is O(N * log(N))


```
def solution(A):
    ma1, ma2, ma3 = -1000, -1000, -1000
    mi1, mi2 = 1000, 1000
    for elem in A:
        if elem > ma1:
            ma1, ma2, ma3 = elem, ma1, ma2
        elif elem > ma2:
            ma2, ma3 = elem, ma2
        elif elem > ma3:
            ma3 = elem
        
        if elem < mi1:
            mi1,mi2 = elem, mi1
        elif elem < mi2:
            mi2 = elem
    a, b = ma1*ma2*ma3, ma1*mi1*mi2
    return a if a > b else b
```

#### solution 2

**note:** 

- just need return the value of the max product,
- so, we can just consider the first or last teiplet, after sort

- Detected time complexity: O(N * log(N))

```
def solution(A):
    A.sort()
    return max(A[0]*A[1]*A[-1], A[-1]*A[-2]*A[-3])

```


<h3 id = "1.6.3"> 
3. Triangle
</h3>


> Determine whether a triangle can be built from a given set of edges.
[https://codesays.com/2014/solution-to-triangle-by-codility/](https://codesays.com/2014/solution-to-triangle-by-codility/)


```
def solution(A):
    # write your code in Python 2.7
    length = len(A)
    if length < 3:
        return 0
    A.sort()
    for idx in xrange(0,length -2):
        if A[idx]+A[idx + 1] > A[idx + 2]:
            return 1
    return 0
```




<h2 id = "1.7"> 
lesson 7: <i>stacks and queues</i>
</h2>


<h3 id = "1.7.2"> 
2. Nesting
</h3>


> Determine whether given string of parentheses is properly nested.

- Test score 100%

```
def solution(S):
    # write your code in Python 2.7
    tmp = 0
    for elem in S:
        if elem == "(":
            tmp += 1
        elif elem == ")":
            tmp -= 1
            if tmp < 0:
                return 0
    if tmp == 0:
        return 1
    else:
        return 0
```

<h3 id = "1.7.4"> 
4. StoneWall
</h3>

> Cover "Manhattan skyline" using the minimum number of rectangles.

- Test score 100%

```
def solution(H):
    # write your code in Python 2.7
    cnt = 0
    stack = []
    for elem in H:
        while len(stack)!= 0 and stack[-1] > elem:
            stack.pop()
        
        if len(stack) != 0 and stack[-1] == elem:
            pass
        else:
            stack.append(elem)
            cnt += 1
    return cnt

```



