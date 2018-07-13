class invalid_input(Exception):
    def __init__(self,s):
        self.s=s
class not_elegible(Exception):
    def __init__(self,s):
        self.s=s
try:
    l=[]
    print("enter the marks in three subjects ")
    for i in range(3):
        x=int(input("enter the marks "))
        if x>0:
            l.append(x)
        else:
            raise invalid_input("the entered marks is negative")
    for i in l:
        if i<20:
            raise not_elegible("you are not elegible to wite the exam")
except invalid_input as arg:
    print(arg)
except not_elegible as arg:
    print(arg)
else:
    print("every thing is fine you are elegible to write the exam")
    =====================================================================
    
