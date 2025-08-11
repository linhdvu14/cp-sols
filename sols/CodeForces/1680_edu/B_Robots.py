''' B. Robots
https://codeforces.com/contest/1680/problem/B
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

def solve(R, C, grid):
    first_r = first_c = None
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'R' and first_r is None:
                first_r = r, c
    for c in range(C):
        for r in range(R):
            if grid[r][c] == 'R' and first_c is None:
                first_c = r, c
    
    if first_r and first_r == first_c: return 'YES'
    return 'NO'


def main():
    T = int(input())
    for _ in range(T):
        R, C = list(map(int, input().split()))
        grid = [input().decode().strip() for _ in range(R)]
        out = solve(R, C, grid)
        print(out)


if __name__ == '__main__':
    main()

