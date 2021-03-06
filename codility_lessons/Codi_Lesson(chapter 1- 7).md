
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
	* [2. Triangle](#1.6.2)
	* [2. MaxProductOfThree](#1.6.3)
	* [4. NumberOfDiscIntersections](#1.6.4)



* [lesson 7: *stacks and queues*](#1.7)
	* [1. Nesting](#1.7.1)
	* [2. StoneWall](#1.7.2)
	* [3. Brackets](#1.7.3)
	* [4. Finsh](#1.7.4)



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


>
Count the number of passing cars on the road.

A non-empty zero-indexed array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

0 represents a car traveling east,
1 represents a car traveling west.
The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:

	  A[0] = 0
	  A[1] = 1
	  A[2] = 0
	  A[3] = 1
	  A[4] = 1
  
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

**Assume that:**

- N is an integer within the range [1..100,000];
- each element of array A is an integer that can have one of the following values: 0, 1.

**Complexity:**

- expected worst-case time complexity is O(N);
- expected worst-case space complexity is O(1), 

思路：

- 可以计算suffix sum的方式
- 然后，从前面开始遍历list，遇到a ＝ 0，result即加上当前的suffix sum的值
- 此题元素是0，1，故可以不用保留每一步的计算，题目有要求限制O(1)的space， 也是给出提示，用一个变量retsum值来记录，每一步的prefix sum值，每移动一步，元素是1的话，将retsum 减1， 即是下一个prefix sum 值。

- Detected time complexity: O(N)
- [100%] 

```
def solution(A):
    # write your code in Python 2.7
    result = 0
    retsum = sum(A)
    for a in A:
        if a == 0:
            result += retsum
            if result > 1000000000:
                return -1
        else:
            retsum -= 1
    return result
```



<h3 id = "1.5.2"> 
2. <i> CountDiv </i>
</h3>

> Compute number of integers divisible by k in range [a..b].


given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Assume that:

- A and B are integers within the range [0..2,000,000,000];
- K is an integer within the range [1..2,000,000,000];
A ≤ B.

**Complexity:**

- expected worst-case time complexity is O(1);
- expected worst-case space complexity is O(1).

 
#### CountDiv solution 1
- Test score 100%

```
def solution(A, B, K):
    # write your code in Python 2.7
    ra = -1 if A == 0 else (A - 1)/K 
    rb = B/K
    
    return rb -ra
    
```
#### solution 2
- Test score 100%

```
def solution(A, B, K):
    # write your code in Python 2.7
    c = 1 if A%K == 0 else 0
    return B/K -A/K + c
    
```

```
def solution(A, B, K):
    # write your code in Python 2.7
    return (B/K - A/K) if (A%K != 0 ) else (B/K - A/K + 1)
```


<h3 id = "1.5.3"> 
3. GenomicRangeQuery
</h3>


> Find the minimal nucleotide from a range of sequence DNA.

A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the types of successive nucleotides in the sequence. Each nucleotide has an impact factor, which is an integer. Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going to answer several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K]\(inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
The answers to these M = 3 queries are as follows:

- The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
- The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
- The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact factor is 1, so the answer is 1.

the function should return the values [2, 4, 1], as explained above.

Assume that:

- N is an integer within the range [1..100,000];
- M is an integer within the range [1..50,000];
- each element of arrays P, Q is an integer within the range [0..N − 1];
- P[K] ≤ Q[K], where 0 ≤ K < M;
- string S consists only of upper-case English letters A, C, G, T.

Complexity:

- expected worst-case time complexity is O(N+M);
- expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).


#### 解法一：
- Test score  62%
- Detected time complexity:
O(N * M)
- 最初的想法是：根据给出的范围，用set保存，看是否有各元素
- 时间复杂度，明显达不到O(N+M)


```
def getMinFactor(S,l,i,j):
    if j == (l-1):
        tmp = set(S[i:])  #
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
- used each list to save that states whether has element or not
- 在用prefix sum 做差的方式，依次检查是否存在A,C,G,T字符
- 注意数值关系


```
def calcPrefixSum(S):
    l = len(S)+1
    pa,pc,pg = [0]*l,[0]*l,[0]*l
    for idx,elem in enumerate(S):
        a,c,g = 0,0,0
        if elem == 'A':
            a = 1
        elif elem == 'C':
            c = 1
        elif elem == 'G':
            g = 1
        pa[idx+1] = pa[idx] + a
        pc[idx+1] = pc[idx] + c
        pg[idx+1] = pg[idx] + g
    return pa,pc,pg

def solution(S, P, Q):
    # write your code in Python 2.7
    pA,pC,pG = calcPrefixSum(S)
    result = []
    for i,j in zip(P,Q):
        if pA[j+1] - pA[i] > 0:
            ret = 1
        elif pC[j+1] - pC[i] > 0:
            ret = 2
        elif pG[j+1] - pG[i] > 0:
            ret = 3
        else:
            ret = 4
        result.append(ret)
    return result
    
```

```
根据prefix sum list:
pA = [0, 0, 1, 1, 1, 1, 1, 2]
pC = [0, 1, 1, 1, 2, 3, 3, 3]
pG = [0, 0, 0, 1, 1, 1, 1, 1]

故，是下标［j＋1］－［i］
```


<h3 id = "1.5.4"> 
4. MinAvgTwoSlice
</h3>


> Find the minimal average of any slice containing at least two elements.

A non-empty zero-indexed array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
contains the following example slices:

- slice (1, 2), whose average is (2 + 2) / 2 = 2;
- slice (3, 4), whose average is (5 + 1) / 2 = 3;
- slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.

The goal is to find the starting position of a slice whose average is minimal.

Complexity:

- expected worst-case time complexity is O(N);
- expected worst-case space complexity is O(N), 

#### sloution
- Test score 100%

**note:** transfer to 2/3 ,
- 只要查看相邻两个和三个的数的平均值即可
- [proof](https://github.com/daotranminh/playground/blob/master/src/codibility/MinAvgTwoSlice/proof.pdf)


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




### exercise

**Problem:**
 
You are given a zero-indexed array A consisting of n > 0 integers; you must return the number of unique values in array A.


**Solution O(nlogn):**
 
 
First, sort array A; similar values will then be next to each other. Finally, just count the number of distinct pairs in adjacent cells.```The number of distinct values — O(nlogn).def distinct(A):	n = len(A)	A.sort()	result = 1	for k in xrange(1, n):		if A[k] != A[k - 1]: result += 1	return result
```
	> The time complexity is O(n log n), in view of the sorting time.




<h3 id = "1.6.1"> 
1. Distinct
</h3>



> Compute number of distinct values in an array.


- 将list保存为set 即可
- Test score 100%
- 也可以排序，然后对不同数进行计数，如exercise那样


```
def solution(A):
    # write your code in Python 2.7
    Aset = set(A)
    return len(Aset)
```


<h3 id = "1.6.2"> 
2. Triangle
</h3>


> Determine whether a triangle can be built from a given set of edges.
[https://codesays.com/2014/solution-to-triangle-by-codility/](https://codesays.com/2014/solution-to-triangle-by-codility/)
>
>On one hand, there is no false triangular. Since the array is sorted, we already know A[index] < = A[index+1] <= A[index+2], and all values are positive. A[index] <= A[index+2], so it must be true that A[index] < A[index+1] + A[index+2]. Similarly, A[index+1] < A[index] + A[index+2]. Finally, we ONLY need to check **A[index]+A[index+1] > A[index+2]** to confirm the existence of triangular.

> On the other hand, there is no underreporting triangular. If the inequality can hold for three out-of-order elements, to say, A[index]+A[index+m] > A[index+n], where n>m>1. Again, because the array is sorted, we must have A[index] < = A[index+m-1] and A[index+m+1] <= A[index + n]. So A[index+m-1] +A[index+m] >= A[index]+A[index+m] > A[index+n] >= A[index+m+1]. After simplification, A[index+m-1] +A[index+m] > A[index+m+1]. In other words, if we have any inequality holding for out-of-order elements, we MUST have AT LEAST an inequality holding for three consecutive elements.
> 



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



<h3 id = "1.6.3"> 
3. MaxProductOfThree
</h3>




> 
Maximize A[P] * A[Q] * A[R] for any triplet (P, Q, R).

#### solution 1
- O(N) 
- Test score  100% OJ test is O(N * log(N))
- 考虑到有负数存在， 故乘积最大的三个数，会出现在两种情况：
	- 三个数均是正数，且是三个最大的数
	- 两个负数和一个正数，最大正数和最小的两个负数


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
- 基于解法一，我们可以先排序，然后直接取，不需要每个比较，相对来说，时间成本稍大
- so, we can just consider the first or last teiplet, after sort

- Detected time complexity: O(N * log(N))

```
def solution(A):
    A.sort()
    return max(A[0]*A[1]*A[-1], A[-1]*A[-2]*A[-3])

```

<h3 id = "1.6.4"> 
4. NumberOfDiscIntersections
</h3>

>We draw N discs on a plane. The discs are numbered from 0 to N − 1. A zero-indexed array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

>We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

>The figure below shows discs drawn for N = 6 and A as follows:


	  A[0] = 1
	  A[1] = 5
	  A[2] = 2
	  A[3] = 1
	  A[4] = 4
	  A[5] = 0
	  
![](https://codility-frontend-prod.s3.amazonaws.com/media/task_img/number_of_disc_intersections/media/auto/mpaecfada7c1e52a7b01b04916c859b15d.png)


>
>There are eleven (unordered) pairs of discs that intersect, namely:

- discs 1 and 4 intersect, and both intersect with all the other discs;
- disc 2 also intersects with discs 0 and 3.

**problem:**
>
Compute the number of intersections in a sequence of discs.
>
given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

**Assume that:**

- N is an integer within the range [0..100,000];
- each element of array A is an integer within the range [0..2,147,483,647].

**Complexity:**

- expected worst-case time complexity is O(N*log(N));
- expected worst-case space complexity is O(N).

**思路：**



- [参考csdn](http://blog.csdn.net/dear0607/article/details/42671621)
- [stackoverflow](http://stackoverflow.com/questions/4801242/algorithm-to-calculate-number-of-intersecting-discs#)
	
	>initially we calculate all start and end points of discs. After go by all line and check count of discs inside current point. If in current point started some discs and intersection count increased by: already active distsc multiplied by count of started in current point (result += t * dps[i]) and count of intersections of started(result += dps[i] * (dps[i] - 1) / 2) eg. if started 5 discs in one of point it will increased by(1+2+3+4+5 intersections, or 5*(5-1) / 2[sum formula]).
- [cnblog](http://www.cnblogs.com/wei-li/p/Numberofdiscintersections.html)
	 
	 
	 
- 构造成区间，[i-A[i],i+A[i]]
	- e.g. A ＝ ［1，5，2，1，4，0］
	- => [－1,1],[-4,6],[0,4],[2,4],[0,8],[5,5]
- 因为我们圆的中心位置在［0，len(A)],e.g. 在上例中 [0,5], 所以起点数组dps计算［0，i-A[i]］的范围，故有max(0,i-A[i])
- 终点数组不要超过每个圆心的最大值，即小于len（A）－1， 故有min（length－1，i+A［i］）


	


#### sloution:[100%]
```
def solution(A):
    result = 0
    length = len(A)
    dps = [0]*length
    dpe = [0]*length
    for i in xrange(length):
        dps[max(0, i-A[i])] += 1
        dpe[min(length-1, i+A[i])] += 1
    tmp = 0
    for i in xrange(length):
        if dps[i] > 0:
            result += tmp*dps[i]
            result += dps[i] * (dps[i] - 1)/2
            if result > 10000000:
                return -1
            tmp += dps[i]
        tmp -= dpe[i]
    return result
```



<h2 id = "1.7"> 
lesson 7: <i>stacks and queues</i>
</h2>


<h3 id = "1.7.1"> 
1. Nesting
</h3>


> Determine whether given string of parentheses is properly nested.

A string S consisting of N characters is called properly nested if:

- S is empty;
- S has the form "(U)" where U is a properly nested string;
- S has the form "VW" where V and W are properly nested strings.

For example, string "(()(())())" is properly nested but string "())" isn't.

**Assume that:**

- N is an integer within the range [0..1,000,000];
- string S consists only of the characters "(" and/or ")".

**Complexity:**

- expected worst-case time complexity is O(N);
- expected worst-case space complexity is O(1) (not counting the storage required for input arguments).

**solution:**

- Test score 100%
- used stack
- must have "(" before ")"

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






<h3 id = "1.7.2"> 
2. StoneWall
</h3>

You are going to build a stone wall. The wall should be straight and N meters long, and its thickness should be constant; however, it should have different heights in different places. The height of the wall is specified by a zero-indexed array H of N positive integers. H[I] is the height of the wall from I to I+1 meters to the right of its left end. In particular, H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.

The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular). Your task is to compute the minimum number of blocks needed to build the wall.

For example, given array H containing N = 9 integers:
	
	  H[0] = 8    H[1] = 8    H[2] = 5
	  H[3] = 7    H[4] = 9    H[5] = 8
	  H[6] = 7    H[7] = 4    H[8] = 8
the function should return 7. The figure shows one possible arrangement of seven blocks.

![](https://codility-frontend-prod.s3.amazonaws.com/media/task_img/stone_wall/media/auto/mp2e167f4181a5967a0844fbd70a3a5bfb.png)


**Assume that:**

- N is an integer within the range [1..100,000];
- each element of array H is an integer within the range [1..1,000,000,000].



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

<h3 id = "1.7.3"> 
3. Brackets

</h3>

> Determine whether a given string of parentheses is properly nested.


**Task description**

A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

- S is empty;
- S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
- S has the form "VW" where V and W are properly nested strings.

For example, the string "{[()()]}" is properly nested but "([)()]" is not.


For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

**Assume that:**

- N is an integer within the range [0..200,000];
- string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".

**Complexity:**

- expected worst-case time complexity is O(N);
- expected worst-case space complexity is O(N) (not counting the storage required for input arguments).

用一个stack，当栈头和新来的元素配对，即弹出，否则压栈。
注意：list为空的时候， 还有多个空值的list。

**solution：**

```
def check(t,s):
    if len(t) < 1:
        return 0
    if s == ')' and t[-1] == '(':
        return 1
    elif s == ']' and t[-1] == '[':
        return 1
    elif s == '}' and t[-1] == '{':
        return 1
    else:
        return 0
        

def solution(S):
    tmp = []
    for elem in S:
        if elem == ' ':
            continue
        if check(tmp, elem):
            tmp.pop()
        else:
            tmp.append(elem)
            #print "append: %s, len: %s" %(elem,len(tmp))
            
    if len(tmp) < 1:
        return 1
    else:
        return 0
```







<h3 id = "1.7.4"> 

4. Fish

</h3>

Given two non-empty zero-indexed arrays A and B consisting of N integers. Arrays A and B represent N voracious fish in a river, ordered downstream along the flow of the river.

The fish are numbered from 0 to N ? 1. If P and Q are two fish and P < Q, then fish P is initially upstream of fish Q. Initially, each fish has a unique position.

Fish number P is represented by A[P] and B[P]. Array A contains the sizes of the fish. All its elements are unique. Array B contains the directions of the fish. It contains only 0s and/or 1s, where:

- 0 represents a fish flowing upstream,
- 1 represents a fish flowing downstream.

If two fish move in opposite directions and there are no other (living) fish between them, they will eventually meet each other. Then only one fish can stay alive ? the larger fish eats the smaller one. More precisely, we say that two fish P and Q meet each other when P < Q, B[P] = 1 and B[Q] = 0, and there are no living fish between them. After they meet:

- If A[P] > A[Q] then P eats Q, and P will still be flowing downstream,
- If A[Q] > A[P] then Q eats P, and Q will still be flowing upstream.

We assume that all the fish are flowing at the same speed. That is, fish moving in the same direction never meet. The goal is to calculate the number of fish that will stay alive.

For example, consider arrays A and B such that:

	  A[0] = 4    B[0] = 0
	  A[1] = 3    B[1] = 1
	  A[2] = 2    B[2] = 0
	  A[3] = 1    B[3] = 0
	  A[4] = 5    B[4] = 0

Initially all the fish are alive and all except fish number 1 are moving upstream. Fish number 1 meets fish number 2 and eats it, then it meets fish number 3 and eats it too. Finally, it meets fish number 4 and is eaten by it. The remaining two fish, number 0 and 4, never meet and therefore stay alive.


For example, given the arrays shown above, the function should return 2, as explained above.

**Assume that:**

- N is an integer within the range [1..100,000];
- each element of array A is an integer within the range [0..1,000,000,000];
- each element of array B is an integer that can have one of the following values: 0, 1;
- the elements of A are all distinct.

**Complexity:**

- expected worst-case time complexity is O(N);
- expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).


考虑到所有鱼的速度一致，那么从上游开始check，
前面的鱼如果是往上游走的话，即永远不会被吃或者吃其他鱼,

```
def solution(A, B):
    # write your code in Python 2.7
    # record the num of fish with downstream 
    lastFishDir = 0
    stackTmp = []
    
    # check fish from upstream 
    for fish, curDir in zip(A,B):
        if lastFishDir < 1:
            stackTmp.append(fish)
            #lastFishDir += curDir
        else:
            if curDir == 0:
                while lastFishDir > 0 and fish > stackTmp[-1]:
                    stackTmp.pop()
                    lastFishDir -= 1
                if len(stackTmp) > 0 and fish < stackTmp[-1]:
                    continue
                stackTmp.append(fish)
            else:
                stackTmp.append(fish)
                
        lastFishDir += curDir
    return len(stackTmp)
```


思考方式很重要：

由于，上游的鱼如果是往上游走的话，即永远不会被吃或者吃其他鱼,
如果把这样的鱼也放在stack里面，每次fight之后，不太好处理，
故我们可以把一定可以存活的鱼直接计数， 将需要fight的鱼放在stack里面

- [100%]

```
def solution(A, B):
    lastFishDir = 0  # record the num of fish with downstream 
    stackDown = []
    aliveCnt = 0
    
    # check fish from upstream 
    for fish, curDir in zip(A,B):
        if curDir == 1:
            # only the downstream fish need fight,
            stackDown.append(fish)
        else:
            while lastFishDir > 0 :
                if fish > stackDown[-1]:
                    stackDown.pop()
                    lastFishDir -= 1
                else:
                    break
            else:
                aliveCnt += 1
            
        lastFishDir += curDir

    return len(stackDown)+aliveCnt
```

该博主分析的很详细，[https://codesays.com/2014/solution-to-fish-by-codility/](https://codesays.com/2014/solution-to-fish-by-codility/)
>
```
def solution(A, B):
    alive_count = 0        # The number of fish that will stay alive
    downstream = []        # To record the fishs flowing downstream
    downstream_count = 0   # To record the number of elements in downstream

    for index in xrange(len(A)):
        # Compute for each fish
        if B[index] == 1:
            # This fish is flowing downstream. It would
            # NEVER meet the previous fishs. But possibly
            # it has to fight with the downstream fishs.
            downstream.append(A[index])
            downstream_count += 1
        else:
            # This fish is flowing upstream. It would either
            #    eat ALL the previous downstream-flow fishs,
            #    and stay alive.
            # OR
            #    be eaten by ONE of the previous downstream-
            #    flow fishs, which is bigger, and died.
            while downstream_count != 0:
                # It has to fight with each previous living
                # fish, with nearest first.
                if downstream[-1] < A[index]:
                    # Win and to continue the next fight
                    downstream_count -= 1
                    downstream.pop()
                else:
                    # Lose and die
                    break
            else:
                # This upstream-flow fish eat all the previous
                # downstream-flow fishs. Win and stay alive.
                alive_count += 1

    # Currently, all the downstream-flow fishs in stack
    # downstream will not meet with any fish. They will
    # stay alive.
    alive_count += len(downstream)

    return alive_count
```



