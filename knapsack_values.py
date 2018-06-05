def inputset():
	global n,item_weights,W,item_values
	n=int(input('Enter the number of items'))
	item_weights.append(0)
	item_values.append(0)
	for i in range(0,n):
		w=int(input('Enter weight of item{0}'.format(i+1)))
		item_weights.append(w)
		v=int(input('Enter value of item{0}'.format(i+1)))
		item_values.append(v)
	W=int(input('Enter total capacity'))

def subset():
	global n,W,item_weights,matrix,item_values
	for i in range(0,W+1):
		matrix[0][i]=0
	for i in range(0,n+1):
		matrix[i][0]=0
	for i in range(1,n+1):
		for w in range(1,W+1):
			if(w<item_weights[i]):
				matrix[i][w]=matrix[i-1][w]
			else:
				matrix[i][w]=max(matrix[i-1][w],item_values[i]+matrix[i-1][w-item_weights[i]])
	print(matrix)
	return matrix[n][W]

def knapsack():
	global n,W,item_weights,matrix,item_values
	i=n
	k=W
	optset=[]
	while(i>0 and k>0):
		if(matrix[i][k]!=matrix[i-1][k]):
			optset.append(i)
			k=k-item_weights[i]
			i=i-1
		else:
			i=i-1
	return optset

n=0
W=0
item_weights=[]
item_values=[]
inputset()
matrix=[[0 for j in range(0,W+1)] for i in range(0,n+1)]
maxval=subset()
optimum=knapsack()
print(maxval)
print(optimum)