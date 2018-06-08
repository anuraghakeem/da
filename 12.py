n=6
jobs=[[99,0,99],[1,2,100],[2,5,200],[3,6,300],[4,8,400],[5,9,500],[6,10,100]]
jobs.sort(key=lambda x: x[1])

start=0
finish=1
value=2

P=[0]*(n+1)
P[0]=99
M=[0]*(n+1)

def pj():
    for i in range(n,1,-1):
        for j in range(i-1,0,-1):
            if jobs[j][finish]<=jobs[i][start]:
                P[i]=j
                break

def compute():
    for j in range(1,n+1):
        M[j] = max(jobs[j][value]+ M[P[j]], M[j-1])

def Find_Solution(j):
    if j > 0:
        if jobs[j][value]+ M[P[j]] >= M[j-1]:
            print(j)
            Find_Solution(P[j])
        else:
            Find_Solution(j-1)

pj()
compute()
Find_Solution(n)
