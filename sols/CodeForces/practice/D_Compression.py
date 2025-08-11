''' D. Compression
https://codeforces.com/contest/1107/problem/D
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

def get_divisors(x):
    small, big = [], []
    d = 1
    while d * d < x:
        d2, r = divmod(x, d)
        if r == 0:
            small.append(d)
            big.append(d2)
        d += 1
    if d * d == x: small.append(d)
    return big + small[::-1]


def solve_1(N, grid):
    # dp[r][c] = max d s.t. the square with side d and top left at (r, c) has same value
    dp = [[1] * N for _ in range(N)]
    for r in range(N-2, -1, -1):
        for c in range(N-2, -1, -1):
            if grid[r][c] != grid[r+1][c] or grid[r][c] != grid[r][c+1] or grid[r][c] != grid[r+1][c+1]: continue
            dp[r][c] = min(dp[r+1][c], dp[r][c+1], dp[r+1][c+1]) + 1
    
    # check that x-compression is ok
    def is_ok(x):
        for r in range(0, N, x):
            for c in range(0, N, x):
                if dp[r][c] < x:
                    return False
        return True

    cands = get_divisors(N)
    for x in cands:
        if is_ok(x):
            return x


from math import gcd

# x must be factor of all consecutive value length, row-wise and col-wise
def solve_2(N, grid):
    res = rcnt = 0
    for r in range(N):
        if r == 0 or grid[r] != grid[r-1]:
            res = gcd(res, rcnt)
            rcnt = ccnt = 0
            for c in range(N):
                if c == 0 or grid[r][c] != grid[r][c-1]:
                    res = gcd(res, ccnt)
                    ccnt = 0
                ccnt += 1
            res = gcd(res, ccnt)
            
        rcnt += 1
    
    res = gcd(res, rcnt)

    return res


solve = solve_2

def main():
    N = int(input())
    grid = []
    for _ in range(N):
        s = input().decode().strip()
        row = bin(int(s, 16))[2:].zfill(N)
        grid.append(row)
    out = solve(N, grid)
    print(out)


if __name__ == '__main__':
    main()

