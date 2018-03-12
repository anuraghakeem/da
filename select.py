import random
def selectionSort(a):
   for i in range(len(a)-1,0,-1):
       posi_Max=0
       for location in range(1,i+1):
           if a[location]>a[posi_Max]:
               posi_Max = location
       temp = a[i]
       a[i] = a[posi_Max]
       a[posi_Max] = temp
n=int(input("lenght of list"))
c = [random.randint(0,100) for i in range(n)]
print(c)
selectionSort(c)
print(c)