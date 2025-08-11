''' D. Med-imize
https://codeforces.com/contest/1993/problem/D
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

from inspect import currentframe, getframeinfo
from re import search
DEBUG = os.environ.get('debug') not in [None, '0']

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

def solve(N, K, A):
    if N <= K: return sorted(A)[(N - 1) // 2]

    sz = N % K or K 
    dp = [-INF] * K

    def ok(x):
        # choose one ele in each idx i % K == k s.t. maximize (A[i] >= x)
        for i in range(K): dp[i] = -INF
        for i, a in enumerate(A):
            i %= K
            b = 1 if a >= x else -1
            if not i: dp[i] = max(dp[i], b)
            else: dp[i] = max(dp[i], dp[i - 1] + b)
        return dp[sz - 1] > 0

    res, lo, hi = 0, 1, max(A)
    while lo <= hi:
        mi = (lo + hi) // 2
        if ok(mi):
            res = mi
            lo = mi + 1
        else:
            hi = mi - 1

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        res = solve(N, K, A)
        print(res)


if __name__ == '__main__':
    main()

