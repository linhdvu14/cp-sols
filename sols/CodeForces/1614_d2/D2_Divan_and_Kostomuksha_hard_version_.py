''' D2. Divan and Kostomuksha (hard version)
https://codeforces.com/contest/1614/problem/D2
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

INF = float('inf')

def sieve(N):
   '''return all primes in [2..N] in O(N)'''
   primes = []
   mpf = [0]*(N+1)  # min prime factor
   for i in range(2, N+1):
       if mpf[i] == 0:
           primes.append(i)
           mpf[i] = i
       for p in primes:
           if p*i > N or p > mpf[i]: break  # mpf[p*i] <= mpf[i] < p
           mpf[p*i] = p                     # once per composite number
   return primes, mpf


# https://codeforces.com/contest/1614/submission/137008425

def solve(N, A):
	MAX = max(A)
	primes, mpf = sieve(MAX + 1)

	# F[a] = all unique prime factors of a
	F = {}
	def get_factors(a):
		if a in F: return F[a]
		facs = []
		while a > 1:
			facs.append(mpf[a])
			while facs[-1] == mpf[a]: a //= mpf[a] 
		return facs

	# C[f] = num elements in A divisible by f
	# think of primes as axes and numbers as points with coordinates = powers of primes
	# for each possible factor f, want to calc how many points a in A have all coordinates >= f
	C = [0]*(MAX+1)
	for a in A: C[a] += 1

	# i.e. for each point a, want to increment count for each b inside the cube 0..a
	# to ensure a increments each b once and only once, there has to be a unique counting path from a to b
	# the below procedure traverses each axis one by one, hence ensures unique paths
	# note that the order of primes/axes are therefore not important
	# it's easiest to visualize a 2D lattice (2 primes)
	for p in primes:
		for a in range(MAX//p, 0, -1):
			C[a] += C[a*p]

	# let g[i]=gcd(a[1]..a[i]) for i=1..N
	# then g[1], g[2]...., g[N] is non-increasing, g[i] % g[i+1] == 0
	# want to max SUM_i g[i]

	# dp(g, p) = max gcd sum from this point onward where
	# * g is the next gcd
	# * p numbers already placed
	# * memo[g] = dp(f, C[g]) over all factors f of g
	#   --> max gcd sum onwards after choosing g as first gcd
	def dp(g, p=0, memo={}):
		if g == 1: return N-p
		if g not in memo:
			facs = get_factors(g)
			memo[g] = max(dp(g//f, C[g], memo) for f in facs)
		
		# note previous p numbers are all multiples of g
		# so there are C[g]-p multiples of g left to place
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

