''' Square Dance
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd74/00000000002b1355
'''

def solve(grid,nr,nc):
	UP,DOWN,LEFT,RIGHT,VAL,ID = 0,1,2,3,4,5
	def idx(r,c): return r*nc+c
	curr = [[None,None,None,None,None,i] for i in range(nr*nc)]  # remaining contestants

	for r in range(nr):
		for c in range(nc):
			curr[idx(r,c)][VAL] = grid[r][c]

	for r in range(nr):
		for c in range(nc-1):
			left, right = idx(r,c), idx(r,c+1)
			curr[left][RIGHT] = curr[right]
			curr[right][LEFT] = curr[left]

	for r in range(nr-1):
		for c in range(nc):
			up, down = idx(r,c), idx(r+1,c)
			curr[up][DOWN] = curr[down]
			curr[down][UP] = curr[up]

	out = 0
	s = sum(sum(row) for row in grid)
	while curr:
		out += s

		killed = set()
		for node in curr:
			tot = cnt = 0
			for d in range(4):  # direction
				if node[d]: 
					tot += node[d][VAL]
					cnt += 1
			if cnt and node[VAL] * cnt < tot:
				killed.add(node[ID])
				s -= node[VAL]

		if not killed: break

		nxt = []
		seen = set([i for i in killed])
		for node in curr:
			if node[ID] not in killed: continue
			for d in range(4):
				fwd, bwd = node[d], node[d^1]
				if fwd: 
					fwd[d^1] = bwd
					if fwd[ID] not in seen:
						nxt.append(fwd)
						seen.add(fwd[ID])
				if bwd: 
					bwd[d] = fwd
					if bwd[ID] not in seen:
						nxt.append(bwd)
						seen.add(bwd[ID])

		curr = nxt

	return out



def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		nr,nc = list(map(int,stdin.readline().strip().split()))
		grid = []
		for _ in range(nr):
			grid.append(list(map(int,stdin.readline().strip().split())))
		out = solve(grid,nr,nc)
		print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
	main()