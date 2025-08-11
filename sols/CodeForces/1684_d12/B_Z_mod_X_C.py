''' B. Z mod X = C
https://codeforces.com/contest/1684/problem/B
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

def solve(a, b, c):
    x, y, z = a + b*c, b, c
    assert x % y == a
    assert y % z == b
    assert z % x == c
    return x, y, z


def main():
    T = int(input())
    for _ in range(T):
        a, b, c = list(map(int, input().split()))
        out = solve(a, b, c)
        print(*out)


if __name__ == '__main__':
    main()

