''' A. Make Even
https://codeforces.com/contest/1611/problem/A
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(S):
	if int(S[-1]) % 2 == 0: return 0
	if int(S[0]) % 2 == 0: return 1
	for c in S:
		if int(c) % 2 == 0: return 2
	return -1


def main():
	T = int(input())
	for _ in range(T):
		S = input().decode().strip()
		out = solve(S)
		output(f'{out}\n')


if __name__ == '__main__':
	main()

