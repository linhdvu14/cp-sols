''' A. Divide and Multiply
https://codeforces.com/contest/1609/problem/A
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

INF = float('inf')

def solve(N, A):
	res = pow = odd = 0
	for a in A:
		while a & 1 == 0:
			pow += 1
			a >>= 1
		res += a
		odd = max(odd, a)

	res += (odd << pow) - odd
	return res


def main():
	T = int(input())
	for _ in range(T):
		N = int(input())
		A = list(map(int, input().split()))
		out = solve(N, A)
		output(f'{out}\n')


if __name__ == '__main__':
	main()

