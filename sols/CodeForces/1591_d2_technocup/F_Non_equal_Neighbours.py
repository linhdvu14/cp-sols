''' F. Non-equal Neighbours
https://codeforces.com/contest/1591/problem/F
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

# https://atcoder.jp/contests/arc115/submissions/27470789
# dp[n] = num ways to select valid b[1]..b[n] = res
# dp[1] = a[1]
# dp[i] = dp[i-1] * a[i]                         ---> free b[i]
#         - dp[i-2] * min(a[i-1], a[i])          ---> with b[i] == b[i-1]
#         + dp[i-3] * min(a[i-2], a[i-1], a[i])  ---> with b[i] == b[i-1] == b[i-2]
#         - ...

def solve_N2(N, A):
    dp = [0]*(N+1)
    dp[0] = 1

    for i, a in enumerate(A):
        mn, sign = a, 1
        for j in range(i, -1, -1):
            mn = min(mn, A[j])
            dp[i+1] += dp[j]*mn*sign
            dp[i+1] %= MOD
            sign *= -1
    
    return dp[-1]


def solve_N(N, A):
    # dp[i] = SUM_(j=0..i-1) sign * dp[j] * min(a[j+1]...a[i])
    dp = [0]*(N+1)
    dp[0] = 1

    # keep monotonic (increasing) stack of (min(a[j+1]...), j, signed agg val corresponding to mn)
    # each ele pushed and popped at most once -> O(N)
    stack = []

    # calc dp[i+1]
    for i, a in enumerate(A):
        cur = 0 if i == 0 else dp[i] 

        # update all min(a[j+1]...) with a
        add = 0
        while stack and stack[-1][0] >= a:
            a2, i2, v = stack.pop()
            if (i-i2) % 2 == 0:
                cur -= v * (a-a2)
                add += v  # to be counted with a
            else:
                cur += v * (a-a2)
                add -= v

        cur = -cur + dp[i]*a 
        cur %= MOD

        dp[i+1] = cur
        stack.append((a, i, add+dp[i]))

    return dp[-1] % MOD


solve = solve_N


def main():
    N = int(input())
    A = list(map(int, input().split()))
    out = solve(N, A)
    output(f'{out}\n')


if __name__ == '__main__':
    main()

