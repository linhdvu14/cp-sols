''' C. Keshi Is Throwing a Party
https://codeforces.com/contest/1610/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(N, bounds):
	def is_ok(x):
		cnt = 0
		for a, b in bounds:
			if a >= x - cnt - 1 and b >= cnt:
				cnt += 1
		return cnt >= x
	
	res, lo, hi = 0, 1, N
	while lo <= hi:
		mi = (lo+hi) // 2
		if is_ok(mi):
			res = mi
			lo = mi + 1
		else:
			hi = mi - 1

	return res


def main():
	T = int(input())
	for _ in range(T):
		N = int(input())
		bounds = [tuple(map(int, input().split())) for _ in range(N)]
		out = solve(N, bounds)
		output(f'{out}\n')


if __name__ == '__main__':
	main()

