''' C. Smilo and Minecraft
https://codeforces.com/contest/2113/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

from inspect import currentframe, getframeinfo
from re import search
DEBUG = os.environ.get('debug') not in [None, '0']

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

def solve(R, C, K, grid):
    ps = [[0] * (C + 1) for _ in range(R + 1)]
    for r in range(R):
        for c in range(C):
            ps[r][c] = ps[r][c - 1] + ps[r - 1][c] - ps[r - 1][c - 1] + (grid[r][c] == 'g')

    def query(r, c):
        r1 = max(r - K + 1, 0)
        r2 = min(r + K - 1, R - 1)
        c1 = max(c - K + 1, 0)
        c2 = min(c + K - 1, C - 1) 
        lost = ps[r2][c2] - ps[r2][c1 - 1] - ps[r1 - 1][c2] + ps[r1 - 1][c1 - 1]
        return lost

    mn = INF
    for r in range(R):
        for c in range(C):
            if grid[r][c] != '.': continue
            mn = min(mn, query(r, c))
    res = ps[R - 1][C - 1] - mn

    return res


def main():
    T = int(input())
    for _ in range(T):
        R, C, K = list(map(int, input().split()))
        grid = [input().decode().strip() for _ in range(R)]
        res = solve(R, C, K, grid)
        print(res)


if __name__ == '__main__':
    main()

