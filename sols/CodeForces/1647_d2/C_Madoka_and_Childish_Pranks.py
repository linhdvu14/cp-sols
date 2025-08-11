''' C. Madoka and Childish Pranks
https://codeforces.com/contest/1647/problem/C
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

# fill each row then first col
def solve(R, C, grid):
    res = []
    for r in range(R):
        for c in range(C-1, 0, -1):
            if grid[r][c] == 1:
                res.append((r+1, c, r+1, c+1))
    for r in range(R-1, -1, -1):
        if grid[r][0] == 1:
            if r == 0: return -1, []
            res.append((r, 1, r+1, 1))
    return len(res), res


def main():
    T = int(input())
    for _ in range(T):
        R, C = list(map(int, input().split()))
        grid = [list(map(int, list(input().decode().strip()))) for _ in range(R)]
        r1, r2 = solve(R, C, grid)
        print(r1)
        if r2:
            for tup in r2: print(*tup)


if __name__ == '__main__':
    main()

