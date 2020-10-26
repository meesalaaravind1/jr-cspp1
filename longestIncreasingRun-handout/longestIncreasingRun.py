
def longestIncreasingRun(n):
	n=str(abs(n))
	seq=str(n[0])
	if (n[1])>n[0]:
		seq+=str(n[1])
	best=str(n[0])
	for i in range(1,len(n)-1):
		if int(n[i])<=int(n[i+1]):
			seq+=n[i+1]
		else:
			# print (seq)
			if len(seq)>=len(best) and int(seq)>int(best):
				best=seq
			seq=n[i+1]
	if len(seq)>=len(best)and int(seq)>int(best):
		best=seq
	return int(best)

print(longestIncreasingRun(int(input())))
