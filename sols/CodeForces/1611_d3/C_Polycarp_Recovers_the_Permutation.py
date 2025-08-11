''' C. Polycarp Recovers the Permutation
https://codeforces.com/contest/1611/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

from collections import deque

def solve1(N, A):
	if A[0] != N and A[-1] != N: return [-1]
	A = deque(A)
	res = deque([])
	while A:
		if A[0] > A[-1]:
			res.appendleft(A.popleft())
		else:
			res.append(A.pop())
	return res

def solve2(N, A):
	if A[0] == N: return [A[0]] + A[1:][::-1]
	if A[-1] == N: return A[:-1][::-1] + [A[-1]]
	return [-1]

solve = solve2

def main():
	T = int(input())
	for _ in range(T):
		N = int(input())
		A = list(map(int, input().split()))
		out = solve(N, A)
		print(' '.join(map(str, out)))


if __name__ == '__main__':
	main()

