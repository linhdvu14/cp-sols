''' Stable Wall
https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/00000000003379bb
'''

class Graph:
	def __init__(self, nodes, edges):
		self.N = len(nodes)
		self.in2out = {i:n for i,n in enumerate(nodes)}
		self.out2in = {n:i for i,n in enumerate(nodes)}
		self.edges = {i:[] for i in range(self.N)}  # u -> adjacent v
		for (u, v) in edges: 
			self.edges[self.out2in[u]].append(self.out2in[v])

	def toposort(self):
		in_degree = [0]*self.N
		for u in range(self.N):
			for v in self.edges[u]:
				in_degree[v] += 1

		queue = [u for u in range(self.N) if in_degree[u] == 0]
		res = []
		while queue:
			u = queue.pop()
			res.append(u)
			for v in self.edges[u]:
				in_degree[v] -= 1
				if in_degree[v] == 0: queue.append(v)

		if len(res) == self.N:
			return False, [self.in2out[u] for u in res]
		return True, []


def solve(R,C,grid):
	nodes = set([v for row in grid for v in row])
	edges = set()
	for r in range(R-1):
		for c in range(C):
			top,bot = grid[r][c], grid[r+1][c]
			if top == bot: continue
			if (top,bot) in edges: return -1
			edges.add((bot,top))  # bot must be placed before top

	if len(edges) == 0: return ''.join(list(nodes))

	graph = Graph(list(nodes),list(edges))
	has_cycle, order = graph.toposort()
	if has_cycle: return -1
	return ''.join(order)



def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		R,C = list(map(int,stdin.readline().strip().split()))
		grid = [stdin.readline().strip() for _ in range(R)]
		out = solve(R,C,grid)
		print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
	main()
