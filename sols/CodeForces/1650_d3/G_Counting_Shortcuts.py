''' G. Counting Shortcuts
https://codeforces.com/contest/1650/problem/G
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

MOD = 10**9 + 7

from collections import deque

def solve(N, S, T, edges):
    S, T = S-1, T-1
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)

    # each ele put on queue at most twice: during shortest path from s, and during shortest path from s + 1
    # dp[0][u] = num ways to go from s to u s.t. dist(s, u) is min
    # dp[1][u] = num ways to go from s to u s.t. dist(s, u) is min dist(s, u) + 1
    # dist[u] = min dist from s to u
    # cnt[u] = num times u has been put on queue
    dp = [[0]*N, [0]*N]
    dist = [INF] * N
    cnt = [0] * N

    res = 0
    dp[0][S] = 1
    dist[S] = 0
    cnt[S] = 1
    queue = deque([(S, 0, 0)])  # (node, dist from s, visit time)
    while queue:
        u, d, t = queue.popleft()
        if u == T: res = (res + dp[t][u]) % MOD
        if d >= dist[T] + 1: continue
        for v in adj[u]:
            if d > dist[v]: continue
            dist[v] = min(dist[v], d+1)
            dp[d+1-dist[v]][v] = (dp[d+1-dist[v]][v] + dp[t][u]) % MOD
            if cnt[v] == 0 or (cnt[v] == 1 and d == dist[v]):
                queue.append((v, d+1, cnt[v]))
                cnt[v] += 1
    return res


def main():
    T = int(input())
    for _ in range(T):
        _ = input()
        N, M = list(map(int, input().split()))
        S, T = list(map(int, input().split()))
        edges = [list(map(int, input().split())) for _ in range(M)]
        out = solve(N, S, T, edges)
        print(out)


if __name__ == '__main__':
    main()

