''' C. Kuroni and Impossible Calculation
https://codeforces.com/contest/1305/problem/C
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

def solve(N, M, A):
    if N > M: return 0  # must be a pair a % M == b % M
    res = 1
    for i in range(N):
        for j in range(i):
            res = (res * abs(A[i] - A[j])) % M
    return res


def main():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    out = solve(N, M, A)
    print(out)


if __name__ == '__main__':
    main()

