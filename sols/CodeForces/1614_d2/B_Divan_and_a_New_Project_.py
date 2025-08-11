''' B. Divan and a New Project
https://codeforces.com/contest/1614/problem/B
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

INF = float('inf')

def solve(N, A):
	A = [(a, i+1) for i, a in enumerate(A)]
	A.sort(reverse=True)
	
	res = [0]*(N+1)
	cnt = 0
	for i, (a, idx) in enumerate(A):
		d = i // 2 + 1
		if i % 2 == 0: d *= -1
		res[idx] = d
		cnt += 2 * abs(d) * a

	print(cnt)
	print(' '.join(map(str, res)))


def main():
	T = int(input())
	for _ in range(T):
		N = int(input())
		A = list(map(int, input().split()))
		solve(N, A)


if __name__ == '__main__':
	main()

