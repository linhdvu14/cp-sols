''' C. Balanced Stone Heaps
https://codeforces.com/contest/1623/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

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

def solve(N, A):
    A.reverse()

    def is_ok(mn):
        add1 = add2 = 0
        for i in range(N-2):
            if A[i] + add1 < mn: return False
            d = min((A[i] + add1 - mn) // 3, A[i] // 3)
            add1, add2 = add2 + d, d*2
        return A[N-2] + add1 < mn and A[N-1] + add2 < mn

    res, lo, hi = -1, min(A), sum(A)
    while lo <= hi:
        mi = (lo+hi) // 2
        if is_ok(mi):
            res = mi
            lo = mi + 1
        else:
            hi = mi - 1

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

