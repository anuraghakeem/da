a=int(input("number of nodes"))
g={}
for i in range(a):
    print("for",i+1)
    b=list(map(int,input().split()))
    for j in b:
        if i+1 not in g:
            g.update({i+1:[j]})
        else:
            g[i+1].append(j)
def DFS(g,start,path=[]):
    path.append(start)
    for i in g[start]:
        if i not in path:
            y=DFS(g,i,path)
    return path
start=int(input("enter the start node"))
print(DFS(g,start))
