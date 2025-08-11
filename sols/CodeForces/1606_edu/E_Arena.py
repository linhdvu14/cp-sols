''' E. Arena
https://codeforces.com/contest/1606/problem/E
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

from functools import lru_cache
MOD = 998244353 

# POW[x][n] = x^n % MOD
POW = [[0]*501 for _ in range(501)]
for x in range(501):
	for n in range(501):
		POW[x][n] = pow(x, n, MOD)

# C[n][k] = nCk % MOD
C = [[0]*501 for _ in range(501)]
for n in range(501):
	for k in range(501):
		if k == 0 or n == k:
			C[n][k] = 1
		elif n == 0:
			C[n][k] = 0
		else:
			C[n][k] = (C[n-1][k] + C[n-1][k-1]) % MOD


def solve(N, X):
	# num ways to choose initial health for n heroes, from 1..x
	# s.t. no winner
	@lru_cache(None)
	def dp(n, x):
		if x <= 0: return 0
		if n <= 0: return 1
		if n == 1: return 0

		# all die after this round
		if x < n: return POW[x][n]

		# after this round:
		# * k heroes die (health this round = 1..n-1)
		# * n-k heroes remain (health next round = 1..x-(n-1))
		res = 0
		for k in range(n+1):
			res += C[n][k] * POW[min(n-1, x)][k] * dp(n-k, x-(n-1))
			res %= MOD
		
		return res
	
	return dp(N, X)



def main():
	N, X = list(map(int, input().split()))
	out = solve(N, X)
	output(str(out) + '\n')


if __name__ == '__main__':
	main()

