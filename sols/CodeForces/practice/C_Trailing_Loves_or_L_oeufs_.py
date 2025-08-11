''' C. Trailing Loves (or L'oeufs?)
https://codeforces.com/contest/1114/problem/C
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

# for int dict key
from random import randrange
RAND = randrange(1 << 62)
def conv(x): return x ^ RAND

INF = float('inf')

# -----------------------------------------

def solve(N, B):
    # required prime factors for 1 zero
    cnt = {}
    d = 2
    while d * d <= B:
        while B % d == 0:
            cnt[d] = cnt.get(d, 0) + 1
            B //= d
        d += 1
    if B > 1: cnt[B] = 1

    res = N
    for d, per_one in cnt.items():
        avail, N2 = 0, N
        while N2 > 0:
            N2 //= d
            avail += N2
        res = min(res, avail // per_one)

    return res


def main():
    N, B = list(map(int, input().split()))
    out = solve(N, B)
    print(out)


if __name__ == '__main__':
    main()

