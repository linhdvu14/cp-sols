''' B. Coloring Rectangles
https://codeforces.com/contest/1589/problem/B
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(N, M):
	a, ra = divmod(N, 3)
	b, rb = divmod(M, 3)
	res = a * b * 3 + b * ra + a * rb
	if ra == 0 or rb == 0: return res
	if ra == rb == 2: return res + 2
	return res + 1


def main():
	T = int(input())
	for _ in range(T):
		N, M = list(map(int, input().split()))
		out = solve(N, M)
		output(f'{out}\n')


if __name__ == '__main__':
	main()

