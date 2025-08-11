''' A. Not Shading
https://codeforces.com/contest/1627/problem/A
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

def solve(R, C, r, c, grid):
    r -= 1
    c -= 1
    if not any('B' in row for row in grid): return -1
    if grid[r][c] == 'B': return 0
    if 'B' in grid[r] or any(row[c] == 'B' for row in grid): return 1
    return 2


def main():
    T = int(input())
    for _ in range(T):
        R, C, r, c = list(map(int, input().split()))
        grid = [input().decode().strip() for _ in range(R)]
        out = solve(R, C, r, c, grid)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

