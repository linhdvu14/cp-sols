''' D. Treelabeling
https://codeforces.com/contest/1605/problem/D
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

# for any edge (u, v), want u and v to have different msb
# partition nodes by even/odd level, then:
# * there's no edge within same partition
# * the smaller partition has different msb from N
# partition labels by msb: 1 | 2 3 4 | 5 6 7 | 8 9 ...
# ---> want to assign msb partitions into 2 node partitions
def solve(N, edges):
	adj = [[] for _ in range(N+1)]
	for u, v in edges:
		adj[u].append(v)
		adj[v].append(u)
	
	# partition nodes
	parts = [[], []]
	seen = [False]*(N+1)
	seen[1] = True
	stack = [(1, 0)]
	while stack:
		u, depth = stack.pop()
		parts[depth % 2].append(u)
		for v in adj[u]:
			if seen[v]: continue
			seen[v] = True
			stack.append((v, depth+1))
	
	# find smaller partition
	small, big = parts[0], parts[1]
	if len(small) > len(big): small, big = big, small
	M = len(small)
	
	# assign labels
	# note msb(cnt) != msb(N) and all possible labels with msb=1..msb(N)-1 are available
	res = [0]*(N+1)
	for i in range(32):
		in_small = (M >> i) & 1 > 0
		lo, hi = 1 << i, min((1 << (i+1)) - 1, N)
		if lo > N: break
		for i in range(lo, hi+1):
			b = small.pop() if in_small else big.pop()
			res[b] = i

	print(' '.join(map(str, res[1:])))


def main():
	T = int(input())
	for _ in range(T):
		N = int(input())
		edges = [tuple(map(int, input().split())) for _ in range(N-1)]
		solve(N, edges)


if __name__ == '__main__':
	main()

