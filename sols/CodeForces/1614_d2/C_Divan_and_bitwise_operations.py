''' C. Divan and bitwise operations
https://codeforces.com/contest/1614/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

INF = float('inf')
MOD = 10**9 + 7

def solve(N, M, segments):
	# D[x][i] = changes in num segments requiring bit i to be 0 after processing x=0..N
	D = [[0]*32 for _ in range(N+1)]
	for l, r, x in segments:
		for i in range(32):
			if (x >> i) & 1 == 0:
				D[l-1][i] += 1
				D[r][i] -= 1

	# seq = possible sequence
	# zero[i] = num segments requiring bit i to be 0
	seq = [0]*N
	zero = [0]*32
	for i in range(N):
		cand = 0
		for j in range(32):
			zero[j] += D[i][j]
			if zero[j] > 0: continue
			cand |= (1 << j)
		seq[i] = cand

	# XOR sum
	bits = 0 
	for val in seq:
		bits |= val
	res = bits * pow(2, N-1, MOD)

	return res % MOD


def main():
	T = int(input())
	for _ in range(T):
		N, M = list(map(int, input().split()))
		segments = [list(map(int, input().split())) for _ in range(M)]
		out = solve(N, M, segments)
		output(f'{out}\n')


if __name__ == '__main__':
	main()

