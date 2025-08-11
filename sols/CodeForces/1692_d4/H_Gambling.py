''' H. Gambling
https://codeforces.com/contest/1692/problem/H
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


INF = float('inf')

# -----------------------------------------

from random import randrange
RAND = randrange(1 << 62)
def conv(x): return x ^ RAND

# find sequence with max(count max occurrences - count other occurrences)
# first and last ele of sequence must equal max occurrence value 
def solve(N, A):
    idx = {}
    for i, a in enumerate(A):
        a = conv(a)
        if a not in idx: idx[a] = []
        idx[a].append(i)
    
    res = (1, A[0], 1, 1)
    for k, pos in idx.items():
        mn = (0, pos[0] + 1)
        for i, a in enumerate(pos):
            res = max(res, (2 * (i + 1) - a - 1 - mn[0], conv(k), mn[1], a + 1))
            mn = min(mn, (2 * i - a, a + 1))
 
    return res[1:]


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        print(*out)


if __name__ == '__main__':
    main()

