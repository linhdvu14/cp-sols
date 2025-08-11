''' C - Robot Takahashi 
https://atcoder.jp/contests/abc257/tasks/abc257_c
'''

import io, os, sys
from re import I
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
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

def solve(N, A, W):
    idx = sorted(list(range(N)), key=lambda i: W[i])
    A = [A[i] for i in idx]
    W = [W[i] for i in idx]

    tot = sum(A)
    res = min(tot, N - tot)
    cur = i = 0
    while i < N:
        j = i 
        while j < N and W[j] == W[i]:
            cur += A[j]
            j += 1
        cand = cur + N - tot - (j - cur)
        res = min(res, cand)
        i = j

    return N - res


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, list(input().decode().strip())))
    W = list(map(int, input().split()))

    out = solve(N, A, W)
    print(out)

