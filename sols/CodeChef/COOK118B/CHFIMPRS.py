''' Impressing Chefina

https://www.codechef.com/COOK118B/problems/CHFIMPRS

'''

def solve(grid):
	nr, nc = len(grid), len(grid[0])
	counts = {}
	for row in grid:
		for v in row:
			if v not in counts: counts[v] = 0
			counts[v] += 1
	
	odd, even = [], []
	for k,v in counts.items():
		if v&1: 
			odd.append(k)
		else:
			even.append(k)

	if len(odd) > nr: return [[-1]]
	if nc%2==0 and odd: return [[-1]]
	if nc%2==1 and (nr-len(odd))%2==1: return [[-1]]

	if nc%2 == 1:
		r = 0
		while r < nr:
			if odd:
				v = odd.pop()
				grid[r][nc//2] = v
				counts[v] -= 1
				if counts[v]: even.append(v)
				r += 1
			else:
				v = even[-1]
				grid[r][nc//2] = grid[r+1][nc//2] = v
				counts[v] -= 2
				if not counts[v]: even.pop()
				r += 2

	for r in range(nr):
		for c in range(nc//2):
			v = even[-1]
			grid[r][c] = grid[r][-1-c] = v
			counts[v] -= 2
			if not counts[v]: even.pop()

	return grid



def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())
	for _ in range(T):
		N,M = list(map(int,stdin.readline().strip().split()))
		grid = [list(map(int,stdin.readline().strip().split())) for _ in range(N)]
		rgrid = solve(grid)
		for row in rgrid: print(' '.join(map(str,row)))




if __name__ == '__main__':
	main()

