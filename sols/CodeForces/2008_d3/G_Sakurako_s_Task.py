''' G. Sakurako's Task
https://codeforces.com/contest/2008/problem/G
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

def solve(N, K, A):
    if N == 1: return K - (A[0] >= K)

    g = A[0]
    for a in A: g = gcd(g, a)
    if g == 1: return N + K - 1

    d = min(N, (K - 1) // (g - 1))
    return K + d - 1 + (d < N) #g * d + K - 1 - d * (g - 1) + (d < N)


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        res = solve(N, K, A)
        print(res)



if __name__ == '__main__':
    main()

