''' A. Hard Way
https://codeforces.com/contest/1642/problem/A
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

def solve(x1, y1, x2, y2, x3, y3):
    if y1 == y2: return 0 if y1 < y3 else abs(x1 - x2)
    if y2 == y3: return 0 if y2 < y1 else abs(x2 - x3)
    if y3 == y1: return 0 if y3 < y2 else abs(x3 - x1)
    return 0


def main():
    T = int(input())
    for _ in range(T):
        x1, y1 = map(int, input().split())
        x2, y2 = map(int, input().split())
        x3, y3 = map(int, input().split())
        out = solve(x1, y1, x2, y2, x3, y3)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

