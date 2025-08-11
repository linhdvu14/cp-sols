''' A. A.M. Deviation
https://codeforces.com/contest/1605/problem/A
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(a, b, c):
	d = abs(a + b - 2*c) % 3
	return min(d, 1)


def main():
	T = int(input())
	for _ in range(T):
		a, b, c = list(map(int, input().split()))
		out = solve(a, b, c)
		output(f'{out}\n')


if __name__ == '__main__':
	main()

