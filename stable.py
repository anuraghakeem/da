def input_men_or_women(n,z):
    g={}
    for i in range(n):
        print("enter the prefernce of ",z," for",i+1,end=":")
        g[i+1]=list(map(int,input().split()))
        if (len(g[i+1])>n):
            print("error:wrong input")
            exit()
        a=list(map(lambda x:x>n,g[i+1]))
        if True in a:
            print("error:out of range")
            exit()
    return g
def priority(men1,women1,men2,women2):
    if(women2[women1].index(men1)<women2[women1].index(men2)):
        return True
    else:
        return False
def gale_shapley(men,women,n):
    paired_men={}
    paired_women={}
    while(len(paired_men)!=n):
        for i in men:
            if i not in paired_men:
                for j in men[i]:
                    if j not in paired_women:
                        paired_men[i]=j
                        paired_women[j]=i
                        break
                    else:
                        if(priority(i,j,paired_women[j],women)):
                            del paired_men[paired_women[j]]
                            paired_men[i] = j
                            paired_women[j]=i
                            break
    return paired_men,paired_women
n=int(input("number of men: "))
men1=input_men_or_women(n,"men")
women1=input_men_or_women(n,"women")
a,b=gale_shapley(men1,women1,n)
print(a)
print(b)