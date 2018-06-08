def inputgraph(ne):
	global graph
	global infinity
	for i in range(ne):
		print('Enter vertex {0}'.format(i+1))
		u=int(input())
		v=int(input())
		w=int(input())
		infinity=infinity+w*2
		graph.append((u,v,w))

def belman_ford(n,source):
	global graph
	global infinity
	distance=[infinity for i in range(0,n+1)]
	distance[s]=0
	for i in range(n-1):
		for triple in graph:
			distance[triple[1]]=min(distance[triple[1]],distance[triple[0]]+triple[2])
	del distance[0]
	return distance

graph=[]
infinity=1
n=int(input('Enter number of vertices'))
ne=int(input('Enter the number of edges'))
inputgraph(ne)
s=int(input('Enter source vertex'))
dset=belman_ford(n,s)
print(dset)	
