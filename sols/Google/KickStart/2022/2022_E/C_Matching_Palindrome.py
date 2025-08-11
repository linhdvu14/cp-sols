''' Matching Palindrome
https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb0f5/0000000000ba82c5 
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

BASE = 31
MOD = 10**9 + 7

# split S into 2 palindromes P1 + P2 s.t. min length P1
# then ans is P1[::-1]
def solve(N, S):
    S = [ord(c) - ord('a') for c in S]
    
    la = lb = S[0]
    ra = rb = 0
    for i in range(1, N): ra = (ra * BASE + S[i]) % MOD
    for i in range(N - 1): rb = (rb * BASE + S[i]) % MOD
    
    for i in range(1, N):
        if la == lb and ra == rb: return ''.join(chr(c + ord('a')) for c in S[:i][::-1])
        la = (la * BASE + S[i]) % MOD
        lb = (lb + S[N - 1 - i] * pow(BASE, i, MOD)) % MOD
        ra = (ra - S[i] * pow(BASE, N - 1 - i, MOD)) % MOD 
        rb = ((rb - S[N - 1 - i]) * pow(BASE, MOD - 2, MOD)) % MOD
    
    return ''.join(chr(c + ord('a')) for c in S[::-1])


def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        S = input().decode().strip()
        out = solve(N, S)
        print(f'Case #{t+1}: {out}')


if __name__ == '__main__':
    main()

