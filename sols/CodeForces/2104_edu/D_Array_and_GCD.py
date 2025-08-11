''' D. Array and GCD
https://codeforces.com/contest/2104/problem/D
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

from inspect import currentframe, getframeinfo
from re import search
DEBUG = os.environ.get('debug') not in [None, '0']

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
from bisect import bisect_right

def sieve(N):
    primes = []
    primes_ps = [0]
    lpf = [0] * (N + 1)
    for i in range(2, N + 1):
        if lpf[i] == 0:
            primes.append(i)
            primes_ps.append(primes_ps[-1] + i - 2)
            lpf[i] = i
        for p in primes:
            if p * i > N or p > lpf[i]: break
            lpf[p * i] = p
    return primes_ps


PRIME_PS = sieve(10**7)


def solve(N, A):
    ps = [0]
    for a in sorted(A, reverse=True):
        ps.append(ps[-1] + a - 2)

    res, lo, hi = 0, 0, N 
    while lo <= hi:
        mi = (lo + hi) // 2
        if ps[mi] >= PRIME_PS[mi]:
            res = mi 
            lo = mi + 1
        else:
            hi = mi - 1
    
    return N - res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        res = solve(N, A)
        print(res)


if __name__ == '__main__':
    main()

