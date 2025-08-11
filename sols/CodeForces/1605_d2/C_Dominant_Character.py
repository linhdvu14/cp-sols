''' C. Dominant Character
https://codeforces.com/contest/1605/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(N, S):
	if 'aa' in S: return 2
	if 'aba' in S or 'aca' in S: return 3
	if 'abca' in S or 'acba' in S: return 4
	if 'abbacca' in S or 'accabba' in S: return 7
	return -1


def main():
	T = int(input())
	for _ in range(T):
		N = int(input())
		S = input().decode().strip()
		out = solve(N, S)
		output(f'{out}\n')


if __name__ == '__main__':
	main()

