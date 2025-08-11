''' B. Odd Grasshopper
https://codeforces.com/contest/1607/problem/B
'''

import io, os, sys
from random import randint
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(X, N):
	if N == 0: return X
	if N == 1: return X-1 if X % 2 == 0 else X +1
	dist = 4 * ((N-1)//4)
	if (N-1) % 4 == 1: dist -= N
	if (N-1) % 4 == 2: dist -= N + N-1
	if (N-1) % 4 == 3: dist += N - (N-1) - (N-2)
	return X - 1 - dist if X % 2 == 0 else X + 1 + dist

def main():
	T = int(input())
	for _ in range(T):
		X, N = list(map(int, input().split()))
		out = solve(X, N)
		output(str(out) + '\n')


if __name__ == '__main__':
	main()

