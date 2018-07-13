l=[]
r=1
while(r==1):
    x=input()
    if(x!="quit"):
        l.append(x)
    else:
        break
print(l)
for i in range(len(l)-1,-1,-1):
    print(l[i])
    ========================================
class invalid_radius(Exception):
    def __int__(self,s):
        self.s=s
        self.random=1000
def find_area(r):
    if r<0:
        raise invalid_radius("negative radius is invalid")
    else:
        print("the area is ")
        a=3.14*r**2
        print("the area is %f" %(a))
try:
    r=int(input("enter a radius"))
    find_area(r)
except invalid_radius as obj:
    print(obj)    
