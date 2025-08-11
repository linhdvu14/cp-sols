''' B. Madoka and the Elegant Gift
https://codeforces.com/contest/1647/problem/B
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

# need a 90 degree angle of 1s
def solve(R, C, grid):
    for r in range(1, R):
        for c in range(1, C):
            if grid[r][c] + grid[r-1][c] + grid[r-1][c-1] + grid[r][c-1] == 3:
                return False    
    return True


def main():
    T = int(input())
    for _ in range(T):
        R, C = list(map(int, input().split()))
        grid = [list(map(int, list(input().decode().strip()))) for _ in range(R)]
        out = solve(R, C, grid)
        print('YES' if out else 'NO')


if __name__ == '__main__':
    main()

