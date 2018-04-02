from collections import defaultdict
def prim(G,s):
    q,p,visit={},{},[i for i in G]
    for i in G:
        q[i]=float('inf')
    q[s],p[s]=0,None
    while q:
        u=min(q.items(), key=lambda x: x[1])[0]
        if u in q: del q[u]
        print(u)
        for v in G[u]:
            if v in q and G[v][u]<q[v]:
                p[v]=u
                q[v]=G[u][v]
    return p

'''
g={0: {1: 3, 3: 6, 2: 1},
   1: {0: 3, 4: 3, 2: 10}, 
   4: {1: 3, 5: 6, 2: 6}, 
   5: {4: 6, 3: 2, 2: 4}, 
   3: {5: 2, 0: 6, 2: 5}, 
   2: {0: 1, 1: 10, 4: 6, 5: 4, 3: 5}}
'''

# graph=  {
#     1: {2:4 , 4:8},
#     2: {1:4 , 3:3 , 4:1},
#     3: {2:3 , 4:7 , 5:8},
#     4: {1:8 , 2:1 , 3:7 , 5:3},
#     5: {3:8 , 4:3}
#     }
    
graph = defaultdict(dict)
n = int(input("Enter number of nodes"))
for i in range(1,n+1):
  x = int(input("Enter number of nodes connected to "+ str(i)))
  for y in range(x):
    f = input("Enter destination and distance connected to "+ str(i)+" separated by comma")
    d,l = f.split(',')
    d = int(d)
    l = int(l)
    graph[i][d] = l

print(prim(graph,1))