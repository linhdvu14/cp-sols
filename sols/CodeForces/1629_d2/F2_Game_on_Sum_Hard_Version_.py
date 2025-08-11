''' F2. Game on Sum (Hard Version)
https://codeforces.com/contest/1629/problem/F2
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


MAX = 10**6
MOD = 10**9 + 7
FACT, INV_FACT = batch_nCk(MAX, MOD)

HALF_POW = [0] * (MAX + 1)
HALF_POW[0] = 1
for i in range(1, MAX+1): HALF_POW[i] = (HALF_POW[i-1] * (1 + MOD) // 2) % MOD


def solve(N, M, K):
    if K == 0 or M == 0: return 0
    if M == N: return (K * N) % MOD

    # dp[i][i] = K*i
    # dp[i][0] = 0
    # dp[n][m] = (dp[n-1][m-1] + dp[n-1][m]) / 2
    # draw dp board, then 
    # * update from (i, j) flows down to (i+1, j+1) or (i+1, j); except (i, i) only flows to (i+1, j)
    # * each step decays update by 1/2
    # need to aggregate updates from all (i, i) on (N, M)
    res = 0
    for i in range(1, M+1):
        # num ways to go from (i+1, j) to (M, N)
        both, one = N - 1 - i, M - i
        ways = K * i * FACT[both] * INV_FACT[one] * INV_FACT[both - one] % MOD
        res = (res + ways * HALF_POW[N - i]) % MOD
    return res


def main():
    T = int(input())
    for _ in range(T):
        N, M, K = list(map(int, input().split()))
        out = solve(N, M, K)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

