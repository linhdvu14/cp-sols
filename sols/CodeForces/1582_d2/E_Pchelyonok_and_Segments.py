''' E. Pchelyonok and Segments
https://codeforces.com/contest/1582/problem/E
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

from math import sqrt

MAX = float('inf')

def solve(N, nums):
	K = int(sqrt(N*2))+1

	pref = [0]*(N+1)
	for i in range(N): pref[i+1] = pref[i] + nums[i]

	# dp[i][k] =
	# * using nums[i..]
	# * place segments of length k, k-1, ..., 1
	# * what is max possible sum for length-k segment (0 if no possible placements)
	# ---> res = max(k s.t. dp[0][k] > 0)
	dp = [MAX]*(N+1)
	
	res = 1
	for k in range(1, K):
		ndp = [0]*(N+1)
		for i in range(N-k*(k+1)//2, -1, -1):
			ndp[i] = ndp[i+1]
			s = pref[i+k] - pref[i]   # current length-k segment
			if s < dp[i+k]: ndp[i] = max(ndp[i], s)
		if ndp[0] == 0: break
		res = k
		dp = ndp

	return res

def main():
	T = int(input())
	for _ in range(T):
		N = int(input())
		nums = list(map(int, input().split()))
		out = solve(N, nums)
		output(str(out) + '\n')


if __name__ == '__main__':
	main()

