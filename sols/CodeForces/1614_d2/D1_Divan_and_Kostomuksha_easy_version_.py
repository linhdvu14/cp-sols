''' D1. Divan and Kostomuksha (easy version)
https://codeforces.com/contest/1614/problem/D1
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

INF = float('inf')


def solve(N, A):
	# F[a] = all factors of a
	F = {}
	def get_factors(a):
		if a in F: return F[a]
		facs = []
		d = 2
		while d*d < a:
			if a % d == 0:
				facs.append(d)
				facs.append(a // d)
			d += 1
		if d*d == a: facs.append(d)
		facs.append(1)
		F[a] = facs
		return facs

	# C[f] = num elements in A divisible by f
	C = {}
	for a in A:
		facs = get_factors(a)
		for f in facs: 
			C[f] = C.get(f, 0) + 1
		if a != 1: C[a] = C.get(a, 0) + 1
	
	# let g[i]=gcd(a[1]..a[i]) for i=1..N
	# then g[1], g[2]...., g[N] is non-increasing, g[i] % g[i+1] == 0
	# want to max SUM_i g[i]

	# dp(g, p) = max gcd sum from this point onward where
	# * g is the next gcd
	# * p numbers already placed
	def dp(g, p=0, memo={}):
		if g == 1: return N-p

		# memo[g] = max gcd sum onwards immediately after using g
		# all numbers already placed are multiples of g
		# so exactly C[g] numbers already placed
		if g not in memo:
			facs = get_factors(g)
			memo[g] = max(dp(f, C[g], memo) for f in facs)
		
		# C[g]-p multiples of g left to place
		return memo[g] + g*(C[g]-p)

	# try each possible g[1]
	res = max(dp(a) for a in A)

	return res


def main():
	N = int(input())
	A = list(map(int, input().split()))
	out = solve(N, A)
	output(f'{out}\n')


if __name__ == '__main__':
	main()



