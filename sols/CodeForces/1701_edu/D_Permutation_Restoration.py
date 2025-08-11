''' D. Permutation Restoration
https://codeforces.com/contest/1701/problem/D
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

from heapq import heappush, heappop

def solve(N, B):
    segs = []
    for n, rem in enumerate(B):
        n += 1
        if rem == 0: 
            segs.append((n+1, N, n))
        else:
            r = n // rem
            l = n // (rem + 1) + 1
            segs.append((l, r, n))  # idx n must contain val l..r

    # take first ending seg
    segs.sort(reverse=True)
    res = [0] * N
    avail = []
    for i in range(1, N + 1):
        while segs and segs[-1][0] <= i: 
            l, r, n = segs.pop()
            heappush(avail, (r, n))
        _, n = heappop(avail)
        res[n-1] = i

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        B = list(map(int, input().split()))
        out = solve(N, B)
        print(*out)


if __name__ == '__main__':
    main()


