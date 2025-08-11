''' D. Cut and Stick
https://codeforces.com/contest/1514/problem/D
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

from bisect import bisect_left, bisect_right
BITS = 19

# https://codeforces.com/contest/1514/submission/113641850
# all bit pos occurring in > 1/2 eles must appear in majority ele

def main():
    N, Q = list(map(int, input().split()))
    A = list(map(int, input().split()))

    pos = [[] for _ in range(N)]
    pref = [[0] * (N+1) for _ in range(BITS)]
    for i, a in enumerate(A):
        a -= 1
        pos[a].append(i)
        for b in range(BITS):
            pref[b][i+1] = pref[b][i] + ((a >> b) & 1)

    res = [1] * Q
    for qi in range(Q):
        l, r = list(map(int, input().split()))
        l -= 1; r -= 1
        ln = r - l + 1
        
        majority = 0
        for b in range(BITS):
            if pref[b][r+1] - pref[b][l] > (ln + 1) // 2:
                majority |= 1 << b 
        
        cnt = bisect_right(pos[majority], r) - bisect_left(pos[majority], l)
        if cnt > (ln + 1) // 2:
            res[qi] = 2 * cnt - ln

    print(*res, sep='\n')


if __name__ == '__main__':
    main()

