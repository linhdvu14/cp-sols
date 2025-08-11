''' C. Chat Ban
https://codeforces.com/contest/1612/problem/C
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

def solve(k, x):
    if x >= k*k: return 2*k - 1
    if x == k * (k+1) // 2: return k

    if x < k * (k+1) // 2:
        r, lo, hi = -1, 0, k
        while lo <= hi:
            mi = (lo + hi) // 2
            if mi * (mi+1) // 2 < x:
                r = mi + 1
                lo = mi + 1
            else:
                hi = mi - 1
        return r
    else:
        r, lo, hi = -1, 0, k-1
        while lo <= hi:
            mi = (lo + hi) // 2
            if k*k - mi * (mi+1) // 2 < x:
                r = mi - 1
                hi = mi - 1
            else:
                lo = mi + 1
        return 2*k - 1 - r


def main():
    T = int(input())
    for _ in range(T):
        k, x = list(map(int, input().split()))
        out = solve(k, x)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

