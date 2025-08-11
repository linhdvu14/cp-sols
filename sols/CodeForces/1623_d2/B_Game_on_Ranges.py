''' B. Game on Ranges
https://codeforces.com/contest/1623/problem/B
'''

import enum
import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

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

def solve(N, intervals):
    intervals = set(intervals)
    for l, r in intervals:
        if l == r:
            print(l, r, l)
        elif (l+1, r) in intervals:
            print(l, r, l)
        elif (l, r-1) in intervals:
            print(l, r, r)
        else:
            for m in range(l+1, r):
                if (l, m-1) in intervals and (m+1, r) in intervals:
                    print(l, r, m)
                    break
    print()


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        intervals = [tuple(map(int, input().split())) for _ in range(N)]
        solve(N, intervals)


if __name__ == '__main__':
    main()

