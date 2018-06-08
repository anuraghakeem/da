import random
b=int(input('enter the range'))
a=[random.randint(0,100) for i in range(b)]
print(a)
for i in range(len(a)):
    r=a[i]
    j=i-1
    while(j>=0 and a[j]>r):
        a[j+1]=a[j]
        j=j-1
        a[j+1]=r
print(a)
