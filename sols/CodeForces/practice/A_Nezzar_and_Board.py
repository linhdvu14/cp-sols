''' A. Nezzar and Board
https://codeforces.com/contest/1477/problem/A
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

# a, a+d --> a-d, a, a+d, a+2d
# not possible if there is an arithmetic sequence that contains all eles but not K

# fix A[0] at 0, make lattice by picking any pair (a, a+d) and mark all (a + nd)
# process stops when all corners have same distance d apart
# then K is reachable iff K % d == 0

def solve(N, K, A):
    g = 0
    for i in range(1, N): g = gcd(g, A[i] - A[0])
    return 'YES' if (K - A[0]) % g == 0 else 'NO'


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        out = solve(N, K, A)
        print(out)


if __name__ == '__main__':
    main()

