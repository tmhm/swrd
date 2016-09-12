


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

#-------------------------------

def quick_sort_2(a, low, high):
    l,h = low, high
    if l >= h:
        print "test"
        return a
    k = a[l]
    while l < h :
        while l < h and k < a[h]: # avoid index out l<h
             h -= 1
        a[l] = a[h]
        while l < h and k > a[l]:
            l += 1
        a[h] = a[l]
        print l,h,k
    a[l] = k
    quick_sort(a,low, l-1)
    quick_sort(a, h+1, high)
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
    print "After sort:"
    print arr



