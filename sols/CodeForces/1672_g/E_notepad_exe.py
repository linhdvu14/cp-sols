''' E. notepad.exe
https://codeforces.com/contest/1672/problem/E
'''


# to test: 
# pypy3 template.py
# or: python3 interactive_runner.py python3 local_testing_tool.py 0 -- python3 a.py

import functools
import os, sys
input = sys.stdin.readline  # strip() if str; io.BytesIO(os.read(0,os.fstat(0).st_size)).readline doesn't work
output = functools.partial(print, flush=True)

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

def ask(w):
    output(f'? {w}')
    res = int(input())
    assert res != -1
    return res


def solve():
    N = int(input())

    # find min length to fit one line: L = total length + N - 1
    L, lo, hi = 1, 1, N*2005
    while lo <= hi:
        mi = (lo + hi) // 2
        h = ask(mi)
        if h == 1:
            L = mi
            hi = mi - 1
        else:  # w too small
            lo = mi + 1
    
    # for given h, cand area in L-h+1..L and divisible by h
    res = L
    for h in range(2, N+1):
        w = L // h
        h = ask(w)
        if h > 0: res = min(res, h * w)

    output(f'! {res}')


def main():
    solve()
    
 
if __name__ == '__main__':
    main()