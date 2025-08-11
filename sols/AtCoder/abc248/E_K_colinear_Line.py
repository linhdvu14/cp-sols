''' E - K-colinear Line
https://atcoder.jp/contests/abc248/tasks/abc248_e
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
from math import gcd

def get_2dline(p1, p2):
    if p1 == p2: return (0, 0, 0)
    _p1, _p2 = min(p1, p2), max(p1, p2)
    a, b, c = _p2[1] - _p1[1], _p1[0] - _p2[0], _p1[1] * _p2[0] - _p1[0] * _p2[1]
    g = gcd(gcd(a, b), c)
    return a // g, b // g, c // g


def main():
    N, K = list(map(int, input().split()))
    if K == 1: return 'Infinity'

    P = [list(map(int, input().split())) for _ in range(N)]

    slopes = {}
    for i in range(N):
        for j in range(i):
            a, b, c = get_2dline(P[i], P[j])
            if (a, b, c) not in slopes: slopes[a, b, c] = set()
            slopes[a, b, c].add(i)
            slopes[a, b, c].add(j)
    
    res = 0
    for v in slopes.values():
        if len(v) >= K:
            res += 1
    return res



if __name__ == '__main__':
    out = main()
    print(out)

