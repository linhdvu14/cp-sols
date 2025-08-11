''' D. The Winter Hike
https://codeforces.com/contest/1621/problem/D
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

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

def solve(N, cost):
    # clear safe area
    res = 0
    for r in range(N, 2*N):
        for c in range(N, 2*N):
            res += cost[r][c]
    
    # should enter safe area from one of 4 corners
    res += min(
        cost[0][N], cost[0][2*N-1],
        cost[N-1][N], cost[N-1][2*N-1],
        cost[N][N-1], cost[N][0],
        cost[2*N-1][N-1], cost[2*N-1][0],
    )

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        cost = [list(map(int, input().split())) for _ in range(2*N)]
        out = solve(N, cost)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

