''' A. Grass Field
https://codeforces.com/contest/1701/problem/A
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

def solve(A, B):
    S = sum(A) + sum(B)
    if S == 0: return 0
    if S == 4: return 2
    return 1


def main():
    T = int(input())
    for _ in range(T):
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        out = solve(A, B)
        print(out)


if __name__ == '__main__':
    main()

