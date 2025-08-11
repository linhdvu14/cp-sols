''' D. Gargari and Permutations
https://codeforces.com/contest/463/problem/D
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(N, K, perms):
	# make DAG from common ordered pairs
	adj = [[] for _ in range(N)]
	for i in range(N):
		ends = set(perms[0][i+1:])
		for k in range(1, K):
			j = perms[k].index(perms[0][i])
			ends &= set(perms[k][j+1:])		
		for j in ends: adj[perms[0][i]-1].append(j-1)
	
	# D[u] = max dist from u to any other node
	D = [0]*N
	def dfs(u):
		if D[u] > 0: return D[u]
		res = 1
		for v in adj[u]:
			res = max(res, 1 + dfs(v))
		D[u] = res
		return res
	
	for u in range(N):
		if D[u] == 0: dfs(u)
	
	return max(D)



def main():
	N, K = list(map(int, input().split()))
	perms = [list(map(int, input().split())) for _ in range(K)]
	out = solve(N, K, perms)
	output(f'{out}\n')


if __name__ == '__main__':
	main()

