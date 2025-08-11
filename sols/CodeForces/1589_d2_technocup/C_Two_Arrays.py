''' C. Two Arrays
https://codeforces.com/contest/1589/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(N, A, B):
	A.sort()
	B.sort()
	return all(a == b or a+1==b for a, b in zip(A, B))

def main():
	T = int(input())
	for _ in range(T):
		N = int(input())
		A = list(map(int, input().split()))
		B = list(map(int, input().split()))
		out = solve(N, A, B)
		print('YES' if out else 'NO')


if __name__ == '__main__':
	main()

