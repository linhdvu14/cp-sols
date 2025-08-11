''' AP Grid
https://www.codechef.com/JUNE222A/problems/APGRID
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

def solve(R, C):
    if R == 1: return [list(range(1, C+1))]
    if C == 1: return [[i] for i in range(1, R+1)]

    # row diff: 1, 2, ..., R; col diff: R+1, R+2, ..., R+C
    # 1            2              3            ...
    # 1 + (R+1)    3 + (R+1)      5 + (R+1)    ...
    # 1 + 2(R+1)   4 + 2(R+1)     7 + 2(R+1)   ...
    A = []
    for r in range(R):
        a = 1 + (R + 1) * r 
        d = r + 1
        row = [a + d * c for c in range(C)]
        A.append(row)
    
    # col diff: 1, 2, ..., C; row diff: C+1, C+2, ..., C+R
    # 1   1 + (C+1)   1 + 2(C+1) ...
    # 2   3 + (C+1)   4 + 2(C+1) ...
    # 3   5 + (C+1)   7 + 2(C+1) ...
    B = []
    for r in range(R):
        a = r + 1 
        d = C + r + 1
        row = [a + d * c for c in range(C)]
        B.append(row)

    return A if A[-1][-1] < B[-1][-1] else B


def main():
    T = int(input())
    for _ in range(T):
        R, C = list(map(int, input().split()))
        grid = solve(R, C)
        for row in grid: print(*row)


if __name__ == '__main__':
    main()

