''' A. Computer Game
https://codeforces.com/contest/1598/problem/A
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(N, grid):
	for i in range(N):
		if grid[0][i] == grid[1][i] == 1: return 'NO\n'
	return 'YES\n'


def main():
	T = int(input())
	for _ in range(T):
		N = int(input())
		grid = []
		for _ in range(2):
			row = list(map(int, list(input().decode().strip())))
			grid.append(row)
		out = solve(N, grid)
		output(out)



if __name__ == '__main__':
	main()

