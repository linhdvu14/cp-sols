''' Random OR
https://www.codechef.com/FEB221A/problems/RANDOMOR
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

MAX = 3 * 10**5
MOD = 10**9 + 7

def batch_pow(b, N, p):
    '''precompute up to b^N % p and 1/(b^N - 1) % p '''
    pw = [1] * (N+1)
    for i in range(1, N+1): 
        pw[i] = (pw[i-1] * b) % p
    
    inv_pw = [1] * (N+1)
    for i in range(1, N+1):
        inv_pw[i] = pow(pw[i]-1, p-2, p)

    return pw, inv_pw


def batch_factorial(N, p):
    ''' precompute n! % p for n=1..N'''
    fact = [1]*(N+1)  # n! % p
    for i in range(1, N+1):
        fact[i] = (i * fact[i-1]) % p
    return fact


def batch_nCk(N, p):
    ''' precompute binomial coefficients to calc up to C(N, N) % p
    C(N, k) mod p = fact[n] * inv_fact[k] * inv_fact[n-k]
    '''
    fact = [1]*(N+1)  # n! % p
    for i in range(1, N+1):
        fact[i] = (i * fact[i-1]) % p

    inv_fact = [1]*(N+1)  # (1 / n!) % p
    for i in range(1, N+1):
        inv_fact[i] = pow(fact[i], p-2, p)
    
    return fact, inv_fact


POW, INV_POW = batch_pow(2, MAX, MOD)
FACT, INV_FACT = batch_nCk(MAX, MOD)

# after each move, each bit independently has prob 0.5 of becoming 1
# need to find expected min moves s.t. all bits are 1
# ans = SUM_{j=1..n} (-1)^(j+1) * nCj * 2^j / (2^j - 1)

def solve(N):
    res = 0
    for j in range(1, N+1):
        res += (-1)**((j+1) % 2) * FACT[N] * INV_FACT[j] * INV_FACT[N-j] * POW[j] * INV_POW[j]
        res %= MOD
    return res
    

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        out = solve(N)
        print(out)


if __name__ == '__main__':
    main()

