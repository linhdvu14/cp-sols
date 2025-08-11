''' Prefix Suffix Distinct
https://www.codechef.com/COOK142A/problems/PRFSUFDSTNCT
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

# P non-decreasing, S non-increasing; difference == 1
# P[0] == S[-1] == 1
# P[-1] == S[0]
# let PI = indices of first instances (from P), SI = indices of last instances (from S)
# PI & SI = indices of unique values

def solve(N, P, S):
    if P != sorted(P): return 'NO'
    if S != sorted(S, reverse=True): return 'NO'
    if P[-1] != S[0] or P[0] != 1 or S[-1] != 1: return 'NO'
    
    PI = set()
    prev = 0
    for i, v in enumerate(P):
        if v != prev: 
            if v - prev != 1: return 'NO'
            PI.add(i)
        prev = v 
    
    SI = set()
    prev = S[0] + 1
    for i, v in enumerate(S):
        if v != prev:
            if prev - v != 1: return 'NO'
            SI.add(i)
        prev = v
    
    inter = PI & SI
    PI = sorted(list(PI - inter))
    SI = sorted(list(SI - inter))

    for (i, j) in zip(PI, SI):
        if i >= j: return 'NO'
    
    return 'YES'


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        P = list(map(int, input().split()))
        S = list(map(int, input().split()))
        out = solve(N, P, S)
        print(out)


if __name__ == '__main__':
    main()

