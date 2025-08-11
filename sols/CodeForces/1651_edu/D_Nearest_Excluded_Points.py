''' D. Nearest Excluded Points
https://codeforces.com/contest/1651/problem/D
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

def solve(N, P):
    P = {(x, y): i for i, (x, y) in enumerate(P)}
    queue = deque([])
    res = [None] * N

    for (x, y), i in P.items():
        for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if (nx, ny) not in P:
                res[i] = (nx, ny)
                queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if (nx, ny) not in P or res[P[nx, ny]]: continue
            res[P[nx, ny]] = res[P[x, y]]
            queue.append((nx, ny))

    return res


def main():
    N = int(input())
    P = [tuple(map(int, input().split())) for _ in range(N)]
    out = solve(N, P)
    for tup in out: print(*tup)


if __name__ == '__main__':
    main()

