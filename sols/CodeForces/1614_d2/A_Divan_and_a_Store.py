''' A. Divan and a Store
https://codeforces.com/contest/1614/problem/A
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

INF = float('inf')

def solve(N, L, R, K, A):
	res = 0
	A.sort()
	for a in A:
		if L <= a <= R:
			K -= a
			if K < 0: break
			res += 1
	return res


def main():
	T = int(input())
	for _ in range(T):
		N, L, R, K = list(map(int, input().split()))
		A = list(map(int, input().split()))
		out = solve(N, L, R, K, A)
		output(f'{out}\n')


if __name__ == '__main__':
	main()

