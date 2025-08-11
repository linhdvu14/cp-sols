''' B. Absent Remainder
https://codeforces.com/contest/1613/problem/B
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

INF = float('inf')

def solve(N, A):
	A.sort()
	for i in range(N//2):
		print(f'{A[i+1]} {A[0]}')


def main():
	T = int(input())
	for _ in range(T):
		N = int(input())
		A = list(map(int, input().split()))
		solve(N, A)


if __name__ == '__main__':
	main()

