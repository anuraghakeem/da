def inputjobs(n):
	global jobs
	jobs.append([0,0,0,0])
	for i in range(n):
		print('Enter job {0}'.format(i+1))
		s=int(input())
		f=int(input())
		w=int(input())
		jobs.append([s,f,w,i+1])
	jobs.sort(key=lambda x:x[1])

def predecessor(n):
	global jobs
	if(n<=1):
		return 0
	else:
		k=n-1
		while(k>0):
			if(jobs[n][0]>=jobs[k][1]):
				break
			else:
				k=k-1
		return k

def opt(n):
	global M
	global jobs
	M.append(0)
	for i in range(1,n+1):
		M.append(max(M[i-1],jobs[i][2]+M[predecessor(i)]))

def findsch(n):
	global M
	global jobs
	schedule=[]
	j=n
	while(j>0):
		if(jobs[j][2]+M[predecessor(j)]>=M[j-1]):
			schedule.append(jobs[j])
			j=predecessor(j)
		else:
			j=j-1
	return schedule

M=[]
jobs=[]
n=int(input('how many jobs'))
inputjobs(n)
opt(n)
print(M)
schedule=findsch(n)
print(schedule)
for i in schedule:
	print(i)