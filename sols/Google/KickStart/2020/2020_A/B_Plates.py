''' Plates
https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d40bb
'''

def solve(vals, p):
	n, k = len(vals), len(vals[0])
	sums = [[0 for x in range(k+1)] for y in range(n)]
	for i in range(n):
		for j in range(1,k+1):
			sums[i][j] = sums[i][j-1] + vals[i][j-1]

	def _solve(n,p,memo):  # return mx  using up to n-th stack, with p plates remaining
		if n == 0 or p == 0: return 0
		if (n,p) in memo: return memo[(n,p)]
		mx = 0
		for i in range(min(p,k)+1):
			mx = max(mx, _solve(n-1,p-i,memo) + sums[n-1][i])
		memo[(n,p)] =  mx
		return memo[(n,p)]

	return _solve(n,p,{})




def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		N,K,P = list(map(int,stdin.readline().strip().split()))
		vals = []
		for _ in range(N):
			plates = list(map(int,stdin.readline().strip().split()))
			vals.append(plates)
		out = solve(vals,P)
		print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
	main()