
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




if __name__ == "__main__":
    L = [i for i in xrange(20,-1,-1)]
    print "Before sort:"
    print "L = ",L

#    selectionSort(L)
    insertionSort(L)
    assert isSort(L),"sort check crashed!\n"
    print "After sort:"
    print "L = ",L







