''' F - Teleporter Setting
https://atcoder.jp/contests/abc257/tasks/abc257_f
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
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

from heapq import heappush, heappop

# after connecting (v1, ..., vm) to u, shortest path 1..N is one of:
# - 1 -> N: original shortest path, w/o vi or u
# - 1 -> vi -> u -> N
# - 1 -> u -> vi -> N
# - 1 -> vi -> u -> vj -> N 

def main():
    N, M = list(map(int, input().split()))

    free = []
    adj = [[] for _ in range(N)]
    for _ in range(M):
        u, v = list(map(int, input().split()))
        if u == 0: free.append(v-1)
        else:
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
    
    # min dist to 0 and N-1 w/o teleporting
    def djikstra(src):
        dist = [INF] * N
        h = [(0, src)]
        while h:
            d, u = heappop(h)
            if dist[u] <= d: continue
            dist[u] = d
            for v in adj[u]:
                if dist[v] <= d + 1: continue
                heappush(h, (d + 1, v))
        return dist
    
    d0, dn = djikstra(0), djikstra(N-1)
    if not free: return [d0[N-1]] * N if d0[N-1] < INF else [-1] * N
    
    m0 = min(d0[v] for v in free)
    mn = min(dn[v] for v in free)

    res = [-1] * N
    for u in range(N):
        cand = min(
            d0[N-1], 
            m0 + dn[u] + 1,
            d0[u] + mn + 1,
            m0 + mn + 2,
        )
        if cand < INF: res[u] = cand

    return res

    

if __name__ == '__main__':
    res = main()
    print(*res)

