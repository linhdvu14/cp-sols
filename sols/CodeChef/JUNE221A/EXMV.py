''' Expected move
https://www.codechef.com/JUNE221A/problems/EXMV
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

# let f(x) = expected number of coin flips if start at x

# for x>1: f(x) = 1 + (f(x-1) + f(x+1)) / 2 -> f(x+1) = 2f(x) - f(x-1) - 2
# f(1) = 0
# f(3) = 2f(2) - f(1) - 2 = 2(f(2) - 1)
# f(4) = 2f(3) - f(2) - 2 = 4f(2) - 4 - f(2) - 2 = 3(f(2) - 2)
# f(5) = 2f(4) - f(3) - 2 = 6(f(2) - 2) - 2(f(2) - 1) - 2 = 4(f(2) - 3)
# f(x) = (x-1) * (f(2) - x + 2)
# f(n) = (n-1) * (f(2) - n + 2)
# f(n-1) = (n-2) * (f(2) - n + 3)

# now f(n) = 1 + (f(n) + f(n-1)) / 2 -> f(n-1) = f(n) - 2
# (n-2) * f(2) - (n-2)(n-3) = (n-1) * f(2) - (n-1)(n-2) - 2
# f(2) = (n-1)(n-2) + 2 - (n-2)(n-3) = 2(n-2) + 2 = 2n - 2


def solve(x, n):
    if x == 1: return 0
    f2 = 2 * (n - 1)
    fx = (x - 1) * (f2 - x + 2)
    return fx
    

def main():
    T = int(input())
    for _ in range(T):
        x, n = list(map(int, input().split()))
        out = solve(x, n)
        print(out)


if __name__ == '__main__':
    main()
