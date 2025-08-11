''' Sleep Technique
https://www.codechef.com/LTIME103B/problems/SLEEPTECH
'''

import io, os, sys
from re import I
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

def solve(N, A, B, intervals):
    # check if l..r can intersect a good interval:
    # * A, A+1, ..., B
    # * 2A+1, 2A+2, ..., 2B-1
    # * 3A+3, 3A+4, ..., 3B-3
    def is_ok(l, r):
        if r < A: return False
        if l > (A+B)*(B-A+1) // 2: return False

        # 3 ways to intersect: l..a..r, l..b..r, a..l..r..b
        # find max n s.t. a = nA + n(n-2)/2 <= r, then check b >= l
        n, lo, hi = -1, 1, B-A+1
        while lo <= hi:
            mi = (lo+hi) // 2
            if mi*A + mi*(mi-1)//2 <= r:
                n = mi
                lo = mi + 1
            else:
                hi = mi - 1
        return n*B - n*(n-1)//2 >= l

    delta = {}
    for l, r in intervals:
        delta[l] = delta.get(l, 0) + 1
        delta[r+1] = delta.get(r+1, 0) - 1
    
    # check each consecutive
    res = bal = 0
    prev = -1
    times = sorted(delta.keys())
    for t in times:
        if prev != -1 and is_ok(prev, t-1):
            res = max(res, bal)
        bal += delta[t]
        prev = t

    return res



def main():
    T = int(input())
    for _ in range(T):
        N, A, B = list(map(int, input().split()))
        intervals = [list(map(int, input().split())) for _ in range(N)]
        out = solve(N, A, B, intervals)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

