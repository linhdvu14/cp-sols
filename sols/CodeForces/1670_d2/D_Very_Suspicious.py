''' D. Very Suspicious
https://codeforces.com/contest/1670/problem/D
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

# distribute equally to 3 directions
# each intersection adds 2 triangles
def solve(N):
    def is_ok(x):
        a = b = c = x // 3
        if x % 3 >= 1: a += 1
        if x % 3 >= 2: b += 1
        return 2 * (a * b + b * c + c * a) >= N
    
    res, lo, hi = 0, 0, N * 3
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
        out = solve(N)
        print(out)


if __name__ == '__main__':
    main()

