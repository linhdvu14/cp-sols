''' D. Social Network
https://codeforces.com/contest/1609/problem/D
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

INF = float('inf')

class UnionFind:
	def __init__(self, N):
		self.N = N
		self.rank = [1 for _ in range(N)]  # for root nodes, height of tree rooted at this node
		self.parent = [i for i in range(N)]
	
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
	
	def get_cc_sizes(self):
		groups = [[] for _ in range(self.N)]
		for i in range(self.N):
			r = self.find(i)
			groups[r].append(i)
		return sorted([len(g) for g in groups if g], reverse=True)


def solve(N, D, edges):
	uf = UnionFind(N)
	sz = 1  # free edges

	for x, y in edges:
		if uf.find(x-1) == uf.find(y-1):
			sz += 1
		else:
			uf.union(x-1, y-1)
		sizes = uf.get_cc_sizes()
		res = sum(sizes[:sz]) - 1
		print(res)


def main():
	N, D = list(map(int, input().split()))
	edges = [list(map(int, input().split())) for _ in range(D)]
	solve(N, D, edges)


if __name__ == '__main__':
	main()

