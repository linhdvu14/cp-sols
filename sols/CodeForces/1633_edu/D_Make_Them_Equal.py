''' D. Make Them Equal
https://codeforces.com/contest/1633/problem/D
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

# OP[n] = min cost to transform 1 to n
OP = [INF] * 2005
OP[1] = 0
for n in range(1, 1001):
    for x in range(1, n+1):
        OP[n + n//x] = min(OP[n + n//x], OP[n] + 1)


def solve(N, K, B, C):
    # W[i] = min cost to transform 1 to B[i]
    W = [OP[b] for b in B]

    # note W[i] <= 10 so total cost of whole A <= 10^4
    if K >= sum(W): return sum(C)

    # knapsack
    # dp[i][k] = max coins converting A[0..i] using up to k operations
    dp = [[0]*(K+1) for _ in range(N)]
    for k in range(W[0], K+1): dp[0][k] = C[0]
    for i in range(1, N):
        for k in range(K+1):
            dp[i][k] = dp[i-1][k]
            if k >= W[i]: dp[i][k] = max(dp[i][k], C[i] + dp[i-1][k-W[i]])

    return dp[-1][-1]


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        B = list(map(int, input().split()))
        C = list(map(int, input().split()))
        out = solve(N, K, B, C)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

