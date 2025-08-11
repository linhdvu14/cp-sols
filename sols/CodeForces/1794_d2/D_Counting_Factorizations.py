''' D. Counting Factorizations
https://codeforces.com/contest/1794/problem/D
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def debug(*args):   
    if os.environ.get('debug') in [None, '0']: return
    from inspect import currentframe, getframeinfo
    from re import search
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')

INF = float('inf')

# -----------------------------------------

def precalc(N, mod):
    fact, inv_fact = [1] * (N + 1), [1] * (N + 1)
    for i in range(1, N + 1): fact[i] = i * fact[i - 1] % mod
    inv_fact[-1] = pow(fact[-1], mod - 2, mod)
    for i in range(N - 1, 0, -1): inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod
    return fact, inv_fact


MOD = 998244353
FACT, INV_FACT = precalc(5100, MOD)

def solve(N, A):
    cnt = {}
    for a in A: cnt[a] = cnt.get(a, 0) + 1

    # choose N distinct primes for base
    exp = FACT[N]
    base = [1] + [0] * N
    for a, c in cnt.items():
        prime = a > 1
        for d in range(2, a):
            if d * d > a: break 
            if a % d == 0:
                prime = False 
                break
        if prime:
            for n in range(N, 0, -1):
                base[n] = (base[n] + base[n - 1] * c) % MOD
        exp = exp * INV_FACT[c] % MOD

    return base[N] * exp % MOD


def main():
    N = int(input())
    A = list(map(int, input().split()))
    res = solve(N, A)
    print(res)


if __name__ == '__main__':
    main()
