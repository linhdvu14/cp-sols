''' A. Optimal Path
https://codeforces.com/contest/1700/problem/A
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

# (1, 1) -> (1, C) -> (R, C)
def solve(R, C):
    return C * (C+1) // 2 + C * R * (R + 1) // 2 - C

def main():
    T = int(input())
    for _ in range(T):
        R, C = list(map(int, input().split()))
        out = solve(R, C)
        print(out)


if __name__ == '__main__':
    main()

