''' A. Enlarge GCD
https://codeforces.com/contest/1034/problem/A
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

def sieve(N):
    lpf = [0] * (N + 1)
    primes = []
    for i in range(2, N+1):
        if lpf[i] == 0:
            lpf[i] = i
            primes.append(i)
        for p in primes:
            if p * i > N or p > lpf[i]: break
            lpf[p * i] = p
    return lpf


def solve(N, A):
    g = 0
    for a in A: g = gcd(g, a)

    cnt = {}
    for a in A:
        a //= g
        cnt[a] = cnt.get(a, 0) + 1

    # find factors that appear in most numbers
    lpf = sieve(max(A))
    fac_cnt = {}
    for a, c in cnt.items():
        while a > 1:
            p = lpf[a]
            fac_cnt[p] = fac_cnt.get(p, 0) + c
            while a % p == 0: a //= p

    if not fac_cnt: return -1
    return N - max(fac_cnt.values())


def main():
    N = int(input())
    A = list(map(int, input().split()))
    out = solve(N, A)
    print(out)


if __name__ == '__main__':
    main()

