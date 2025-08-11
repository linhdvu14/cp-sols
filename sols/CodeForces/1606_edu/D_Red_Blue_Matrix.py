''' D. Red-Blue Matrix
https://codeforces.com/contest/1606/problem/D
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

if DEBUG:
    from varname.core import argname
    from inspect import currentframe

def debug(var, *more_vars):
    if not DEBUG: return
    var_names = argname('var', '*more_vars', func=debug)
    values = (var, *more_vars)
    name_and_values = [f'{var_name}={value}'  for var_name, value in zip(var_names, values)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(name_and_values)}')


INF = float('inf')

# -----------------------------------------

def solve(R, C, grid):
	# sort all rows by 1st col from small to big
	# then all blue rows on top, all red rows on bottom
	row_idx = sorted(list(range(R)), key=lambda i: grid[i][0])
	grid = [grid[i] for i in row_idx]

	# MAX_UL[r][c] = max val in top left rectangle (0, 0)..(r, c)
	# MIN_DL[r][c] = min val in bottom left rectangle (0, R-1)..(r, c)
	# MIN_UR[r][c] = min val in top right rectangle (r, c)..(0, C-1)
	# MAX_DR[r][c] = max val in bottom right rectangle (r, c)..(R-1, C-1)
	MAX_UL = [[grid[r][c] for c in range(C)] for r in range(R)]
	for r in range(R):
		for c in range(C):
			if r > 0: MAX_UL[r][c] = max(MAX_UL[r][c], MAX_UL[r-1][c])
			if c > 0: MAX_UL[r][c] = max(MAX_UL[r][c], MAX_UL[r][c-1])

	MIN_DL = [[grid[r][c] for c in range(C)] for r in range(R)]
	for r in range(R-1, -1, -1):
		for c in range(C):
			if r < R-1: MIN_DL[r][c] = min(MIN_DL[r][c], MIN_DL[r+1][c])
			if c > 0: MIN_DL[r][c] = min(MIN_DL[r][c], MIN_DL[r][c-1])

	MIN_UR = [[grid[r][c] for c in range(C)] for r in range(R)]
	for r in range(R):
		for c in range(C-1, -1, -1):
			if r > 0: MIN_UR[r][c] = min(MIN_UR[r][c], MIN_UR[r-1][c])
			if c < C-1: MIN_UR[r][c] = min(MIN_UR[r][c], MIN_UR[r][c+1])

	MAX_DR = [[grid[r][c] for c in range(C)] for r in range(R)]
	for r in range(R-1, -1, -1):
		for c in range(C-1, -1, -1):
			if r < R-1: MAX_DR[r][c] = max(MAX_DR[r][c], MAX_DR[r+1][c])
			if c < C-1: MAX_DR[r][c] = max(MAX_DR[r][c], MAX_DR[r][c+1])

	# try each possible cut
	res_r = res_c = -1
	for r in range(R-1):
		for c in range(C-1):
			if MAX_UL[r][c] < MIN_DL[r+1][c] and MIN_UR[r][c+1] > MAX_DR[r+1][c+1]:
				res_r, res_c = r, c
				break

	if res_r == res_c == -1: return 'NO', '', -1
	
	colors = ['R']*R
	for r in range(res_r+1):
		colors[row_idx[r]] = 'B'
	return 'YES', ''.join(colors), res_c+1


def main():
	T = int(input())
	for _ in range(T):
		R, C = list(map(int, input().split()))
		grid = [list(map(int, input().split())) for _ in range(R)]
		r1, r2, r3 = solve(R, C, grid)
		print(r1)
		if r1 == 'YES': print(r2, r3)

if __name__ == '__main__':
	main()

