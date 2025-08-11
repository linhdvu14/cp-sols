''' F - Keep Connect
https://atcoder.jp/contests/abc248/tasks/abc248_f
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

# connect vertices column by column, from left to right
# at any stage, can only have 1 or 2 connected components
# let dp[k][i][j] = num ways to connect columns 0..i, s.t. have j edges removed, k = whether currently connected
# ans is dp[1][N-1][j] for j=1..N-1
# dp[0][i][j] -> update dp[1][i+1][j], dp[0][i+1][j+1]
# dp[1][i][j] -> update dp[1][i+1][j], 3x dp[1][i+1][j+1], 2x dp[0][i+1][j+2]

def main():
    N, P = list(map(int, input().split()))

    dp = [[[0]*N for _ in range(N)] for _ in range(2)]
    dp[0][0][1] = dp[1][0][0] = 1
    for i in range(N-1):
        for j in range(N):
            dp[1][i+1][j] = (dp[1][i+1][j] + dp[0][i][j] + dp[1][i][j]) % P
            if j+1 < N:
                dp[0][i+1][j+1] = (dp[0][i+1][j+1] + dp[0][i][j]) % P
                dp[1][i+1][j+1] = (dp[1][i+1][j+1] + 3 * dp[1][i][j]) % P
            if j+2 < N:
                dp[0][i+1][j+2] = (dp[0][i+1][j+2] + 2 * dp[1][i][j]) % P
    
    print(*dp[1][N-1][1:])


if __name__ == '__main__':
    main()

