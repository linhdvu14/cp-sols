''' G. Changing Brackets
https://codeforces.com/contest/1593/problem/G
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str

def solve(S, Q, queries):
	S = ''.join('a' if c in '[]' else 'b' for c in S)
	N = len(S)

	# aa/bb, bb/aa alr balanced
	# ab/ba, ba/ab cancel out
	# ab/ab, ba/ba incur cost 1
	prefix = [[0], [0]]
	for i in range(N):
		if i + 2 > N: break
		sub = S[i:i+2]
		nxt = prefix[i%2][-1]
		if sub in ['ab', 'ba']:
			nxt += 1 if sub == 'ab' else - 1
		prefix[i%2].append(nxt)

	for l, r in queries:
		if l % 2 == 0:
			ls, rs = prefix[0][l//2], prefix[0][(r+1)//2]
		else:
			ls, rs = prefix[1][(l-1)//2], prefix[1][r//2]
		print(abs(rs - ls))


def main():
	T = int(input())
	for _ in range(T):
		S = input().decode()
		Q = int(input())
		queries = []
		for _ in range(Q):
			l, r = list(map(int, input().split()))
			queries.append((l-1, r-1))
		solve(S, Q, queries)


if __name__ == '__main__':
	main()

