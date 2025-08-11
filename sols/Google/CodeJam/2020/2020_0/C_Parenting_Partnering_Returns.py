''' Parenting Partnering Returns
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020bdf9
'''

def solve(N,intervals):
	if N == 1: return 'C'
	if N == 2: return 'CJ'

	indices = sorted(range(N), key=lambda k: intervals[k])
	res = [-1]*N
	res[indices[0]] = 0

	for i in range(1,N):
		s2,e2 = intervals[indices[i]]
		for j in range(i):
			s1,e1 = intervals[indices[j]]
			if s1 <= s2 < e1:
				if res[indices[i]] == -1: res[indices[i]] = 1-res[indices[j]]
				if res[indices[i]] == res[indices[j]]: return 'IMPOSSIBLE'
		if res[indices[i]] == -1: 
			res[indices[i]] = 0

	return ''.join('J' if x else 'C' for x in res)


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		N = int(stdin.readline().strip())
		intervals = []
		for _ in range(N):
			s,e = list(map(int,stdin.readline().strip().split()))
			intervals.append((s,e))
		out = solve(N,intervals)
		print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
	main()