''' G. Remove Directed Edges
https://codeforces.com/contest/1674/problem/G
'''

import io, os, sys
from tkinter import NE
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') not in [None, '0']

if DEBUG:
    from inspect import currentframe, getframeinfo
    from re import search

def debug(*args):
    if not DEBUG: return
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')


INF = float('inf')

# -----------------------------------------

def toposort_kahn(adj, N):
	in_degree = [0]*N
	for u in range(N):
		for v in adj[u]:
			in_degree[v] += 1

	queue = [u for u in range(N) if in_degree[u] == 0]
	res = []
	while queue:
		u = queue.pop()
		res.append(u)
		for v in adj[u]:
			in_degree[v] -= 1
			if in_degree[v] == 0: queue.append(v)

	if len(res) < N: return [] 
	return res


def main():
    N, M = list(map(int, input().split()))
    
    outdeg = [0] * N
    indeg = [0] * N
    adj = [[] for _ in range(N)]
    for _ in range(M):
        u, v = list(map(int, input().split()))
        outdeg[u-1] += 1
        indeg[v-1] += 1
        adj[u-1].append(v-1)
    
    # dp[u] = longest path ending at u s.t. 
    # * all nodes except first have indeg >= 2
    # * all nodes except last have outdeg >= 2
    dp = [1] * N

    # toposrt
    topo = toposort_kahn(adj, N)
    for u in topo:
        if outdeg[u] >= 2:
            for v in adj[u]:
                if indeg[v] >= 2:
                    dp[v] = max(dp[v], dp[u] + 1)
    
    print(max(dp))


if __name__ == '__main__':
    main()

