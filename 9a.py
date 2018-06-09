def bubble_sort(*a):
    a=list(a)
    print(a)

    for i in range(len(a)):
        for j in range(1,len(a)-i):
            if a[j-1]>a[j]:
                a[j-1],a[j]=a[j],a[j-1]
    print("the list is ")
    print(a)
bubble_sort(10,9,8,7,6,5,4,3,2,1)
================================================
class student:
    student_count=0
    def __init__(self,n,u,sub):
        self.name=n
        self.usn=u
        self.sub=sub
        student.student_count+=1
    def display(self):
        print("the name is %s usn is %s" %(self.name,self.usn))

stud=[]
r=1
while r==1:
    x=int(input("enetr the operation to be performed \n 1. enter a student \n 2. show students who have taken python \n 3. display student count \n"))
    if x==1:
        l=[]
        n=input("enter the student name ")
        u=input("enter the student usn ")
        n=int(input("enter the number of sujects that student takes"))
        for i in range(n):
            z=input("enter the subject ")
            l.append(z)
        stud.append(student(n,u,l))
    elif x==2:
        for i in stud:
            if "python" in i.sub:
                i.display()
    elif x==3:
        print("the total number of students in the class is ")
        print(student.student_count)
    else:
        r=0
