''' D. A Wide, Wide Graph
https://codeforces.com/contest/1805/problem/D
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def debug(*args):   
    if os.environ.get('debug') in [None, '0']: return
    from inspect import currentframe, getframeinfo
    from re import search
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

def solve(N, edges):
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)
    
    def bfs(u):
        dist = [INF] * N 
        dist[u] = 0
        queue = deque([u])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if dist[v] < INF: continue
                dist[v] = dist[u] + 1
                queue.append(v)
        return dist, max((d, u) for u, d in enumerate(dist))[1]

    # tree diameter
    _, x = bfs(0)
    dx, y = bfs(x)
    dy, _ = bfs(y)

    # u connected if max(dx[u], dy[u]) >= k
    diff = [0] * (N + 1)
    for u in range(N): diff[max(dx[u], dy[u])] += 1

    res = [-1] * N
    cnt = N
    for k in range(N, 0, -1):
        cnt -= diff[k]
        res[k - 1] = min(cnt + 1, N)

    return res


def main():
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N - 1)]
    res = solve(N, edges)
    print(*res)


if __name__ == '__main__':
    main()

