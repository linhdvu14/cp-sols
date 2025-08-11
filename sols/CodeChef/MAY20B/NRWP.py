''' Not a Real World Problem

https://www.codechef.com/MAY20B/problems/NRWP

'''

def min_cut(capacity,src,sink):
	from collections import deque	
	N  = len(capacity)

	def bfs():
		queue = deque([src])
		parents = {src:-1}
		found = False
		while queue:
			u = queue.popleft()
			if u == sink:
				found = True
				break
			for v in range(N):
				if v not in parents and capacity[u][v] > 0:
					parents[v] = u
					queue.append(v)
		return found, parents

	while True:
		found, parents = bfs()
		if not found: break
		
		# trace path to find bottleneck
		mn = float('inf')
		v = sink
		while parents[v] != -1:
			u = parents[v]
			mn = min(mn,capacity[u][v])
			v = u

		# update capacity
		v = sink
		while parents[v] != -1:
			u = parents[v]
			capacity[u][v] -= mn
			capacity[v][u] += mn
			v = u

	# find partition id
	queue = deque([src])
	src_nodes = set([src])
	while queue:
		u = queue.popleft()
		for v in range(N):
			if v not in src_nodes and capacity[u][v] > 0:
				src_nodes.add(v)
				queue.append(v)
	return src_nodes


def solve(nr,nc,grid,particles):
	particles = [(r-1,c-1,x) for r,c,x in particles]
	N = len(particles)
	pos, neg = N, N+1

	capacity = [[0]*(N+2) for _ in range(N+2)]
	for i,(r,c,x) in enumerate(particles):
		if grid[r][c] > 0: capacity[pos][i] = x*grid[r][c]
		if grid[r][c] < 0: capacity[i][neg] = -x*grid[r][c]
		for j in range(i+1,len(particles)):
			rr,cc,xx = particles[j]
			if (r==rr and abs(c-cc)==1) or (c==cc and abs(r-rr)==1): 
				capacity[i][j] = x*xx
				capacity[j][i] = x*xx

	# get sign assignment
	pos_nodes = min_cut(capacity,pos,neg)
	sign = [1 if u in pos_nodes else -1 for u in range(N)]

	# get sum
	res = 0
	for i,(r,c,x) in enumerate(particles):
		res += grid[r][c]*x*sign[i]
		for j in range(i+1,len(particles)):
			rr,cc,xx = particles[j]
			if (r==rr and abs(c-cc)==1) or (c==cc and abs(r-rr)==1):
				res += x*xx*sign[i]*sign[j]
	return res, sign


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for _ in range(T):
		H,W,N = list(map(int,stdin.readline().strip().split()))
		grid = [list(map(int,stdin.readline().strip().split())) for _ in range(H)]
		particles = [list(map(int,stdin.readline().strip().split())) for _ in range(N)]
		res, sign = solve(H,W,grid,particles)
		print(res)
		print(' '.join(map(str,sign)))


if __name__ == '__main__':
	main()