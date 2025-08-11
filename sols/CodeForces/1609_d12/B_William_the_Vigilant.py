''' B. William the Vigilant
https://codeforces.com/contest/1609/problem/B
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

INF = float('inf')

def solve(N, Q, S, queries):
	def is_substr(i): return 0 <= i < N-2 and S[i] == 'a' and S[i+1] == 'b' and S[i+2] == 'c'

	S = list(S)
	cnt = sum(1 for i in range(N) if is_substr(i))

	for i, c in queries:
		if any(is_substr(i-j) for j in range(3)): cnt -= 1
		S[i] = c
		if any(is_substr(i-j) for j in range(3)): cnt += 1
		print(cnt)


def main():
	N, Q = list(map(int, input().split()))
	S = input().decode().strip()
	queries = []
	for _ in range(Q):
		ts = input().decode().strip().split()
		queries.append((int(ts[0])-1, ts[1]))
	solve(N, Q, S, queries)


if __name__ == '__main__':
	main()

