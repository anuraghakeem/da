dict={}
def insert():
    w=input("enter the word : ")
    m=input("enter the words meaning : ")
    dict[w]=m
def find_word():
    w=input("enter the word : ")
    if w in dict.keys():
        print(dict[w])
    else:
        print("the word not found ")
def find_same():
    m=input("enter the meaning ")
    for k,v in dict.items():
        if m==v:
            print(k)
def remove_word():
    w=input("enter the word")
    del dict[w]
def sort_dict():
    l=list(dict.keys())
    l.sort()
    for i in l:
        print("%s:%s" %(i,dict[i]))
r=1
while(r==1):
    x=int(input("enter the operation to be performed \n 1. insert \n 2. find word \n 3. find same \n 4. remove \n 5. sort_dict \n"))
    if x==1:
        insert()
    elif x==2:
        find_word()
    elif x==3:
        find_same()
    elif x==4:
        remove_word()
    elif x==5:
        sort_dict()
    else:
        r=0
================================
def subset(a,s):
    for i in range(0,len(a)):
        left=i+1
        right=len(a)-1
        while(right>left):
            #print("the values are %d %d %d" %(a[i],a[left],a[right]))
            if a[i]+a[left]+a[right]-s==0:
                print("the final set is %d %d %d " %(a[i],a[left],a[right]))
                return 1
            elif a[i]+a[left]+a[right]-s>0:
                right-=1
            else:
                left+=1
    return -1
l=[]
n=int(input("enter the number of elements in the set"))
for i in range(n):
    r=int(input("enter the element "))
    l.append(r)
s=int(input("enter the sum "))
l.sort()
if(subset(l,s)==1):
    print("TRUE")
else:
    print("FALSE")
