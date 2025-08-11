''' A. Anti Light's Cell Guessing
https://codeforces.com/contest/1610/problem/A
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(N, M):
	if N == M == 1: return 0
	if N == 1 or M == 1: return 1
	return 2


def main():
	T = int(input())
	for _ in range(T):
		N, M = list(map(int, input().split()))
		out = solve(N, M)
		output(f'{out}\n')


if __name__ == '__main__':
	main()

