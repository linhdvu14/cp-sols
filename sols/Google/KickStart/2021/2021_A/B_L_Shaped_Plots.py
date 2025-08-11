''' L Shaped Plots 
https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068c509
'''
def solve(nr,nc,grid):
	# max num contiguous ones from grid[r][c]
	up = [[0]*nc for _ in range(nr)]
	down = [[0]*nc for _ in range(nr)]
	left = [[0]*nc for _ in range(nr)]
	right = [[0]*nc for _ in range(nr)]

	for r in range(nr):
		for c in range(nc):
			if grid[r][c] == 0: continue
			up[r][c] = 1 + up[r-1][c] if r>0 else 1
			left[r][c] = 1 + left[r][c-1] if c>0 else 1

	for r in range(nr-1,-1,-1):
		for c in range(nc-1,-1,-1):
			if grid[r][c] == 0: continue
			down[r][c] = 1 + down[r+1][c] if r<nr-1 else 1
			right[r][c] = 1 + right[r][c+1] if c<nc-1 else 1

	res = 0
	for r in range(nr):
		for c in range(nc):
			numu,numd,numl,numr = up[r][c],down[r][c],left[r][c],right[r][c]
			for x,y in [(numu,numl),(numu,numr),(numd,numl),(numd,numr)]:
				res += max(0,min(x//2,y)-1) + max(0,min(y//2,x)-1)

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