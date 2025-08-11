''' D. Cut
https://codeforces.com/contest/1516/problem/D
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

def sieve(N):
    primes = []
    lpf = [0] * (N + 1)
    for i in range(2, N+1):
        if lpf[i] == 0:
            lpf[i] = i
            primes.append(i)
        for p in primes:
            if p * i > N or p > lpf[i]: break
            lpf[p * i] = p 
    return lpf


# lcm equals product when each pair of ele is relatively prime
# for each query, go l to r and greedily pick longest valid subarray

def solve(N, Q, A, queries):
    lpf = sieve(max(A))

    # par[i] = max j s.t. A[i..j-1] is valid
    par = [N] * (N + 1)
    last = {}
    for i in range(N-1, -1, -1):
        a = A[i]
        while a > 1:
            f = lpf[a]
            while a % f == 0: a //= f
            par[i] = min(par[i], last.get(f, N))
            last[f] = i
        par[i] = min(par[i], par[i+1])  # prevent case i < (k, l) < par[i] not coprime

    # up[i][k] = (2^k)-th ancestor of A[i]
    L = N.bit_length()
    up = [[N] * L for _ in range(N+1)]
    for k in range(L):
        for i in range(N):
            if k == 0: up[i][k] = par[i]
            else: up[i][k] = up[up[i][k-1]][k-1]

    # for each query, find min j s.t. j-th ancestor of l > r
    res = [0] * Q
    for qi, (l, r) in enumerate(queries):
        l -= 1; r -= 1
        j = 0
        for k in range(L-1, -1, -1):
            if up[l][k] <= r:
                j |= 1 << k
                l = up[l][k]
        res[qi] = j + 1
    
    return res



def main():
    N, Q = list(map(int, input().split()))
    A = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for _ in range(Q)]
    out = solve(N, Q, A, queries)
    print(*out, sep='\n')


if __name__ == '__main__':
    main()
