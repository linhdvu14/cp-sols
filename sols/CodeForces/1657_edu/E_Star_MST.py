''' E. Star MST
https://codeforces.com/contest/1657/problem/E
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

MOD = 998244353

def precalc_nCk(N, p):
    ''' precompute binomial coefficients to calc up to C(N, N) % p
    C(N, k) mod p = fact[n] * inv_fact[k] * inv_fact[n-k]
    '''
    fact = [1] * (N+1)  # n! % p
    for i in range(1, N+1):
        fact[i] = (i * fact[i-1]) % p

    inv_fact = [1] * (N+1)  # (1 / n!) % p
    for i in range(1, N+1):
        inv_fact[i] = pow(fact[i], p-2, p)
    
    return fact, inv_fact

# grow mst from vertex 1 ~ kruskal
# stage k adds edges (1, u) with weight k for k=1..N
# let V = set of vertices already connected to 1, U = remaining vertices
# to add edges (1, u) with weight k:
# * all edges (1, v) have weight <= k
# * all edges (~1, u) have weight >= k --> include (u, u') and (v, u)

# dp[n][k] = num valid graphs with n vertices connected to 1, all edge weights <= k
#          = SUM_{i=0..n} C(n, i) * dp[n-i][k-1] * (K-k+1)^(i*(i-1)/2 + i*(n-i))
# (add i edges (1, u) in stage k; N-i is size of V)
# ans is dp[N-1][K]

def solve(N, K):
    fact, inv_fact = precalc_nCk(N, MOD)

    dp = [[0]*(K+1) for _ in range(N)]
    dp[0][0] = 1

    for k in range(1, K+1):
        for n in range(N): 
            for i in range(n+1):
                dp[n][k] += fact[n] * inv_fact[i] * inv_fact[n-i] * dp[n-i][k-1] * pow(K-k+1, i*(i-1)//2 + i*(n-i), MOD)
                dp[n][k] %= MOD

    return dp[N-1][K] % MOD


def main():
    N, K = list(map(int, input().split()))
    out = solve(N, K)
    print(out)


if __name__ == '__main__':
    main()

