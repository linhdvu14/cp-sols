''' Gcd and Lcm
https://www.codechef.com/JUNE222A/problems/GCDANDLCM
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

def is_square(x):
    s = int(x**0.5)
    return any(a*a == x for a in [s-1, s, s+1])


# let a = gm, b = gn where gcd(m, n) = 1
# then g^2 (m^2 + 1) (n^2 + 1) = N

def solve(N):
    res = 0
    g = 1
    while g * g < N:
        prod, r = divmod(N, g*g)
        if r == 0:
            d1 = 2
            while d1 * d1 < prod:
                if is_square(d1-1):
                    d2, r = divmod(prod, d1)
                    if r == 0 and is_square(d2-1) and gcd(d1-1, d2-1) == 1:
                        res += 2
                d1 += 1
            if d1 * d1 == prod and d1 == 2: res += 1
        g += 1
    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        out = solve(N)
        print(out)


if __name__ == '__main__':
    main()

