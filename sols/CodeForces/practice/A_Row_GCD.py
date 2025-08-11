''' A. Row GCD
https://codeforces.com/contest/1458/problem/A
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

# gcd(a1 + b, a2 + b, ..., an + b) = gcd(a1 + b, a2-a1, a3-a1, .., an-a1)

def solve(N, M, A, B):
    g = 0
    for i in range(1, N): g = gcd(g, A[i] - A[0])
    return [gcd(g, A[0] + B[j]) for j in range(M)]


def main():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    out = solve(N, M, A, B)
    print(*out)


if __name__ == '__main__':
    main()

