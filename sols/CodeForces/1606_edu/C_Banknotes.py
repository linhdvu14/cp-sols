''' C. Banknotes
https://codeforces.com/contest/1606/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(N, K, pows):
	# costs[i] = f(10^pows[i]-1) = min notes to make all amount up to 10^pows[i] - 1
	# e.g. pows = [1, 10^2, 10^5], f(10^5-1) = f(10^2-1) + 999 (to make 999*10^2)
	costs = [0]*N
	for i in range(1, N):
		costs[i] = costs[i-1] + 10**(pows[i]-pows[i-1]) - 1
	
	i = 1
	while i < N:
		if costs[i] > K: break
		i += 1

	# to make max number using K notes:
	# * reserve costs[i-1] to make 0..10^pows[i-1]-1
	# * remain K-costs[i-1] to buy 10^pows[i-1]
	return (K - costs[i-1] + 1) * 10**(pows[i-1]) + 10**(pows[i-1]) - 1


def main():
	T = int(input())
	for _ in range(T):
		N, K = list(map(int, input().split()))
		pows = list(map(int, input().split()))
		out = solve(N, K, pows)
		output(str(out) + '\n')


if __name__ == '__main__':
	main()
