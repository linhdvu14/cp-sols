''' G - Builder Takahashi
https://atcoder.jp/contests/abc239/tasks/abc239_g
'''

import io, os, sys
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

from collections import deque	

def max_flow(N, capacity, src, tar):
    '''
    N = num nodes
    capacity[u][v] = capacity of directed edge (u, v)
    src, tar: node id
    returns: max flow, residual_capacity
    time O(V E^2)
    '''
    residual_capacity = [row[:] for row in capacity]

    # undirected edges
    adj = [[] for _ in range(N)]
    for u in range(N):
        for v in range(N):
            if capacity[u][v] == 0: continue
            adj[u].append(v)
            adj[v].append(u)
    
    def bfs(src, tar):
        '''
        find augmenting path (bottleneck flow > 0) from src to tar
        returns: min flow of aug path; par of aug path
        '''
        par = [-1] * N
        par[src] = -2
        queue = deque([(src, INF)])

        while queue:
            u, flow = queue.popleft()
            for v in adj[u]:
                if par[v] != -1 or residual_capacity[u][v] == 0: continue
                par[v] = u
                new_flow = min(flow, residual_capacity[u][v])
                if v == tar: return new_flow, par
                queue.append((v, new_flow))
        
        return 0, par

    max_flow = 0
    while True:
        add, par = bfs(src, tar)
        if add == 0: break
        max_flow += add
        v = tar
        while v != src:
            u = par[v]
            residual_capacity[u][v] -= add
            residual_capacity[v][u] += add
            v = u

    return max_flow, residual_capacity


def find_min_cut_partition(N, residual_capacity, src):
    '''
    given residual capacity after max flow algo
    find min-cut s-t node partitioning
    '''
    queue = deque([src])
    src_nodes = {src}
    while queue:
        u = queue.popleft()
        for v in range(N):
            if v in src_nodes or residual_capacity[u][v] == 0: continue
            src_nodes.add(v)
            queue.append(v)
    tar_nodes = set(u for u in range(N) if u not in src_nodes)
    return src_nodes, tar_nodes


def find_min_cut_edges(src_nodes, tar_nodes, capacity):
	'''
	given s-t partition and original capacity
	find set of min-cut edges
	'''
	res = []
	for s in src_nodes:
		for t in tar_nodes:
			if 0 < capacity[s][t] < INF:
				res.append((s, t))
	return res


# change node u into 2 nodes: u_in, u_out
# change edge (u, v) into (u_out, v_in), (v_out, u_in)
# capacity(u_in, u_out) = cost(u)
# capacity(u_out, v_in) = capacity(v_out, u_in) = INF
# set src = 1_out, sink = N_in
# need to disconnect S, T by cutting min cost set of (u_in, u_out)

def main():
    N, M = list(map(int, input().split()))

    capacity = [[0]*2*N for _ in range(2*N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        capacity[2*u+1][2*v] = INF
        capacity[2*v+1][2*u] = INF
        
    C = list(map(int, input().split()))
    for u, c in enumerate(C):
        if u == 0 or u == N-1: capacity[2*u][2*u+1] = INF
        else: capacity[2*u][2*u+1] = c
    
    flow, residual_capacity = max_flow(2*N, capacity, 0, 2*N-1)
    s_nodes, t_nodes = find_min_cut_partition(2*N, residual_capacity, 0)
    cut_edges = find_min_cut_edges(s_nodes, t_nodes, capacity)
    cut_nodes = set(u//2 + 1 for u, _ in cut_edges if u // 2 != 0)
    print(flow)
    print(len(cut_nodes))
    print(*cut_nodes)



if __name__ == '__main__':
    main()

