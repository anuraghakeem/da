s=input("enter a string")
a=0
e=0
i=0
o=0
u=0
s=s.lower()
for j in s:
    if j=='a':
        a+=1
    elif j=='e':
        e+=1
    elif j=='i':
        i+=1
    elif j=='o':
        o+=1
    elif j=='u':
        u=+1
print("the count of the vowels are \n a: %d \n e: %d \n i: %d \n o: %d \n u: %d \n" %(a,e,i,o,u))
====================================================================================================
class Triangle:
    n=3
    def __init__(self,a1,a2,a3):
        self.a1=a1
        self.a2=a2
        self.a3=a3
    def check_triangle(self):
        s=self.a1+self.a2+self.a3
        if s==180:
            return "true"
        else:
            return "false"
my_triangle=Triangle(60,60,60)
print(my_triangle.check_triangle())
