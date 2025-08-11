''' C. Those Who Are With Us
https://codeforces.com/contest/2121/problem/C
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

def solve(R, C, grid):
    mx = mxr = mxc = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] > mx:
                mx, mxr, mxc = grid[r][c], r, c
    
    cand_c = None
    ok = True
    for r in range(R):
        for c in range(C):
            if grid[r][c] != mx: continue
            if r == mxr: continue
            if cand_c is not None and cand_c != c: ok = False
            cand_c = c
    if ok: return mx - 1

    cand_r = None
    ok = True
    for r in range(R):
        for c in range(C):
            if grid[r][c] != mx: continue
            if c == mxc: continue
            if cand_r is not None and cand_r != r: ok = False
            cand_r = r
    if ok: return mx - 1

    return mx


def main():
    T = int(input())
    for _ in range(T):
        R, C = list(map(int, input().split()))
        grid = [list(map(int, input().split())) for _ in range(R)]
        res = solve(R, C, grid)
        print(res)


if __name__ == '__main__':
    main()

