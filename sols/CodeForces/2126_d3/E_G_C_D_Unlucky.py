''' E. G-C-D, Unlucky!
https://codeforces.com/contest/2126/problem/E
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

from inspect import currentframe, getframeinfo
from re import search
DEBUG = os.environ.get('debug') not in [None, '0']

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
from math import gcd

def solve(N, P, S):
    A = [p * s // gcd(p, s) for p, s in zip(P, S)]

    g = 0
    for i in range(N):
        g = gcd(g, A[i])
        if g != P[i]: return 'NO'

    g = 0
    for i in range(N - 1, -1, -1):
        g = gcd(g, A[i])
        if g != S[i]: return 'NO'

    return 'YES'


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        P = list(map(int, input().split()))
        S = list(map(int, input().split()))
        res = solve(N, P, S)
        print(res)


if __name__ == '__main__':
    main()

