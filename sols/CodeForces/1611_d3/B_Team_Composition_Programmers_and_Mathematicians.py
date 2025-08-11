''' B. Team Composition: Programmers and Mathematicians
https://codeforces.com/contest/1611/problem/B
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write


def solve(a, b):
	if a < b: a, b = b, a
	t = min((a-b)//2, a//3, b)
	a -= t*3
	b -= t
	return t + min(a, b) // 2

def main():
	T = int(input())
	for _ in range(T):
		a, b = list(map(int, input().split()))
		out = solve(a, b)
		output(f'{out}\n')


if __name__ == '__main__':
	main()

