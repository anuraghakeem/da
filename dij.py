import time
from collections import defaultdict
from heapq import heappush, heappop
def Dijkstra(graph,start):
    A={}
    queue = {start:0}
    while queue:
        v,path_len=min(queue.items(), key=lambda x: x[1])
        if v in queue: del queue[v]
        if v not in A :
            A[v] = path_len
            for w,edge_len in graph[v].items():
                if w not in A :
                    queue[w]=path_len+edge_len
    return A



# graph = {0 : {1:6, 2:8},
# 1 : {4:11},
# 2 : {3: 9},
# 3 : {},
# 4 : {5:3},
# 5 : {2: 7, 3:4}}


graph = defaultdict(dict)
n = int(input("Enter number of nodes"))
for i in range(n):
  x = int(input("Enter number of nodes connected to "+ str(i)))
  for y in range(x):
    f = input("Enter destination and distance connected to "+ str(i)+" separated by comma")
    d,l = f.split(',')
    d = int(d)
    l = int(l)
    graph[i][d] = l
    
print (graph)
  

start=time.clock()
print(Dijkstra(graph,0))
print(time.clock()-start)