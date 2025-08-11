''' C. Make Them Equal
https://codeforces.com/contest/1594/problem/C
'''

import sys
input = sys.stdin.readline
output = print

def solve(N, C, S):
	if all(c==C for c in S): return (0, [])
	last = -1
	for i in range(N-1, -1, -1):
		if S[i] == C:
			last = i+1
			break
	if last*2 <= N: return (2, [N, N-1])
	return (1, [last])
	

def main():
	T = int(input())
	for _ in range(T):
		N, C = input().strip().split(' ')
		N = int(N)
		S = input().strip()
		times, idx = solve(N, C, S)
		print(times)
		if times > 0: print(' '.join(map(str, idx)))


if __name__ == '__main__':
	main()

