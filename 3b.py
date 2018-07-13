dict={}
def put_mobile():
    x=input("enter the phone name")
    y=input("enter the price of the phone")
    dict[x]=y
def find_mobile():
    x=input("enter the phone to be searched")
    if(x in dict.keys()):
        print("the price of the phone is %d" %(int(dict[x])))
    else:
        print("do you want to put that phone")
        y=input("enter yes or no")
        if(y=="yes"):
            put_mobile()
def same_price():
    x=input("enter the price of the phone")
    for i in dict.keys():
        if x==dict[i]:
            print(i)
def remove_phone():
    x=input("enter the phone name")
    del dict[x]
def sort_phone():
    l=sorted(dict,key=dict.get)
    print("the sorted dictony is ")
    print(l)

i=1
while(i==1):
    print("enter the operation to be performed \n 1.input \n 2. find \n 3. same price \n 4. remove \n 5. sort phones \n 6.exit \n")
    x=int(input("enter the input"))
    if(x==1):
        put_mobile()
    elif(x==2):
        find_mobile()
    elif(x==3):
        same_price()
    elif(x==4):
        remove_phone()
    elif(x==5):
        sort_phone()
    else:
        i=0

============================================================
class Account:
    def __init__(self,b,i,an):
        self.b=int(b)
        self.i=int(i)
        self.an=int(an)
        self.fees=0
    def withdraw(self):
        x=int(input("enter the amount to be withdrawn"))
        if self.b>x:
            print("yes your amount will be withdrawn")
            print("the amount withdrawn is %d" %(x))
            self.b-=x
        else:
            self.fees+=100
            self.b-=x
            self.b-=self.fees
            print("the thing was overdrawn the amount to be paid is %d" %(-1*self.b))

    def desposit(self):
        x=int(input("enter the amount to be deposited "))
        self.b+=x
    def intrest(self):
        x=int(input("give the intrest rate"))
        r=self.b*(x/100.0)
        print("the intrest is %d " %r)
obj=Account(10000,1,1234)
r=1
while(r==1):
    print("enter the operation to be performed 1. deposit 2. withdraw 3. intrest 4. exit")
    x=int(input())
    if x==1:
        obj.desposit()
    elif x==2:
        obj.withdraw()
    elif x==3:
        obj.intrest()
    elif x==4:
        r=0
