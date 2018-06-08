graph={1:[2,4],2:[1,3,4],3:[2,4,6],4:[1,2,3,6],6:[3,4]}
edges={(1,2):4,(1,4):8,(2,4):1,(2,3):3,(3,4):7,(3,6):8,(4,6):3}

def prim(source):
    U=[source]
    V=list(graph.keys())
    tree={}

    while len(U)!=len(V):
        d={}
        for u in U:
            for v in set(V)-set(U):
                if (u,v) in edges:
                    cost=edges.get((u,v))
                    d[cost]=(u,v)
                elif (v,u) in edges:
                    cost=edges.get((v,u))
                    d[cost]=(u,v)
                else:
                    pass

        min_cost=min(d)
        uv=d.get(min_cost)
        v=uv[1]
        tree[uv]=min_cost
        U.append(v)

    return tree

final=prim(1)
print(final)
                        
                    
                    
    
    
