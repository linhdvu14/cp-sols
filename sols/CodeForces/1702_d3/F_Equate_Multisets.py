''' F. Equate Multisets
https://codeforces.com/contest/1702/problem/F
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

def solve(N, A, B):
    # keep odd binary prefixes
    ca = {}
    for a in A:
        while a & 1 == 0: a >>= 1
        ca[a] = ca.get(a, 0) + 1
    
    # greedily use b for max possible a
    for b in B:
        while b and not ca.get(b): b >>= 1
        if not b: return 'NO'
        ca[b] -= 1

    return 'YES'


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        out = solve(N, A, B)
        print(out)


if __name__ == '__main__':
    main()

