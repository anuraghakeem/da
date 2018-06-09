count=0
def is_abecedarian(s):
    global count
    for i in range(1,len(s)):
        if s[i-1]>s[i]:
            return False
    count+=1
    return True
x=int(input("enter the number of words to be checked"))
for i in range(x):
    w=input("enter the words")
    is_abecedarian(w)
print("the total number of words is %d" %(count))
===========================================================
class full_exception(Exception):
    def __init__(self,s):
        self.s=s
class empty_exception(Exception):
    def __init__(self,s):
        self.s=s
class queue:
    def __init__(self,max):
        self.max=max
        self.q=[]
    def insert(self):
        try:
            if len(self.q)>self.max:
                raise full_exception("the queue is full ")
            else:
                x=int(input("enter the element that has to be entered into the queue"))
                (self.q).append(x)
        except full_exception as arg:
            print(arg)
            return
    def delete(self):
        try:
            if len(self.q)<=0:
                raise empty_exception("the queue is empty")
            else:
                x=self.q[0]
                print("the element that is popped is %d" %x)
                del(self.q[0])
        except empty_exception as arg:
            print(arg)
            return
    def display(self):
        print("the queue is ")
        print(self.q)
i=1
obj=queue(5)
while(i==1):
    x=int(input("enter the operation to be performed \n 1. input \n 2. remove \n 3. display \n"))
    if x==1:
        obj.insert()
    elif x==2:
        obj.delete()
    elif x==3:
        obj.display()
    else:
        i=0
