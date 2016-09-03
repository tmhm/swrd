def quick_sort(a, low, high):
    l,h = low, high
    if l >= h:
        return a
    k = a[l]
    while l < h :
        while l < h and k < a[h]:
             h -= 1
        a[l] = a[h]
        while l < h and k > a[l]:
            l += 1
        a[h] = a[l]
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

