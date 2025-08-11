''' D. Yet Another Minimization Problem
https://codeforces.com/contest/1637/problem/D
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

# cost[a] = SUM (a[i] + a[j]) ^ 2 
#         = (n-1) SUM (a[i]) ^ 2 + 2 SUM a[i] a[j]
#         = (n-2) SUM (a[i]) ^ 2 + (SUM a[i]) ^ 2
# cost[b] = (n-2) SUM (b[i]) ^ 2 + (SUM b[i]) ^ 2
# cost[a] + cost[b] = (n-2) (SUM (a[i]) ^ 2 + SUM (b[i]) ^ 2) + (SUM a[i]) ^ 2 + (SUM b[i]) ^ 2
#                   = (n-2) (SUM (a[i]) ^ 2 + SUM (b[i]) ^ 2) + (SUM (a[i] + b[i])) ^ 2 - 2 * SUM a[i] * SUM b[i]
# -> want abs(SUM a[i] - SUM b[i]) min

def solve(N, A, B):
    # dp[i][s] = whether a subset of D[..i] has sum s
    D = [abs(a - b) for a, b in zip(A, B)]
    SD = sum(D)
    dp = [[False]*(SD+1) for _ in range(N)]
    for i, d in enumerate(D):
        dp[i][0] = True
        dp[i][d] = True
        for s in range(1, SD+1):
            if i > 0: dp[i][s] |= dp[i-1][s]
            if s-d >= 0: dp[i][s] |= dp[i-1][s-d]

    # partition D into two subsets with min sum diff
    mnd = -1
    for d in range(SD // 2, -1, -1):
        if dp[-1][d]:
            mnd = SD - 2*d
            break

    # corresponding SUM a[i], SUM b[i]
    S = sum(A) + sum(B)
    sa = (S + mnd) // 2
    sb = (S - mnd) // 2

    s1 = s2 = 0
    for a, b in zip(A, B):
        s1 += a + b
        s2 += a*a + b*b

    res = (N-2) * s2 + s1 * s1 - 2 * sa * sb
    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        out = solve(N, A, B)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

