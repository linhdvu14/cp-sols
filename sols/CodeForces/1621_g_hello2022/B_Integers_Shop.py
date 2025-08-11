''' B. Integers Shop
https://codeforces.com/contest/1621/problem/B
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

def solve(N, segs):
    left = right = mid = None
    for l, r, c in segs:
        if not left or left[0] > l or (left[0] == l and left[1] > c): left = (l, c)
        if not right or right[0] < r or (right[0] == r and right[1] > c): right = (r, c)
        if not mid or mid[0] < r-l+1 or (mid[0] == r-l+1 and mid[1] > c): mid = (r-l+1, c)
        cost = left[1] + right[1]
        if mid and mid[0] == right[0] - left[0] + 1: cost = min(cost, mid[1])
        print(cost)


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        segs = [tuple(map(int, input().split())) for _ in range(N)]
        solve(N, segs)


if __name__ == '__main__':
    main()

