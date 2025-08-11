''' E - Small d and k
https://atcoder.jp/contests/abc254/tasks/abc254_e
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
    N, M = list(map(int, input().split()))
    adj = [[] for _ in range(N)]
    for _ in range(M):
        u, v = list(map(int, input().split()))
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    
    Q = int(input())
    queries = []
    for i in range(Q):
        x, k = list(map(int, input().split()))
        queries.append((x-1, k, i))
    queries.sort()

    res = [-1] * Q
    prev_x = dp = None
    for x, k, i in queries:
        if not prev_x or x != prev_x:
            dp = [0] * 4
            queue = deque([(x, 0)])
            seen = set([x])
            while queue:
                u, d = queue.popleft()
                dp[d] += u + 1
                if d == 3: continue
                for v in adj[u]:
                    if v in seen: continue
                    seen.add(v)
                    queue.append((v, d + 1))
            prev_x = x
        res[i] = sum(dp[j] for j in range(k + 1))

    print(*res, sep='\n')



if __name__ == '__main__':
    main()

