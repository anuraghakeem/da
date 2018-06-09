print("enter the three elements ")
l=[]
for i in range(3):
    x=input()
    l.append(x)
print("the list is ")
print(l)
print("the list after left rotate is ")
l.append(l[0])
del(l[0])
print(l)


=======================================
def stats(file):
    f=open(file,"r")
    linen=0
    wordn=0
    charn=0
    for i in f.readlines():
        print(i)
        linen+=1
        r=i.split()
        for j in r:
            wordn+=1
            charn+=len(j)
    print("line count : %d" %linen)
    print("word count:  %d" %wordn)
    print("charcter count : %d" %charn)
f=open("new.txt","w")
i=int(input("enter the number of lines"))
for i in range(i):
    s=input("enter the line")
    f.write(s+"\n")
    #f.write("\n")
f.close()
stats("new.txt")
