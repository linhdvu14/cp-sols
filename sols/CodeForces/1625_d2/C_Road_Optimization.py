''' C. Road Optimization
https://codeforces.com/contest/1625/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug')

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

def solve(N, L, K, D, A):
    # dp[i][k] = min cost to go 0..i if
    # * last unremoved sign is i
    # * having removed k signs
    dp = [[INF]*(K+1) for _ in range(N)]
    dp[0][0] = 0
    
    for j in range(1, N):
        for k in range(K+1):
            for i in range(j): # for each possible prev unremoved sign
                d = j - i - 1  # d signs to remove between j and i
                if k + d <= K:
                    dp[j][k+d] = min(dp[j][k+d], dp[i][k] + (D[j]-D[i])*A[i])

    res = INF
    for i in range(N):
        for k in range(K+1):
            if k + N - i - 1 <= K:
                res = min(res, dp[i][k] + (L-D[i])*A[i])

    return res


def main():
    N, L, K = list(map(int, input().split()))
    D = list(map(int, input().split()))
    A = list(map(int, input().split()))
    out = solve(N, L, K, D, A)
    output(f'{out}\n')


if __name__ == '__main__':
    main()

