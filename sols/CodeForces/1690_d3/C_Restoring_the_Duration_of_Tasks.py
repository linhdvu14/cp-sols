''' C. Restoring the Duration of Tasks
https://codeforces.com/contest/1690/problem/C
'''

import io, os, sys
from operator import ilshift
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

def solve(N, B, E):
    res = [-1] * N
    t = 0
    for i, (b, e) in enumerate(zip(B, E)):
        t = max(t, b)
        res[i] = e - t
        t = e
    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        B = list(map(int, input().split()))
        E = list(map(int, input().split()))
        out = solve(N, B, E)
        print(*out)


if __name__ == '__main__':
    main()

