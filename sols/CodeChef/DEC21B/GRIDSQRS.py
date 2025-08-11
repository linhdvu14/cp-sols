''' Squares Counting
https://www.codechef.com/DEC21B/problems/GRIDSQRS
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

if DEBUG:
    from varname.core import argname
    from inspect import currentframe

def debug(var, *more_vars):
    if not DEBUG: return
    var_names = argname('var', '*more_vars', func=debug)
    values = (var, *more_vars)
    name_and_values = [f'{var_name}={value}'  for var_name, value in zip(var_names, values)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(name_and_values)}')


INF = float('inf')

# -----------------------------------------

def solve(N, grid):
    # right[r][c] = max consecutive ones from (r, c) to the right
    right = [[0]*N for _ in range(N)]
    for r in range(N):
        cnt = 0
        for c in range(N-1, -1, -1):
            right[r][c] = cnt = 0 if grid[r][c] == '0' else cnt + 1
    
    # down[r][c] = max consecutive ones from (r, c) down
    down = [[0]*N for _ in range(N)]
    for c in range(N):
        cnt = 0
        for r in range(N-1, -1, -1):
            down[r][c] = cnt = 0 if grid[r][c] == '0' else cnt + 1

    # make each (r, c) top left of square
    res = 0
    for r in range(N):
        for c in range(N):
            if grid[r][c] == '0': continue
            mx = min(right[r][c], down[r][c])
            for d in range(mx):
                if right[r+d][c] >= d+1 and down[r][c+d] >= d+1:
                    res += 1
    
    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        grid = [list(input().decode().strip()) for _ in range(N)]
        out = solve(N, grid)
        print(out)


if __name__ == '__main__':
    main()

