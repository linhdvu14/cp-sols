''' Yet Another Contest 2 P4 - No More Arithmetic
https://dmoj.ca/problem/yac2p4
'''

import os, sys
input = sys.stdin.readline  # strip() if str

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

def get_weight(a, b, M):
    if a < b: a, b = b, a
    w = max((a + b) % M, (a - b) % M, (a * b) % M)
    if a % b == 0: w = max(w, (a // b) % M)
    return w

# mst
# for ml: use python3, dense prim (instead of kruskal)
def main():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))

    dist = [-INF for _ in range(N)]
    dist[0] = 0
    used = [0] * N
    res = 0

    for _ in range(N):
        u = -1
        for v in range(N):
            if not used[v] and (u == -1 or dist[v] > dist[u]):
                u = v

        used[u] = 1
        res += dist[u]

        for v in range(N):
            dist[v] = max(dist[v], get_weight(A[u], A[v], M))

    print(res)


if __name__ == '__main__':
    main()