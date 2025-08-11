''' E2. Rubik's Cube Coloring (hard version)
https://codeforces.com/contest/1594/problem/E2
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

MOD = 10**9 + 7
cmap = {
	'white': 0,
	'blue': 1,
	'red': 2,
	'orange': 3,
	'green': 4,
	'yellow': 5,
}

# Consider the set G of all nodes whose subtree contains a known node, then
# * G is a tree-like subgraph of the original graph
# * nodes in G are constrained
# * nodes not in G are unconstrained (4 color choices)
# Let dp[u][c] = num ways to form a G-subtree at node u s.t. u has color c
# then ans = (SUM_j dp[1][j]) * 4^(num nodes not in G)

def solve(K, N, known):
	G = set()
	color = {}
	for u, c in known:
		color[u] = c
		while u > 0:
			G.add(u)
			u >>= 1

	G = sorted(list(G), reverse=True)
	dp = {}
	for u in G:
		dp[u] = [0]*6
		a, b = 2*u, 2*u+1
		if (a not in dp) & (b not in dp):  # leaf -> known color
			dp[u][color[u]] = 1
		elif (a in dp) ^ (b in dp):        # one child
			if a not in dp: a, b = b, a
			for cu in range(6):
				for ca in range(6):
					if cu==ca or cu+ca==5: continue
					dp[u][cu] += dp[a][ca]
		else:
			for cu in range(6):
				for ca in range(6):
					for cb in range(6):
						if cu==ca or cu+ca==5 or cu==cb or cu+cb==5: continue
						dp[u][cu] += dp[a][ca] * dp[b][cb]
		if u in color:
			for c in range(6):
				if c != color[u]: dp[u][c] = 0

	res = sum(dp[1]) % MOD
	res *= pow(4, 2**K-1 - len(G), MOD)
	res %= MOD
	return res


def main():
	K = int(input().strip())
	N = int(input().strip())
	known = []
	for _ in range(N):
		u, s = input().decode().split()
		known.append((int(u), cmap[s]))
	out = solve(K, N, known)
	output(str(out) + '\n')


if __name__ == '__main__':
	main()
