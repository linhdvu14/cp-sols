''' Sorting Vases

https://www.codechef.com/MAY20B/problems/SORTVS

'''

class UnionFind:
	def __init__(self, n):
		self.size = [1 for _ in range(n)]
		self.parent = [i for i in range(n)]
	
	def find(self, i):
		while self.parent[i] != self.parent[self.parent[i]]:
			self.parent[i] = self.parent[self.parent[i]]
		return self.parent[i]

	def union(self, i, j):
		rooti, rootj = self.find(i), self.find(j)
		if rooti == rootj: return
		if self.size[rooti] > self.size[rootj]:
			rooti, rootj = rootj, rooti
		self.parent[rooti] = rootj
		self.size[rootj] += self.size[rooti]


def solve(N,M,nums,pairs):
	nums = [n-1 for n in nums]
	pairs = [[x-1,y-1] for x,y in pairs]

	# find group ID
	uf = UnionFind(N)
	for x,y in pairs: uf.union(x,y)
	group = [uf.find(i) for i in range(N)]

	# sort to 1-N
	res = N*N
	def valid(val,i): return group[i] == group[val]
	def swap(i,j): nums[i],nums[j] = nums[j],nums[i]
	def search(i,cnt):
		nonlocal res
		if i >= N-1:
			res = min(res,cnt)
			return
		if valid(nums[i],i):
			search(i+1,cnt)
			return
		for j in range(i+1,N):
			if valid(nums[j],i):
				swap(i,j)
				search(i+1,cnt+1)
				swap(i,j)
	
	search(0,0)
	return res


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())
	for _ in range(T):
		N,M = list(map(int,stdin.readline().strip().split()))
		nums = list(map(int,stdin.readline().strip().split()))
		pairs = [list(map(int,stdin.readline().strip().split())) for _ in range(M)]
		out = solve(N,M,nums,pairs)
		print(out)


if __name__ == '__main__':
	main()

