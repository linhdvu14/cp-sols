''' E. Keshi in Search of AmShZ
https://codeforces.com/contest/1694/problem/E
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

# for int dict key
from random import randrange
RAND = randrange(1 << 62)
def conv(x): return x ^ RAND

INF = float('inf')

# -----------------------------------------

# https://codeforces.com/blog/entry/103952?#comment-923706
# consider reverse-edge graph
# let dist[u] = min ops to reach u from n ---> want dist[1]
# edge_weight(u -> v) = 1 + count(t s.t. there's edge t -> v and dist[t] > dist[u])
# i.e. 1 op to move, count(.) ops to block all worse roads

from heapq import heappush, heappop

def main():
    N, M = list(map(int, input().split()))
    adj = [[] for _ in range(N)]
    deg = [0] * N
    for _ in range(M):
        u, v = list(map(int, input().split()))
        adj[v-1].append(u-1)
        deg[u-1] += 1  # to track count(t)

    dist = [INF] * N
    h = []
    heappush(h, (0, N-1))
    while h:
        d, u = heappop(h)
        if dist[u] < INF: continue
        dist[u] = d
        for v in adj[u]:
            deg[v] -= 1
            heappush(h, (d + 1 + deg[v], v))
    
    print(dist[0])
            

if __name__ == '__main__':
    main()

