''' D. Lena and Matrix
https://codeforces.com/contest/1689/problem/D
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
    # |x1 - x2| + |y1 - y2| = max(|(x1+y1) - (x2+y2)|, |(x1-y1) - (x2-y2)|)
    # farthest B must be among: max(x+y), max(x-y), min(x+y), min(x-y)
    mxs, mxd, mns, mnd = (-INF, -1, -1), (-INF, -1, -1), (INF, -1, -1), (INF, -1, -1)
    for r in range(R):
        for c in range(C):
            if grid[r][c] != 'B': continue
            mxs = max(mxs, (r + c, r, c))
            mxd = max(mxd, (r - c, r, c))
            mns = min(mns, (r + c, r, c))
            mnd = min(mnd, (r - c, r, c))
    blacks = [(mxs[1], mxs[2]), (mxd[1], mxd[2]), (mns[1], mns[2]), (mnd[1], mnd[2])]
    
    res = (INF, -1, -1)
    for r in range(R):
        for c in range(C):
            mx = max(abs(r - br) + abs(c - bc) for br, bc in blacks)
            res = min(res, (mx, r, c))
    
    return res[1] + 1, res[2] + 1


def main():
    T = int(input())
    for _ in range(T):
        R, C = list(map(int, input().split()))
        grid = [input().decode().strip() for _ in range(R)]
        out = solve(R, C, grid)
        print(*out)


if __name__ == '__main__':
    main()

