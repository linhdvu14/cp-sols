''' D. X-Magic Pair
https://codeforces.com/contest/1612/problem/D
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

# a < b --> (b-a, b) --> (a, b) or (a, b-a) --> X
#       --> (b-a, a)

def solve(a, b, x):
    if a > b: a, b = b, a
    while a > 0 and b >= x:
        if (b - x) % a == 0: return True
        a, b = b % a, a
    return False


def main():
    T = int(input())
    for _ in range(T):
        a, b, x = list(map(int, input().split()))
        out = solve(a, b, x)
        print('YES' if out else 'NO')


if __name__ == '__main__':
    main()

