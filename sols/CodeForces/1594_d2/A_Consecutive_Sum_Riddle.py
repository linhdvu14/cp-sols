''' A. Consecutive Sum Riddle
https://codeforces.com/contest/1594/problem/A
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(N):
	l, r = -N+1, N
	output(str(l) + ' ' + str(r) + '\n')

def main():
	T = int(input())
	for _ in range(T):
		N = int(input())
		solve(N)


if __name__ == '__main__':
	main()

