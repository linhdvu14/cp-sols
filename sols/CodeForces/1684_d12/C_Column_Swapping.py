''' C. Column Swapping
https://codeforces.com/contest/1684/problem/C
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
    sgrid = [sorted(row) for row in grid]
    swaps = set()
    for row, srow in zip(grid, sgrid):
        wrong = [i for i, (a, b) in enumerate(zip(row, srow)) if a != b]
        if len(wrong) > 2: return [-1]
        if wrong: swaps.add(tuple(wrong))
    
    if not swaps: return [1, 1]
    if len(swaps) > 1: return [-1]
    
    i, j = list(swaps)[0]
    for row, srow in zip(grid, sgrid):
        if (row[i], row[j]) != (srow[j], srow[i]): return [-1]
    
    return [i+1, j+1]


def main():
    T = int(input())
    for _ in range(T):
        R, C = list(map(int, input().split()))
        grid = [list(map(int, input().split())) for _ in range(R)]
        out = solve(R, C, grid)
        print(*out)


if __name__ == '__main__':
    main()

