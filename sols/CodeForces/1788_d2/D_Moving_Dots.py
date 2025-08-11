''' D. Moving Dots
https://codeforces.com/contest/1788/problem/D
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def debug(*args):   
    if os.environ.get('debug') in [None, '0']: return
    from inspect import currentframe, getframeinfo
    from re import search
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')

INF = float('inf')

# -----------------------------------------

from bisect import bisect_left
MOD = 10**9 + 7


def solve(N, A):
    POW = [1] * (N + 1)
    for i in range(1, N + 1): POW[i] = POW[i - 1] * 2 % MOD

    # make a, b move towards each other
    res = 0
    for i, a in enumerate(A):
        for j in range(i + 1, N):
            b = A[j]
            d = b - a
            l = bisect_left(A, a - d) - 1  # max l < i s.t. A[l] < a - d
            r = bisect_left(A, b + d)      # min r > j s.t. A[r] >= b + d
            res = (res + POW[l + 1] * POW[N - r]) % MOD  # any subset on left x any subset on right

    return res


def main():
    N = int(input())
    A = list(map(int, input().split()))
    res = solve(N, A)
    print(res)


if __name__ == '__main__':
    main()
