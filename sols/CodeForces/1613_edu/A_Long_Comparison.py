''' A. Long Comparison
https://codeforces.com/contest/1613/problem/A
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

INF = float('inf')

def solve(x1, p1, x2, p2):
	p1, p2 = int(p1), int(p2)
	mn = min(p1, p2)
	p1 -= mn
	p2 -= mn

	N1, N2 = len(x1), len(x2)
	if N1+p1 < N2+p2: return '<'
	if N1+p1 > N2+p2: return '>'
	for i in range(N1+p1):
		n1 = x1[i] if i < N1 else '0'
		n2 = x2[i] if i < N2 else '0'
		if n1 < n2: return '<'
		if n1 > n2: return '>'
	return '='


def main():
	T = int(input())
	for _ in range(T):
		x1, p1 = input().decode().strip().split()
		x2, p2 = input().decode().strip().split()
		out = solve(x1, p1, x2, p2)
		output(f'{out}\n')


if __name__ == '__main__':
	main()

