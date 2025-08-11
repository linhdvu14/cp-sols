''' E1. Rubik's Cube Coloring (easy version)
https://codeforces.com/contest/1594/problem/E1
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

MOD = 10**9 + 7

def solve(K):
	m = 16
	res = 6
	for _ in range(K-1):
		res = (res * m) % MOD
		m = (m*m) % MOD
	return res


def main():
	K = int(input())
	out = solve(K)
	output(str(out) + '\n')


if __name__ == '__main__':
	main()

