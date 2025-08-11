''' E - Rook Path
https://atcoder.jp/contests/abc232/tasks/abc232_e
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

MOD = 998244353

# https://atcoder.jp/contests/abc232/submissions/28018647
def main():
    R, C, K = list(map(int, input().split()))
    x1, y1, x2, y2 = list(map(int, input().split()))

    # dp[k][0] = num paths to (x1, y1) after k moves
    # dp[k][1] = num paths to (x1, y) where y != y1 (same row)
    # dp[k][2] = num paths to (x, y1) where x != x1 (same col)
    # dp[k][3] = num paths to (x, y) where x != x1, y != y1
    dp = [[0]*4 for _ in range(K+1)]
    dp[0][0] = 1

    for k in range(1, K+1):
        dp[k][0] = (dp[k-1][1]*(C-1) + dp[k-1][2]*(R-1)) % MOD
        dp[k][1] = (dp[k-1][0] + dp[k-1][1]*(C-2) + dp[k-1][3]*(R-1)) % MOD
        dp[k][2] = (dp[k-1][0] + dp[k-1][2]*(R-2) + dp[k-1][3]*(C-1)) % MOD
        dp[k][3] = (dp[k-1][1] + dp[k-1][2] + dp[k-1][3]*(R+C-4)) % MOD
    
    if x1 == x2 and y1 == y2: 
        print(dp[-1][0])
    elif x1 == x2: 
        print(dp[-1][1])
    elif y1 == y2: 
        print(dp[-1][2])
    else:
        print(dp[-1][3])


if __name__ == '__main__':
    main()

