class vehicle:
    def __init__(self,wheel):
        self.wheel=wheel
        print("it comes to the main class")
    def display(self):
        print(self.wheel)
class bike(vehicle):
    def __init__(self):
        print("the bike init is called")
        super().__init__(2)
class car(vehicle):
    def __init__(self):
        print("the car init is called")
        super().__init__(4)
class pedal(bike):
    def __init__(self):
        print("the pedal init is called")
        super().__init__()
class motor(bike):
    def __init__(self):
        print("the motor init is called")
        super().__init__()
obj=pedal()
obj.display()
=========================================================================
def censor(file):
    f=open(file,"r")
    f1=open("censor.txt","w")
    for i in f.readlines():
        r=i.split()
        for j in r:
            if len(j)==4:
                f1.write("xxxx"+" ")
            else:
                f1.write(j+" ")
        f1.write("\n")
f=open("new.txt","w")
i=int(input("enter the number of lines"))
for i in range(i):
    s=input("enter the line")
    f.write(s+"\n")
    #f.write("\n")
f.close()
censor("new.txt")

