''' C. Zero Path
https://codeforces.com/contest/1695/problem/C
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

# can convert any path to any path, by converting through path (1, 1) -> (1, C) -> (R, C)
# each move changes sum by -2, 0 or 2
# so any sum between min and max is possible, if parity ok

def solve(R, C, grid):
    if (R + C - 1) % 2 != 0: return 'NO'
 
    mn = [[0] * C for _ in range(R)]
    mx = [[0] * C for _ in range(R)]
    mn[0][0] = mx[0][0] = grid[0][0]
    for r in range(1, R):
        mn[r][0] = mn[r-1][0] + grid[r][0]
        mx[r][0] = mx[r-1][0] + grid[r][0]
    for c in range(1, C):
        mn[0][c] = mn[0][c-1] + grid[0][c]
        mx[0][c] = mx[0][c-1] + grid[0][c]
    for r in range(1, R):
        for c in range(1, C):
            mn[r][c] = min(mn[r-1][c], mn[r][c-1]) + grid[r][c]
            mx[r][c] = max(mx[r-1][c], mx[r][c-1]) + grid[r][c]
    
    if mn[R-1][C-1] <= 0 <= mx[R-1][C-1]: return 'YES'
    return 'NO'


def main():
    T = int(input())
    for _ in range(T):
        R, C = list(map(int, input().split()))
        grid = [list(map(int, input().split())) for _ in range(R)]
        out = solve(R, C, grid)
        print(out)


if __name__ == '__main__':
    main()

