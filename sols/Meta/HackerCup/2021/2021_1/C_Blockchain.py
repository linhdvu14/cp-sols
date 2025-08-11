''' Problem C: Blockchain
https://www.facebook.com/codingcompetitions/hacker-cup/2021/round-1/problems/C
'''

import gc, resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))
sys.setrecursionlimit(10**6)

MOD = 10**9 + 7

def solve(N, edges):
	# adj list
	adj = [[] for _ in range(N)]
	for u,v,w in edges:
		adj[u-1].append((v-1,w))
		adj[v-1].append((u-1,w))

	# down[u][c] = num nodes v in u's subtree (excluding u) s.t. capacity(u,v) == c
	# dfs children -> parent
	down = {u:[0]*21 for u in range(N)}
	def dfs_down(u, parent=-1):
		for v,w in adj[u]:			
			if v == parent: continue			
			dfs_down(v, u)

			# v -> u
			down[u][w] += 1

			# child(v) -> u
			for ww in range(1,21):
				if ww < w:
					down[u][ww] += down[v][ww]
				else:
					down[u][w] += down[v][ww]
	dfs_down(0)

	# up[u][c] = num nodes v not in u's subtree (excluding u) s.t. capacity(u,v) == c
	# dfs parent -> children
	up = {u:[0]*21 for u in range(N)}
	def dfs_up(u, parent=-1):
		for v,w in adj[u]:
			if v == parent: continue

			# u -> v
			up[v][w] += 1
			
			# par(u) -> v
			for ww in range(1,21):   
				if ww < w:
					up[v][ww] += up[u][ww]
				else:
					up[v][w] += up[u][ww] 

			# sibling(v) -> v
			for ww in range(1,21):
				if ww < w:
					up[v][ww] += down[u][ww] - down[v][ww]
				else:
					up[v][w] += down[u][ww] - down[v][ww]
			up[v][w] -= 1
			dfs_up(v, u)
	dfs_up(0) 

	# total capacity if no roads disrupted
	total = 0
	for u in range(N):
		for w in range(1, 21):
			total += w * (down[u][w] + up[u][w])
	total = (total // 2) % MOD
	
	# rm each edge
	prod = 1
	stack = [(0, -1)]
	while stack:
		u, parent = stack.pop()
		for v, w in adj[u]:
			if v == parent: continue
			stack.append((v,u))
			drop = 0
			for w1 in range(1,w+1):       # disconnect par(v)-v (including par(v)=u)
				drop += w1 * up[v][w1]
				for w2 in range(1,21):   # disconnect par(v)-child(v) (including par(v)=u))
					drop += min(w1, w2) * up[v][w1] * down[v][w2]
					drop %= MOD
			rem = (total - drop + MOD) % MOD
			prod = (prod*rem) % MOD
	
	return prod


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())
	for t in range(T):
		N = int(stdin.readline().strip())
		edges = [tuple(map(int, stdin.readline().strip().split())) for _ in range(N-1)]
		out = solve(N, edges)
		print('Case #{}: {}'.format(t+1, out))
		gc.collect()


if __name__ == '__main__':
	main()
