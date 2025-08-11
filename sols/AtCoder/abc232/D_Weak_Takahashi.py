''' D - Weak Takahashi
https://atcoder.jp/contests/abc232/tasks/abc232_d
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

from collections import deque

def main():
    R, C = list(map(int, input().split()))
    grid = [input().decode().strip() for _ in range(R)]

    res = 1
    visited = [[False]*C for _ in range(R)]
    queue = deque([(0, 0, 1)])
    while queue:
        r, c, d = queue.popleft()
        if visited[r][c]: continue
        visited[r][c] = True
        res = max(res, d)
        for rr, cc in [(r, c+1), (r+1, c)]:
            if not (0 <= rr < R and 0 <= cc < C): continue
            if grid[rr][cc] == '#': continue
            if visited[rr][cc]: continue
            queue.append((rr, cc, d+1))

    print(d)



if __name__ == '__main__':
    main()

