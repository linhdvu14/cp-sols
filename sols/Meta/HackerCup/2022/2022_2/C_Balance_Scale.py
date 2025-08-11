''' Problem C: Balance Scale
https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-2/problems/C
'''

import os, sys
input = sys.stdin.readline
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

def precalc_nCk(N, p):
    fact = [1] * (N+1)  # n! % p
    inv_fact = [1] * (N+1)  # (1 / n!) % p
    for i in range(1, N+1):
        fact[i] = (i * fact[i-1]) % p
        inv_fact[i] = pow(fact[i], p-2, p)
    return fact, inv_fact


MOD = 10**9 + 7
MAX = 6 * 10**6
FACT, INV_FACT = precalc_nCk(MAX, MOD)

def nCk(n, k): 
    if k > n: return 0
    return (FACT[n] * INV_FACT[k] * INV_FACT[n-k]) % MOD


# choose random subset of size (K + 1), find prob heaviest (tie randomly broken) is from batch 1
def solve(N, K, A):
    c1, w1 = A[0]
    
    s = m = l = 0
    for c, w in A:
        if w < w1: s += c 
        elif w == w1: m += c
        else: l += c 
    
    # num subsets of size (K + 1)
    tot = nCk(s + m + l, K + 1)
    
    # num subsets of size (K + 1) s.t. max weight is w1
    x = nCk(s + m, K + 1) - nCk(s, K + 1)

    # prob of picking subset with max weight w1
    p1 = x * pow(tot, MOD - 2, MOD)

    # prob of remain cookie being from batch 1, having chosen subset with max weight w1
    p2 = c1 * pow(m, MOD - 2, MOD)

    return (p1 * p2) % MOD



def main():
    T = int(input())
    for t in range(T):
        N, K = list(map(int, input().split()))
        A = [list(map(int, input().split())) for _ in range(N)]
        res = solve(N, K, A)
        print(f'Case #{t+1}: {res}')


if __name__ == '__main__':
    main()

