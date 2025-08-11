''' C. Schedule Management
https://codeforces.com/contest/1701/problem/C
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

def solve(N, M, A):
    cnt = [0] * N
    for a in A: cnt[a-1] += 1

    def is_ok(t):
        rem = 0
        for c in cnt:
            if c < t: rem -= (t - c) // 2
            else: rem += c - t
        return rem <= 0

    res, lo, hi = -1, 1, max(cnt)
    while lo <= hi:
        mi = (lo + hi) // 2
        if is_ok(mi):
            res = mi
            hi = mi - 1
        else:
            lo = mi + 1

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        A = list(map(int, input().split()))
        out = solve(N, M, A)
        print(out)


if __name__ == '__main__':
    main()

