''' C. Baby Ehab Partitions Again
https://codeforces.com/contest/1516/problem/C
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

from math import gcd

def solve(N, A):
    g = 0
    for a in A: g = gcd(g, a)
    for i in range(N): A[i] //= g 
    S = sum(A)

    # check if originally can't partition
    dp = [0] * (S + 1)
    dp[0] = 1
    for a in A:
        ndp = [0] * (S + 1)
        for i in range(S + 1):
            if dp[i]: ndp[i] = ndp[i + a] = 1
        dp = ndp 
    
    if S % 2 or not dp[S // 2]: return [0]

    # rm any odd ele
    for i, a in enumerate(A):
        if a % 2: return [1, i+1]



def main():
    N = int(input())
    A = list(map(int, input().split()))
    out = solve(N, A)
    print(*out, sep='\n')


if __name__ == '__main__':
    main()

