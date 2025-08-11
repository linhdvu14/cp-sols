''' F. Prabowo Bunny Senpai
https://tlx.toki.id/contests/troc-25/problems/F
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

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

def batch_mobius(N):
    '''return Mobius func of [1..N] in O(N)'''
    primes = []
    lpf = [0]*(N+1)         # least prime factor
    for i in range(2, N+1):
        if lpf[i] == 0:
            primes.append(i)
            lpf[i] = i
        for p in primes:
            if p > lpf[i] or p*i > N: break
            lpf[p*i] = p    # set once per composite number
    
    mobius = [0]*(N+1)
    mobius[1] = 1
    for i in range(2, N+1):
        if lpf[i] == lpf[i // lpf[i]]:  # square lpf
            mobius[i] = 0
        else:
            mobius[i] = -1 * mobius[i // lpf[i]]

    return mobius


def factorize_all(n):
    '''returns a sorted list of all distinct factors of n'''
    small, large = [], []
    for i in range(1, int(n**0.5) + 1, 2 if n & 1 else 1):
        if n % i == 0:
            small.append(i)
            large.append(n // i)
    if small[-1] == large[-1]: large.pop()
    return small + large[::-1]


# let f(x) = num ways to reach x from 1
# let g(z) = SUM_{y < x; z | y} f(y)
# then f(x) = SUM_{y < x; gcd(x, y) = 1} f(y)
#           = SUM_{y < x} f(y) - SUM_{y < x; gcd(x, y) > 1} f(y)
#           = SUM_{y < x} f(y) + SUM_{z > 2; z | x} g(z) mu(z)  (prove by inclusion-exclusion)
#           = SUM_{z=1..x-1; z|x} g(z) mu(z)

# alternate proof using mobius func property:
#      f(x) = SUM_{y < x; gcd(x, y) = 1} f(y)
#           = SUM_{y} f(y) * I[gcd(x, y) == 1]
#           = SUM_{y} f(y) * SUM_{z | gcd(x, y)} mu(z)
#           = SUM_{y} f(y) * SUM_{z} mu(z) * I[z | gcd(x, y)]
#           = SUM_{y} f(y) * SUM_{z} mu(z) * I[z|x] * I[z|y]
#           = SUM_{z|x, z|y} f(y) mu(z)
#           = SUM_{z|x} g(z) mu(z)

def solve(T, MOD, N):
    MAX = max(N)

    mu = batch_mobius(MAX)  # mobius
    f = [0]*(MAX+1)         # num ways to reach x from 1
    g = [0]*(MAX+1)         # g(z) up to current x
    f[1] = 1
    g[1] = 1

    for x in range(2, MAX+1):
        factors = factorize_all(x)
        for z in factors:
            if z == x: continue
            f[x] = (f[x] + g[z] * mu[z]) % MOD
        for z in factors: 
            g[z] = (g[z] + f[x]) % MOD
    
    for x in N: print(f[x])


def main():
    T, MOD = list(map(int, input().split()))
    N = [int(input()) for _ in range(T)]
    solve(T, MOD, N)


if __name__ == '__main__':
    main()

