''' C. Product 1 Modulo N
https://codeforces.com/contest/1514/problem/C
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

from math import gcd

# list must include only coprimes with N
def solve(N):
    res = set()
    p = 1
    for a in range(1, N):
        if gcd(a, N) == 1:
            res.add(a)
            p = (p * a) % N
    if p > 1: res.remove(p)
    return sorted(list(res))


def main():
    N = int(input())
    out = solve(N)
    print(len(out))
    print(*out)


if __name__ == '__main__':
    main()
