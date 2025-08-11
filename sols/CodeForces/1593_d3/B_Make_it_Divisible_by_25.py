''' B. Make it Divisible by 25
https://codeforces.com/contest/1593/problem/B
'''

import sys
input = sys.stdin.readline
output = print

targets = ['00', '50', '25', '75']

def solve(S):
	res = N = len(S)
	if N >= 2 and S[N-2:] in targets: return 0
	for i in range(N):
		for j in range(i+1, N):
			if S[i] + S[j] in targets:
				res = min(res, j-i-1 + N-j-1)
	return res


def main():
	T = int(input())
	for _ in range(T):
		S = input().strip()
		out = solve(S)
		output(out)


if __name__ == '__main__':
	main()

