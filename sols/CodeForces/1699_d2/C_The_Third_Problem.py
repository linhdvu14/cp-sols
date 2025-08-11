''' C. The Third Problem
https://codeforces.com/contest/1699/problem/C
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

MOD = 10**9 + 7

# invariant: after placing 0..n, all intervals with MEX <= n are correct
# note that placing n only affects intervals with MEX == n

# 0 and 1 must be at pos[0] and pos[1]

# if WLOG pos[0] < pos[1] < pos[2], then:
#   * MEX(0..pos[2]-1) == 2 --> 2 cannot be in 0..pos[2]-1
#   * MEX(0..pos[2]) > 2 --> 2 must be in 0..pos[2]
#   --> 2 must be at pos[2]
# if pos[0] < pos[2] < pos[1], then:
#   * MEX(pos[0]..pos[1]) > 2 --> 2 must be in pos[0]..pos[1]
#   * if 2 anywhere in pos[0]..pos[1], all intervals containing 0 and 1 must contain 2 
#   --> no interval has MEX == 2; invariant satisfied

# in general case, maintain min interval containing all fixed indices so far (l, r)
# if WLOG l < r < pos[n], then
#   * MEX(0..r-1) == n --> n cannot be in 0..r-1
#   * MEX(0..r) > n --> n must be in 0..r
#   --> n must be at pos[n]
# if l < pos[n] < r, then
#   * MEX(l..r) > n --> n must be in l..r
#   * if n anywhere in l..r, all intervals containing 0..n-1 must contain n
#   --> no interval has MEX == n; invariant satisfied

def solve(N, A):
    pos = [-1] * N
    for i, a in enumerate(A): pos[a] = i

    res = 1
    l, r = INF, -INF
    for i, p in enumerate(pos):
        if l < p < r: res = (res * (r - l + 1 - i)) % MOD
        l = min(l, p)
        r = max(r, p)

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        print(out)


if __name__ == '__main__':
    main()

