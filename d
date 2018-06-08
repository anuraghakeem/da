graph={1:[2,5],2:[1,3],3:[2,4,5],4:[3,5],5:[1,3,4]}
edges={(1,2):10,(1,5):100,(2,3):50,(5,3):10,(5,4):60,(3,4):20}

def dijkstra(source):
    S=[source]
    V=list(graph.keys())
    
    distance=[999]*(len(V)+1)
    distance[source]=0

    while len(S)!=len(V):
        d={}
        for u in S:
            for v in graph[u]:
                if v not in S:
                    if (u,v) in edges:
                        cost=distance[u]+edges.get((u,v))
                    elif (v,u) in edges:
                        cost=distance[u]+edges.get((v,u))
                    d[cost]=(u,v)

        min_cost=min(d)
        uv=d.get(min_cost)
        v=uv[1]
        distance[v]=min_cost
        S.append(v)
    return distance

final=dijkstra(1)
print(final)
