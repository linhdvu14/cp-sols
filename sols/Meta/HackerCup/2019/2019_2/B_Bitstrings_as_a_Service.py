''' Problem B: Bitstrings as a Service
https://www.facebook.com/codingcompetitions/hacker-cup/2019/round-2/problems/B
'''

# max recusion depth exceeded with memo, dfs (union find)

class UnionFind:
	def __init__(self, n):
		self.n = n
		self.rank = [1 for _ in range(n)]  # for root nodes, height of tree rooted at this node
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


def solve(N, M, intervals):
    # endpoint sum -> min start point
    intervalSum = {}  
    for x,y in intervals:
        intervalSum[x+y-2] = min(x-1, intervalSum.get(x+y-2,N))

    # what index groups are equal
    # (i,j) equal <-> x-i-j-y <-> i+j = x+y and i >=x
    uf = UnionFind(N)
    for i in range(N):
        for j in range(i+1,N):
            if i >= intervalSum.get(i+j,N): 
                uf.union(i, j)
    groups = {}
    for i in range(N):
        p = uf.find(i)
        if p not in groups: groups[p] = []
        groups[p].append(i)
    groups = list(groups.values())
    
    # split into 2 approximately equal partitions
    # dp[i][s] = whether possible to make sum s using sizes[0..i]
    sizes = [len(g) for g in groups]
    dp = [[False]*(N+1) for _ in range(len(sizes))]
    for i in range(len(sizes)):
        dp[i][0] = True
    dp[0][sizes[0]] = True

    for i in range(1,len(sizes)):
        for s in range(1,N+1):
            dp[i][s] = dp[i-1][s]
            if s >= sizes[i]: 
                dp[i][s] = dp[i][s] or dp[i-1][s-sizes[i]]

    # trace
    for s in range(sum(sizes)//2,-1,-1):
        if dp[len(sizes)-1][s]:
            idx = []
            for i in range(len(sizes)-1,0,-1):  
                if not dp[i-1][s]:
                    idx.append(i)
                    s -= sizes[i]
            if s: idx.append(0)
            break

    # build
    res = [0]*N
    for i in idx:
        for j in groups[i]:
            res[j] = 1

    return ''.join(map(str, res))



def main():
    from sys import stdin
    
    T = int(stdin.readline().strip())
    for t in range(T):
        N, M = list(map(int, stdin.readline().strip().split()))
        intervals = [tuple(map(int, stdin.readline().strip().split())) for _ in range(M)]
        out = solve(N, M, intervals)
        print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
    main()
