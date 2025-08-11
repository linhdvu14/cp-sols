''' E - Skiing
https://atcoder.jp/contests/abc237/tasks/abc237_e
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

# https://codeforces.com/blog/entry/95823
# w(u -> v) = 2(H[v] - H[u]) if H[u] < H[v]
#          or H[v] - H[u] < 0 if H[u] > H[v]
# let potential p(u) = H(u)
# then w(u -> v) = H[v] - H[u] > 0 if H[u] < H[v]
#               or 0 if H[u] > H[v]

def main():
    N, M = list(map(int, input().split()))
    H = list(map(int, input().split()))

    adj = [[] for _ in range(N)]
    for _ in range(M):
        u, v = list(map(int, input().split()))
        d = H[v-1] - H[u-1]
        adj[u-1].append((v-1, max(d, 0)))
        adj[v-1].append((u-1, max(-d, 0)))
    
    dist = [INF] * N
    dist[0] = 0
    h = []
    for v, d in adj[0]: heappush(h, (d, v))
    while h:
        d, u = heappop(h)
        if dist[u] < INF: continue
        dist[u] = d
        for v, d2 in adj[u]:
            if dist[v] < INF: continue
            heappush(h, (d+d2, v))

    for u in range(N): dist[u] -= H[0] - H[u]
    print(-min(dist))


if __name__ == '__main__':
    main()

