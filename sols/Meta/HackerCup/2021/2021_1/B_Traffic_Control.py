''' Problem B: Traffic Control
https://www.facebook.com/codingcompetitions/hacker-cup/2021/round-1/problems/B
'''


# A M M M B
# 1 M M M 1
# 1 M M M 1
# 1 1 1 1 1
def solve(n, m, a, b):
	a -= m+n-2
	b -= m+n-2
	if a<=0 or b<=0: return False, []

	grid = [[1000]*m for _ in range(n)]

	# last row
	for c in range(m):
		grid[n-1][c] = 1
	
	# first and last col
	for r in range(n):
		grid[r][0] = 1
		grid[r][m-1] = 1

	# start points
	grid[0][0] = a
	grid[0][m-1] = b

	return True, grid


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())
	for t in range(T):
		n, m, a, b = list(map(int, stdin.readline().strip().split()))
		possible, grid = solve(n, m, a, b)
		if possible:
			print('Case #{}: {}'.format(t+1, 'Possible'))
			for row in grid:
				print(' '.join(list(map(str, row))))
		else:
			print('Case #{}: {}'.format(t+1, 'Impossible'))


if __name__ == '__main__':
	main()
