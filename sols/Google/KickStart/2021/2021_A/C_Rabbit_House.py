''' Rabbit House 
https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068cb14
'''
def solve(nr,nc,grid):
	hmap = {}
	for r in range(nr):
		for c in range(nc):
			if grid[r][c] not in hmap: hmap[grid[r][c]] = set()
			hmap[grid[r][c]].add((r,c))

	res = 0
	h = max(hmap.keys())
	cur = hmap[h]
	while cur:
		h -= 1
		nxt = hmap[h] if h in hmap else set()
		for r,c in cur:
			for rr,cc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
				if not (0<=rr<nr and 0<=cc<nc): continue
				if grid[rr][cc] > h: continue
				res += h - grid[rr][cc]
				grid[rr][cc] = h
				nxt.add((rr,cc))
		cur = nxt
	return res

def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		nr,nc = list(map(int,stdin.readline().strip().split()))
		grid = []
		for _ in range(nr):
			grid.append(list(map(int,stdin.readline().strip().split())))
		out = solve(nr,nc,grid)
		print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
	main()