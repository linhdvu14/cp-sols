''' E. Gardener and Tree
https://codeforces.com/contest/1593/problem/E
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write


def solve(N, K, edges):
	degree = [0]*N
	adj = [[] for _ in range(N)]
	for u, v in edges:
		degree[u] += 1
		degree[v] += 1
		adj[u].append(v)
		adj[v].append(u)

	removed = [False]*N
	cur = set([u for u in range(N) if degree[u]==1 or degree[u]==0])
	res = N
	for _ in range(K):
		nxt = set([])
		for u in cur:
			if removed[u]: continue
			removed[u] = True
			res -= 1
			for v in adj[u]:
				degree[v] -= 1
				if (degree[v] == 1 or degree[v] == 0) and not removed[v]:
					nxt.add(v)
		cur = nxt
		if not cur: break

	return res


def main():
	T = int(input())
	for _ in range(T):
		_ = input()
		N, K = list(map(int, input().split()))
		edges = []
		for _ in range(N-1):
			u, v = list(map(int, input().split()))
			edges.append((u-1, v-1))
		out = solve(N, K, edges)
		output(str(out) + '\n')


if __name__ == '__main__':
	main()

