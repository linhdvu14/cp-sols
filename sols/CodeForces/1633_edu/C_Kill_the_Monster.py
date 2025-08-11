''' C. Kill the Monster
https://codeforces.com/contest/1633/problem/C
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

# C dies after t1 = (h1 + d2 - 1) // d2
# H dies after t2 = (h2 + d1 - 1) // d1

def solve(h1, d1, h2, d2, k, d, h):
    for a in range(k+1): 
        b = k - a
        t1 = (h1 + a*h + d2 - 1) // d2
        t2 = (h2 + d1 + b*d - 1) // (d1 + b*d)
        if t1 >= t2: return True
    return False


def main():
    T = int(input())
    for _ in range(T):
        h1, d1 = list(map(int, input().split()))
        h2, d2 = list(map(int, input().split()))
        k, d, h = list(map(int, input().split()))
        out = solve(h1, d1, h2, d2, k, d, h)
        print('YES' if out else 'NO')


if __name__ == '__main__':
    main()

