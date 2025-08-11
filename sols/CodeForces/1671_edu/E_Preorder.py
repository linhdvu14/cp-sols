''' E. Preorder
https://codeforces.com/contest/1671/problem/E
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

MOD = 998244353

def solve(N, S):
    # num nodes whose children are not isomorphic (cannot transform after some sub-swaps)
    # if isomorphic, should swap at subtree level
    cnt = 0

    # 2 subtrees are isomorphic if have same minimum preorder string
    # dp[p] = min preorder string of subtree p
    dp = list(S)
    for p in range(2**(N-1)-2, -1, -1):
        l, r = 2*p + 1, 2*p + 2
        if dp[l] < dp[r]: dp[p] += dp[l] + dp[r]
        else: dp[p] += dp[r] + dp[l]
        if dp[l] != dp[r]: cnt += 1

    return pow(2, cnt, MOD)


def main():
    N = int(input())
    S = input().decode().strip()
    out = solve(N, S)
    print(out)


if __name__ == '__main__':
    main()

