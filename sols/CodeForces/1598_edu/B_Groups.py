''' B. Groups
https://codeforces.com/contest/1598/problem/B
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(N, grid):
	for a in range(5):
		for b in range(a+1, 5):
			ca = cb = cab = 0
			for i in range(N):
				if grid[i][a]: ca += 1
				if grid[i][b]: cb += 1
				if grid[i][a] or grid[i][b]: cab +=1
			if cab == N and ca >= N//2 and cb >= N//2:
				return 'YES\n'
	return 'NO\n'


def main():
	T = int(input())
	for _ in range(T):
		N = int(input())
		grid = [list(map(int, input().split())) for _ in range(N)]
		out = solve(N, grid)
		output(out)


if __name__ == '__main__':
	main()

