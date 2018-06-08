import random
import time
def partion(a,first,last):
    pivot=a[first]
    left=first+1
    right=last
    while True:
        while (left<=right and a[left]<=pivot):
            left=left+1
        while (right>=left and a[right]>=pivot):
            right=right-1
        if right<left:
            break
        else:
            temp=a[left]
            a[left]=a[right]
            a[right]=temp
    temp=a[first]
    a[first]=a[right]
    a[right]=temp
    return right
def quicksort(a,first,last):
    if first<last:
        midpoint=partion(a,first,last)
        quicksort(a,first,midpoint-1)
        quicksort(a,midpoint+1,last)
a=[random.randint(0,100) for i in range(int(input("Enter a range: ")))]
print(a)
start=time.clock()
quicksort(a,0,len(a)-1)
print(a)
print(time.clock()-start)
