''' C. Permutation Game
https://codeforces.com/contest/1033/problem/C
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

def solve(N, A):
    pos = {a: i for i, a in enumerate(A)}
    win = [0] * N
    for a in range(N-1, 0, -1):
        i = pos[a]
        for j in range(i-a, -1, -a): 
            if A[j] > A[i] and not win[j]: win[i] = 1
        for j in range(i+a, N, a): 
            if A[j] > A[i] and not win[j]: win[i] = 1
    
    return ''.join('A' if w else 'B' for w in win)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    out = solve(N, A)
    print(out)


if __name__ == '__main__':
    main()

