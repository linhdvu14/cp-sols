''' D. Tenzing and His Animal Friends
https://codeforces.com/contest/1842/problem/D
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
from heapq import heappush, heappop


# iteratively kill node with min remain time
def solve_1(N, M, edges):
    adj = [[] for _ in range(N)]
    for u, v, w in edges:
        u -= 1; v -= 1
        adj[u].append([v, w])
        adj[v].append([u, w])

    alive = [1] * N
    dead_since = [-1] * N
    time = 0
    ops = []

    rm = (0, 1 - N)
    while len(ops) < N * N:
        rmt, rmu = rm; rmu = -rmu

        time += rmt 
        dead_since[rmu] = time 
        if rmt: ops.append([''.join(map(str, alive)), rmt])
        alive[rmu] = 0
        
        if not rmu: return time, ops 

        rm = (INF, INF)
        for u in range(N):
            if not alive[u]: continue 
            for v, t in adj[u]:
                if not alive[v]: 
                    rm = min(rm, (t - time + dead_since[v], -u))
        if rm == (INF, INF): break

    return INF, []


# can select u at most dist(u, N) time
def solve_2(N, M, edges):
    adj = [[] for _ in range(N)]
    for u, v, w in edges:
        u -= 1; v -= 1
        adj[u].append([v, w])
        adj[v].append([u, w])
    
    dist = [INF] * N
    dist[N - 1] = 0
    h = [(0, N - 1)]
    ops = []
    while h:
        d, u = heappop(h)
        if dist[u] < d: continue
        ops.append(u)
        if u == 0: break
        for v, w in adj[u]:
            if dist[v] <= d + w: continue
            dist[v] = d + w
            heappush(h, (d + w, v))
    
    if dist[0] is INF: return INF, []
    
    res = []
    mask = [1] * N; mask[N - 1] = 0
    for i in range(1, len(ops)):
        t = dist[ops[i]] - dist[ops[i - 1]]
        if t: res.append([''.join(map(str, mask)), t])
        mask[ops[i]] = 0
    
    return dist[0], res


solve = solve_2

def main():
    N, M = list(map(int, input().split()))
    edges = [list(map(int, input().split())) for _ in range(M)]
    tot, ops = solve(N, M, edges)
    if tot is INF:
        print(tot)
    else:
        print(tot, len(ops))
        for o in ops: print(*o)


if __name__ == '__main__':
    main()
    # gen()
