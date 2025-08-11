''' D. Circle Game
https://codeforces.com/contest/1451/problem/D
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

def solve(d, k):
    # max n s.t. (nk, nk) inside circle
    n = s = int((d**2 // 2 // k**2)**0.5)
    for t in (s-1, s, s+1):
        if 2 * (t*k)**2 <= d**2: n = t
    
    if (n*k)**2 + (n*k + k)**2 <= d**2: return 'Ashish'
    return 'Utkarsh'


def main():
    T = int(input())
    for _ in range(T):
        d, k = list(map(int, input().split()))
        out = solve(d, k)
        print(out)


if __name__ == '__main__':
    main()

