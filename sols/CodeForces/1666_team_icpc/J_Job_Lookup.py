''' J. Job Lookup
https://codeforces.com/contest/1666/problem/J
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

def main():
    N = int(input())
    C = [list(map(int, input().split())) for _ in range(N)]

    # pref[i+1][j+1] = SUM of rectangle (0, 0)..(i, j) of matrix C
    pref = [[0] * (N+1) for _ in range(N+1)]
    for r in range(N): 
        for c in range(N):
            pref[r+1][c+1] = pref[r+1][c] + pref[r][c+1] - pref[r][c] + C[r][c]

    # sum c(u, v) for u in l..r and v not in l..r
    def get_cost(l, r): 
        res = pref[r+1][N] - pref[l][N]
        res -= pref[r+1][r+1] - pref[r+1][l] - pref[l][r+1] + pref[l][l]
        return res

    # each edge lying on shortest path between (u, v) contributes c(u, v) to total cost
    # dp[l..r] = min contribution of all edges in a bst covering nodes l..r
    dp = [[INF] * N for _ in range(N)]
    for i in range(N): dp[i][i] = 0

    # to build min cost tree over l..r, try to root at each k=l..r
    # cost for subtrees l..k-1, k+1..r do not depend on ancestor splits, so can be optimized independently
    # -> dp[l..r] = min_k (dp[l..k-1] + dp[k+1..r] + cost of connecting k to l..k-1 + cost of connecting k to k+1..r)
    # cost of connecting k to l..k-1 = sum c(u, v) for u in l..k-1 and v not in l..k-1
    split = [list(range(N)) for _ in range(N)]
    for ln in range(1, N):
        for i in range(N-ln):
            j = i + ln
            for k in range(i, j+1):
                l = r = 0
                if i <= k-1: l = dp[i][k-1] + get_cost(i, k-1)
                if k+1 <= j: r = dp[k+1][j] + get_cost(k+1, j)
                if l + r < dp[i][j]:
                    dp[i][j] = l + r
                    split[i][j] = k
    
    # trace 
    par = [0] * N
    queue = deque([(0, N-1, -1)])
    while queue:
        l, r, p = queue.popleft()
        k = split[l][r]
        par[k] = p + 1
        if l <= k-1: queue.append((l, k-1, k))
        if k+1 <= r: queue.append((k+1, r, k))
    
    print(*par)


if __name__ == '__main__':
    main()

