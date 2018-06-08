n=5
graph=[[1,2,4],[2,3,3],[2,4,1],[1,4,8],[4,3,7],[3,5,8],[4,5,3]]

graph.sort(key=lambda x:x[2])
parent=[-1]*(n+1)

def find_parent(node):
    if parent[node]==-1:
        return node
    else:
        return parent[node]
    
def union_sets(u,v):
    u_p=find_parent(u)
    v_p=find_parent(v)
    parent[u_p]=v_p

count=0
final=[]

for edge in graph:
    if count==n-1:
        break

    u=edge[0]
    v=edge[1]
    
    u_p=find_parent(u)

    v_p=find_parent(v)
    
    if u_p!=v_p:
        count=count+1
        final.append(edge)
        union_sets(u,v)

print(final)
        
