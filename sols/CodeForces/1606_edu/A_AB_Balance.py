''' A. AB Balance
https://codeforces.com/contest/1606/problem/A
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(S):
	if S[0] == S[-1]: return S
	return S[:-1] + S[0]


def main():
	T = int(input())
	for _ in range(T):
		S = input().decode().strip()
		out = solve(S)
		output(str(out) + '\n')


if __name__ == '__main__':
	main()


