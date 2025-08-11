''' Possible GCD
https://www.codechef.com/JUNE221A/problems/DISTGCD
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

# gcd(a-b, a+x) for any x >= 0
# gcd(a-b, x) for any x >= a
# -> num divisors of a-b

def solve(a, b):
    c = abs(a - b)
    res = 0
    d = 1
    while d * d < c:
        if c % d == 0: res += 2
        d += 1
    if d * d == c: res += 1
    return res
    

def main():
    T = int(input())
    for _ in range(T):
        a, b = list(map(int, input().split()))
        out = solve(a, b)
        print(out)


if __name__ == '__main__':
    main()
