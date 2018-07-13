def spl(l):
    t1=[]
    t2=[]
    for i in l:
        if i[0]>='A' and i[0]<='M':
            t1.append(i)
        else:
            t2.append(i)
    print(t1)
    print(t2)
l=[]
n=int(input("enter the number of players"))
for i in range(n):
    x=input("enter the name")
    l.append(x)
l=list(map(lambda x:x.capitalize(),l))
spl(l)
