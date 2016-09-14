
print "\n ===sort learning!=== \n"

# some tools
def myLess(a, b):
    return a < b

def myExch(a,b):
    a,b = b,a

def isSort(a):
    length = len(a)
    for i in xrange(length):
        if a[i] > a[i+1]:
            return False
        return True


def selectionSort(a):
    length = len(a)
    for i in xrange(length):
        mintmp = i
        for j in xrange(i + 1, length):
            if a[j] < a[mintmp]:
                mintmp = j
        a[i], a[mintmp] = a[mintmp], a[i]

def insertionSort(a):
    length = len(a)
    for i in xrange(1, length):
        for j in xrange(i, 0, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]




# this fun will been in infinte loop, when partition num is the max or min num
# e.g. a = [1,2,3,4,5,1,2,3,4,5]
def quick_sort(a, low, high):
    l,h = low, high
    if l >= h:
        return a
    k = a[l]
    while l < h :
        while l < h and k < a[h]: # avoid index out l<h
             h -= 1
        a[l] = a[h]
        while l < h and k > a[l]:
            l += 1
        a[h] = a[l]
    a[l] = k
    quick_sort(a,low, l-1)
    quick_sort(a, h+1, high)
    return a

# -----
def quick_sort_2(a, low, high):
    l,h = low, high
    if l >= h:
        print "test"
        return a
    k = a[l]
    while l < h :
        while l < h and k <= a[h]: # avoid index out l<h
             h -= 1
        a[l] = a[h]
        while l < h and k > a[l]:
            l += 1
        a[h] = a[l]
        print l,h,k
    a[l] = k
    quick_sort_2(a,low, l-1)
    quick_sort_2(a, h+1, high)
    return a

#-------------------------------
def quick_sort_3way(a, low, high):
    l,h = low, high
    if l >= h:
        print "test"
        return a
    k = a[l]
    while l < h :
        while l < h and k <= a[h]: # avoid index out l<h
             h -= 1
        a[l] = a[h]
        while l < h and k > a[l]:
            l += 1
        a[h] = a[l]
        print l,h,k
    a[l] = k
    quick_sort_3way(a,low, l-1)
    quick_sort_3way(a, h+1, high)
    return a

def bubble_sort(L):
    l = len(L)
    for idx in xrange(l):
        for idy in xrange(l-idx-1):
            if  L[idy] > L[idy + 1]:
                L[idy], L[idy + 1] = L[idy+ 1], L[idy]
    return L


if __name__ == "__main__":
    import random
    arr = [random.randint(1,100) for i in xrange(10)]
    print "before sort:", arr
    quick_sort(arr,0,len(arr)-1)

    #selectionSort(arr)
    #insertionSort(arr)
    assert isSort(arr),"sort check crashed!\n"
    print "After sort:"
    print arr




