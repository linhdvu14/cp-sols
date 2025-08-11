''' B1. Send Boxes to Alice (Easy Version)
https://codeforces.com/contest/1254/problem/B1
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

# iterate over each k
# best to create num_ones // k boxes of k chocolates each
# for each box, best to aggregate to median of k consecutive points

def solve(N, A):
    A = [i + 1 for i, a in enumerate(A) if a == 1]
    N = len(A)
    if N == 1: return -1

    pref = [0]
    for a in A: pref.append(pref[-1] + a)

    # min cost to aggregate l..r to median
    def cost(l, r):
        m = (l + r) // 2
        left = A[m] * (m - l) - (pref[m] - pref[l])
        right = pref[r + 1] - pref[m + 1] - A[m] * (r - m)
        return left + right

    res = INF
    k1 = 1
    while k1 * k1 <= N:
        k2, r = divmod(N, k1)
        if r == 0:
            for k in [k1, k2]:
                if k == 1: continue
                cand = sum(cost(l, l+k-1) for l in range(0, N, k))
                res = min(res, cand)
        k1 += 1

    return res


def main():
    N = int(input())
    A = list(map(int, input().split()))
    out = solve(N, A)
    print(out)


if __name__ == '__main__':
    main()

