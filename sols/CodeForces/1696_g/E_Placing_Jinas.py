''' E. Placing Jinas
https://codeforces.com/contest/1696/problem/E
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

MOD = 10**9 + 7

def precalc_nCk(N, p):
    ''' precompute binomial coefficients to calc up to C(N, N) % p
    C(N, k) mod p = fact[n] * inv_fact[k] * inv_fact[n-k]
    '''
    fact = [1] * (N+1)  # n! % p
    inv_fact = [1] * (N+1)  # (1 / n!) % p
    for i in range(1, N+1):
        fact[i] = (i * fact[i-1]) % p
        inv_fact[i] = pow(fact[i], p-2, p)
    return fact, inv_fact


# let S(n, d) = sum of d-th diagonal of Pascal's triangle with (n+1) rows
# n=0:  1
# n=1:  1 1
# n=2:  1 2 1
# n=3:  1 3 3  1
# n=4:  1 4 6  4  1
# n=5:  1 5 10 10 5 1
# row i needs sum A[i] elements of diagonal i
def solve_1(N, A):
    MAX = max(a + i - 1 for i, a in enumerate(A)) + 10
    FACT, INV_FACT = precalc_nCk(MAX, MOD)

    def nCk(n, k): return (FACT[n] * INV_FACT[k] * INV_FACT[n-k]) % MOD
    def diagonal_sum(n, d): return nCk(n+1, d+1) % MOD

    res = 0
    for i, a in enumerate(A):
        if a == 0: break
        res = (res + diagonal_sum(a + i - 1, i)) % MOD
    return res


# let f(i, j) = num ops on cell (i, j)
# then f(i, j) = f(i-1, j) + f(i, j-1) = C(i+j, i)
# then ans = SUM_{i=0..n} SUM_{j=0..A[i]-1} C(i+j, i) = SUM_{i=0..n} C(i + A[i], i + 1)
def solve_2(N, A):
    MAX = max(a + i - 1 for i, a in enumerate(A)) + 10
    FACT, INV_FACT = precalc_nCk(MAX, MOD)

    def nCk(n, k): return (FACT[n] * INV_FACT[k] * INV_FACT[n-k]) % MOD

    res = 0
    for i, a in enumerate(A):
        if a == 0: break
        res = (res + nCk(i + a, i + 1)) % MOD

    return res


solve = solve_2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    out = solve(N, A)
    print(out)


if __name__ == '__main__':
    main()

