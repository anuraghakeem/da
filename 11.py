n=3
W=5
weights=[99,2,2,3]
values=[99,20,10,30]

#M= [[0 for x in range(W+1)] for y in range(n+1)] 
M=[[0]*(W+1) for x in range(n+1)]
for i in range(1,n+1):
    for w in range(1,W+1):
        if weights[i]>w:
            M[i][w]=M[i-1][w]
        else:
            M[i][w]=max(M[i-1][w],values[i]+M[i-1][w-weights[i]])

print(M)

i=n
k=W

while i>0 and k>0:
    if M[i][k]!=M[i-1][k]:
        print(i)
        k=k-weights[i]
    i=i-1
