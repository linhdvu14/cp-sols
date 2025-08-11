''' A. Mathematical Addition
https://codeforces.com/contest/1589/problem/A
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(u, v):
	print(f'{-u*u} {v*v}')

def main():
	T = int(input())
	for _ in range(T):
		u, v = list(map(int, input().split()))
		solve(u, v)


if __name__ == '__main__':
	main()

