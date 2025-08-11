''' A. Elections
https://codeforces.com/contest/1593/problem/A
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = print

def solve(a, b, c):
	ma = max(b+1, c+1, a) - a
	mb = max(a+1, c+1, b) - b
	mc = max(a+1, b+1, c) - c
	output(f'{ma} {mb} {mc}')


def main():
	T = int(input())
	for _ in range(T):
		a, b, c = list(map(int, input().split()))
		solve(a, b, c)


if __name__ == '__main__':
	main()

