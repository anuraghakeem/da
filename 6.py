import random
cnt=0
n=int(input("Enter a range of numbers: "))
a=[random.randint(0,100) for i in range(n)]
def merge(a,b):
    i,j,c=0,0,[]
    while((i<len(a)) and (j<len(b))):
        if (a[i]<b[j]):
            c.append(a[i])
            i=i+1
        else:
            c.append(b[j])
            j=j+1
            global cnt
            cnt=cnt+(len(a)-i)
    while(i<len(a)):
        c.append(a[i])
        i=i+1
    while(j<len(b)):
        c.append(b[j])
        j=j+1
    return c
def count_invert(a):
    if(len(a)>1):
        a1=count_invert(a[0:len(a)//2])
        b1=count_invert(a[len(a)//2:])
        a=merge(a1,b1)
    return a
print(a)
print(count_invert(a))
print(cnt)
