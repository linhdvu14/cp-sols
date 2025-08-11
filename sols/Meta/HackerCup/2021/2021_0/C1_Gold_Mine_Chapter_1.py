''' Problem C1: Gold Mine - Chapter 1
https://www.facebook.com/codingcompetitions/hacker-cup/2021/qualification-round/problems/C1
'''


def solve(vals, conns, N):
	adj = [set() for _ in range(N)]
	for u,v in conns:
		adj[u-1].add(v-1)
		adj[v-1].add(u-1)
	
	def dfs(u, seen=set([0])):  # max val path under subtree u
		res = vals[u]
		seen.add(u)
		child = 0
		for v in adj[u]:
			if v not in seen:
				child = max(child, dfs(v))
		return res + child
	
	cands = [dfs(v) for v in adj[0]]
	if len(cands) == 0: return vals[0]
	if len(cands) == 1: return vals[0] + cands[0]
	cands.sort(reverse=True)
	return vals[0] + cands[0] + cands[1]


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		N = int(stdin.readline().strip())
		vals = list(map(int, stdin.readline().strip().split()))
		conns = [list(map(int, stdin.readline().strip().split())) for _ in range(N-1)]
		out = solve(vals, conns, N)
		print('Case #{}: {}'.format(t+1, out))


def gen():
	class UnionFind:
		def __init__(self, n):
			self.n = n
			self.rank = [1 for _ in range(n)]  # tree height: num elements under one root, including self
			self.parent = [i for i in range(n)]
		
		def find(self, i):  # path compression: connect all parents from i..root to root
			root = i
			while self.parent[root] != root:
				root = self.parent[root]		
			while self.parent[i] != root:
				p = self.parent[i]
				self.parent[i] = root
				i = p
			return root

		def union(self, i, j):  # rank compression: merge small tree to large tree
			rooti, rootj = self.find(i), self.find(j)
			if rooti == rootj: return
			if self.rank[rooti] > self.rank[rootj]:
				rooti, rootj = rootj, rooti
			self.parent[rooti] = rootj
			self.rank[rootj] += self.rank[rooti]
		
	
	import random
	random.seed(12)

	T = 1000
	print(T)
	for _ in range(T):
		N = random.randint(1,50)
		print(N)
		vals = [random.randint(0,20000000) for _ in range(N)]
		print(' '.join(map(str,vals)))
		uf = UnionFind(N)
		edges = set()
		while len(edges) < N-1:
			u = random.randint(0,N-1)
			v = random.randint(0,N-1)
			ru, rv = uf.find(u), uf.find(v)
			if ru != rv:
				edges.add((u,v))
				uf.union(u,v)
		for u,v in edges:
			print(f'{u+1} {v+1}')



if __name__ == '__main__':
	# gen()
	main()