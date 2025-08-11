''' Workout
https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3f5b
'''

def solve(k,mins):
	vals = [mins[i]-mins[i-1] for i in range(1,len(mins),1)]
	vals.sort()

	def isValid(mi, k):
		for v in vals:
			if v <= mi: continue
			c = v // mi 
			if v % mi != 0: c += 1
			k -= c-1
			if k < 0: return False
		return True

	lo, hi =  1, vals[-1]
	res = hi
	while lo <= hi:
		mi = lo + (hi-lo) // 2
		if isValid(mi, k):
			hi = mi-1
			res = mi
		else:
			lo = mi+1
	return res



def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		N,K = list(map(int,stdin.readline().strip().split()))
		mins = list(map(int,stdin.readline().strip().split()))
		out = solve(K,mins)
		print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
	main()