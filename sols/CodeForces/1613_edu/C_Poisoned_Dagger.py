''' C. Poisoned Dagger
https://codeforces.com/contest/1613/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

INF = float('inf')


def solve(N, H, A):
	def is_ok(K):
		cnt = K
		for i in range(N-1):
			cnt += min(A[i+1]-A[i], K)
		return cnt >= H

	res, lo, hi = -1, 1, H
	while lo <= hi:
		mi = (lo+hi) // 2
		if is_ok(mi):
			res = mi
			hi = mi-1
		else:
			lo = mi+1

	return res


def main():
	T = int(input())
	for _ in range(T):
		N, H = list(map(int, input().split()))
		A = list(map(int, input().split()))
		out = solve(N, H, A)
		output(f'{out}\n')


if __name__ == '__main__':
	main()

