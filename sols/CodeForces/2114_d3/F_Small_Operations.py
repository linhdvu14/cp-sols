''' F. Small Operations
https://codeforces.com/contest/2114/problem/F
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
from math import gcd


def solve(X, Y, K):
    g = gcd(X, Y)
    X //= g 
    Y //= g

    def f(x):
        if x == 1: return 0

        divs = []
        d1 = 1
        while d1 * d1 <= x:
            d2, r = divmod(x, d1)
            if not r: divs += [d1, d2]
            d1 += 1
        divs.sort()

        N = len(divs)
        dp = [INF] * N
        dp[0] = 0
        for i in range(1, N):
            for j in range(i - 1, -1, -1):
                y, r = divmod(divs[i], divs[j])
                if y > K: break 
                if not r: dp[i] = min(dp[i], dp[j] + 1)
        
        return dp[-1]
    

    res = f(X) + f(Y)
    return -1 if res is INF else res


def main():
    T = int(input())
    for _ in range(T):
        X, Y, K = list(map(int, input().split()))
        res = solve(X, Y, K)
        print(res)


if __name__ == '__main__':
    main()

