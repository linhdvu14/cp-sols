''' C. Palindrome Basis
https://codeforces.com/contest/1673/problem/C
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
MAX = 4*10**4

# dp[n][i] = num ways to represent n with first i palins
#          = dp[n][i-1] + dp[n-palins[i]][i]
dp = [0] * (MAX + 1)
dp[0] = 1
for p in range(1, MAX+1):
    sp = str(p)
    if sp != sp[::-1]: continue
    for n in range(p, MAX+1):
        dp[n] = (dp[n] + dp[n-p]) % MOD


def solve(N):
    return dp[N]


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        out = solve(N)
        print(out)


if __name__ == '__main__':
    main()

