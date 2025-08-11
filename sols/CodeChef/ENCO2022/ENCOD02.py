''' Gamestation
https://www.codechef.com/ENCO2022/problems/ENCOD02
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

def solve(N, X, Y):
    if X > Y: X, Y = Y, X

    def is_ok(n): 
        return n // X + n // Y >= N
    
    res, lo, hi = 0, X, X * N
    while lo <= hi:
        mi = (lo + hi) // 2
        if is_ok(mi):
            res = mi
            hi = mi - 1
        else:
            lo = mi + 1

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        X, Y = list(map(int, input().split()))
        out = solve(N, X, Y)
        print(out)


if __name__ == '__main__':
    main()

