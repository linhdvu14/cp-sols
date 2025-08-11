''' D. The Number of Imposters
https://codeforces.com/contest/1594/problem/D
'''

import sys
input = sys.stdin.readline
output = print


def solve(N, M, cmts):
	# connect each same/opposite node pairs
	adj = [set() for _ in range(N)]
	for u, v, same in cmts:
		adj[u].add((v, same))
		adj[v].add((u, same))

	# check if each cc is bipartite
	# if it is, take larger partition as impostors
	res = 0
	color = [-1]*N
	for u in range(N):
		if color[u] != -1: continue
		color[u] = 0
		sizes = [1, 0]  # num nodes with each color
		stack = [u]
		while stack:
			u = stack.pop()
			for v, same in adj[u]:
				if color[v] == -1:
					color[v] = color[u] if same else 1-color[u]
					sizes[color[v]] += 1
					stack.append(v)
					continue
				if same and color[v] != color[u]: return -1
				if not same and color[v] == color[u]: return -1
		res += max(sizes)
	
	return res


def main():
	T = int(input())
	for _ in range(T):
		N, M = list(map(int, input().split()))
		cmts = []
		for _ in range(M):
			i, j, c = input().strip().split()
			cmts.append((int(i)-1, int(j)-1, c=='crewmate'))
		out = solve(N, M, cmts)
		output(out)


if __name__ == '__main__':
	main()

