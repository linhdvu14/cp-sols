''' Problem 3. Walking Home '''

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

def solve(N, K, grid):
    # dp[r][c][k][d] = 
    # * num ways to reach grid[r][c]
    # * having used k turns so far
    # * entering with direction d: 0=right, 1=down
    dp = [[[[0]*2 for _ in range(K+1)] for _ in range(N)] for _ in range(N)]
    for c in range(N):
        if grid[0][c] == 'H': break
        dp[0][c][0][0] = 1
    for r in range(N):
        if grid[r][0] == 'H': break
        dp[r][0][0][1] = 1

    for r in range(1, N):
        for c in range(1, N):
            for k in range(K+1):
                if grid[r][c] == 'H':
                    dp[r][c][k][0] = 0
                    dp[r][c][k][1] = 0
                else:
                    dp[r][c][k][0] += dp[r][c-1][k][0]
                    dp[r][c][k][1] += dp[r-1][c][k][1]
                    if k > 0:
                        dp[r][c][k][0] += dp[r][c-1][k-1][1]
                        dp[r][c][k][1] += dp[r-1][c][k-1][0]

    res = sum(sum(row) for row in dp[-1][-1])
    return res


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        grid = [input().decode().strip() for _ in range(N)]
        out = solve(N, K, grid)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

