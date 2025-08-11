''' Sum and OR
https://www.codechef.com/JAN222A/problems/SUMANDOR
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

def is_ok(n, X, S):
    '''is there a seq of length n s.t. sum is S and or is X'''
    # X must be an element of optimal sequence (can rearrange 1 bit)
    # this step ensures all set bits of X are covered
    S -= X
    n -= 1

    # each set bit of X can have at most n-1 copies
    # should use as many as possible as higher bits can always trade for lower bits
    for i in range(31, -1, -1):
        if (X >> i) & 1 == 0: continue
        used = min(S // (1<<i), n)
        S -= (1<<i) * used
    return S == 0


def solve(X, S):
    res, lo, hi = -1, 1, S+1
    while lo <= hi:
        mi = (lo+hi) // 2
        if is_ok(mi, X, S):
            res = mi
            hi = mi - 1
        else:
            lo = mi + 1
    return res


def main():
    T = int(input())
    for _ in range(T):
        X, S = list(map(int, input().split()))
        out = solve(X, S)
        print(out)


if __name__ == '__main__':
    main()

