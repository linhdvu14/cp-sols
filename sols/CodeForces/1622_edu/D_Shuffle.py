''' D. Shuffle
https://codeforces.com/contest/1622/problem/D
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

def batch_nCk(N, p):
    ''' precompute for binomial coefficient up to C(N, N) % p
    C(N, k) mod p = fact[n] * inv_fact[k] * inv_fact[n-k]
    '''
    fact = [1]*(N+1)  # n! % p
    for i in range(1, N+1):
        fact[i] = (i * fact[i-1]) % p
 
    inv_fact = [1]*(N+1)  # (1 / n!) % p
    for i in range(1, N+1):
        inv_fact[i] = pow(fact[i], p-2, p)
    
    return fact, inv_fact
 
 
MOD = 998244353
MAX = 5005
FACT, INV_FACT = batch_nCk(MAX, MOD)


# say S becomes S' after shuffling a substring
# then S' must have a minimal mid-segment that's different from S
# formally there exists i, j s.t. S[:i] == S'[:i], S[j+1:] == S'[j+1:], S[i] != S'[i], S[j] != S'[j]
 
# different resultant S' are uniquely identified by their i, j
# a segment i..j is valid (can be substring of a substring with exactly K 1s) if 
# * S has >= K 1s
# * S[i..j] has <= K 1s

def solve_N2(N, K, S):
    if K == 0 or sum(S) < K: return 1
 
    res = 1
    for i in range(N):
        cnt = 0
        for j in range(i, N):
            if S[j] == 1: cnt += 1
            if cnt > K: break
            mid_cnt = cnt - (S[i] == 0) - (S[j] == 0)
            if 0 <= mid_cnt <= j - i - 1:
                res += FACT[j - i - 1] * INV_FACT[mid_cnt] * INV_FACT[j - i - 1 - mid_cnt]
                res %= MOD
 
    return res
 

# let j be the first idx where S' differs from S
# formally S[:j] == S'[:j], S[j] != S'[j]
# then different resultant S' are uniquely identified by their j
# a segment i..j is valid if it has <= K 1s

def solve_N(N, K, S):
    if K == 0 or sum(S) < K: return 1

    res = 1
    cnt = i = 0
    for j, n in enumerate(S):
        cnt += n
        while cnt > K: 
            cnt -= S[i]
            i += 1

        one, zero = cnt, j - i + 1 - cnt
        if n == 0: one -= 1
        if n == 1: zero -= 1

        if one < 0 or zero < 0: continue
        res += FACT[one+zero] * INV_FACT[one] * INV_FACT[zero]
        res %= MOD

    return res

solve = solve_N

def main():
    N, K = list(map(int, input().split()))
    S = list(map(int, list(input().decode().strip())))
    out = solve(N, K, S)
    output(f'{out}\n')
 

if __name__ == '__main__':
    main()
 
