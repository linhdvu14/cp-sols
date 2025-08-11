''' F. Interacdive Problem
https://codeforces.com/contest/1624/problem/F
'''

# to test: 
# pypy3 template.py
# or: python interactive_runner.py python local_testing_tool.py 0 -- python3 a.py

import functools
import os, sys
input = sys.stdin.readline  # io.BytesIO(os.read(0,os.fstat(0).st_size)).readline doesn't work
output = functools.partial(print, flush=True)

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

def query(c):
    output(f'+ {c}')
    return int(input())

def main():
    N = int(input())

    d, lo, hi = 0, 1, N-1
    while lo < hi:
        mi = (lo+hi+1) // 2
        q = N - mi
        d2 = query(q)  # lo..mi-1 under, mi..hi overflow
        if d2 == d:
            hi = mi - 1
        else:
            lo = mi
        lo = (lo+q) % N
        hi = (hi+q) % N
        d = d2

    output(f'! {d*N + lo}')

    
 
if __name__ == '__main__':
    main()

