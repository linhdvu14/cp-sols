''' Reduce to zero
https://www.codechef.com/JUNE221A/problems/RED0
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

# when x < y, need at least y + 1 ops (at least y ops to make y zero)
# when x < y <= 2x, this strategy requires exactly y + 1 ops:
# * use 3rd op (2x-y) times --> x := y-x; y := 2(y-x)
# * use 1st op 1 time       --> x = y := 2(y-x)
# * use 3rd op 2(y-x) times --> x = y := 0
# -> total = (2x-y) + 1 + 2(y-x) = y + 1

def solve(x, y):
    if x == y: return x
    if x > y: x, y = y, x
    if x == 0: return -1

    # use 1st op until x <= y <= 2x
    res, lo, hi = 0, 0, 64
    while lo <= hi:
        mi = (lo + hi) // 2
        if (x << mi) >= y:
            res = mi
            hi = mi - 1
        else:
            lo = mi + 1
    
    return res + y


def main():
    T = int(input())
    for _ in range(T):
        x, y = list(map(int, input().split()))
        out = solve(x, y)
        print(out)


if __name__ == '__main__':
    main()

