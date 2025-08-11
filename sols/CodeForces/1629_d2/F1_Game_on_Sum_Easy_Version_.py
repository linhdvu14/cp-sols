''' F1. Game on Sum (Easy Version)
https://codeforces.com/contest/1629/problem/F1
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

MOD = 10**9 + 7
HALF = (MOD + 1) // 2

def solve(N, M, K):
    if K == 0 or M == 0: return 0
    if M == N: return (K * N) % MOD

    # dp[n][m] = score if A has n turns left, B has m adds left
    # say A picks a, after B picks will have min(dp[n-1][m-1] + a, dp[n-1][m] - a)
    # A should pick intersection to max this min
    dp = [[0]*(M+1) for _ in range(N+1)]
    for n in range(1, N+1):
        for m in range(1, min(n, M+1)):
            dp[n][m] = (dp[n-1][m-1] + dp[n-1][m]) * HALF % MOD
        for m in range(n, M+1):
            dp[n][m] = (K*n) % MOD
    
    return dp[N][M]


def main():
    T = int(input())
    for _ in range(T):
        N, M, K = list(map(int, input().split()))
        out = solve(N, M, K)
        output(f'{out}\n')


if __name__ == '__main__':
    main()
