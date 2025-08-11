''' E. Monsters
https://codeforces.com/contest/1810/problem/E
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

# https://codeforces.com/blog/entry/114521?#comment-1018275
def solve(N, M, A, edges):
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)

    def expand(src):
        h = [(A[src], src)]
        sz = 0
        seen = {src}
        while h and h[0][0] <= sz:
            _, u = heappop(h)
            won[u] = 1
            sz += 1
            for v in adj[u]:
                if v not in seen:
                    heappush(h, (A[v], v))
                    seen.add(v)
        return sz == N
    
    won = [0] * N 
    for u in range(N):
        if won[u] or A[u]: continue
        if expand(u): return 'YES'

    return 'NO'

# TLE test 49
# https://codeforces.com/contest/1810/submission/199973604


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        A = list(map(int, input().split()))
        edges = [list(map(int, input().split())) for _ in range(M)]
        res = solve(N, M, A, edges)
        print(res)


if __name__ == '__main__':
    main()

