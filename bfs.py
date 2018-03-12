a=int(input("number of nodes"))
g={}
for i in range(a):
    print("for",i+1,"enter all the conecting nodes:",)
    b=list(map(int,input().split()))
    for j in b:
        if i+1 not in g:
            g.update({i+1:[j]})
        else:
            g[i+1].append(j)
def bfs(graph, start):
    visited, queue = [], [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend([i for i in graph[vertex] if i not in visited])
    return visited
s=int(input("starting point of graph"))
print(bfs(g,s))