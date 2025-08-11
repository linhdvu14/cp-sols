''' B. Special Numbers
https://codeforces.com/contest/1594/problem/B
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

MOD = 10**9 + 7

def solve(N, K):
	res = 0
	p = 1
	while K > 0:
		if K & 1: res = (res + p) % MOD
		p = (p*N) % MOD
		K >>= 1
	return res

def main():
	T = int(input())
	for _ in range(T):
		N, K = list(map(int, input().split()))
		out = solve(N, K)
		output(str(out) + '\n')

if __name__ == '__main__':
	main()

