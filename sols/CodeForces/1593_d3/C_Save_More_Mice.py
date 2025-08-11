''' C. Save More Mice
https://codeforces.com/contest/1593/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(N, K, points):
	points.sort(reverse=True)
	res = 0
	bal = N
	for pi in points:
		bal -= N - pi
		if bal <= 0: break
		res += 1
	return res


def main():
	T = int(input())
	for _ in range(T):
		N, K = list(map(int, input().split()))
		points = list(map(int, input().split()))
		out = solve(N, K, points)
		output(str(out) + '\n')


if __name__ == '__main__':
	main()

