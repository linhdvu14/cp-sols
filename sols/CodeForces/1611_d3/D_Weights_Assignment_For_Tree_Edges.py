''' D. Weights Assignment For Tree Edges
https://codeforces.com/contest/1611/problem/D
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(N, B, P):
	B = [b-1 for b in B]
	P = [p-1 for p in P]
	if B[P[0]] != P[0]: return [-1]
	
	res = [-1]*N   # dist to par
	dist = [-1]*N  # dist to root
	for d, c in enumerate(P):
		if d == 0:
			res[c] = 0
			dist[c] = 0
			continue
		b = B[c]
		if dist[b] == -1: return [-1]
		dist[c] = d
		res[c] = d - dist[b]

	return res


def main():
	T = int(input())
	for _ in range(T):
		N = int(input())
		B = list(map(int, input().split()))
		P = list(map(int, input().split()))
		out = solve(N, B, P)
		print(' '.join(map(str, out)))


if __name__ == '__main__':
	main()

