''' D. Fixed Point Guessing
https://codeforces.com/contest/1698/problem/D
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

# for int dict key
from random import randrange
RAND = randrange(1 << 62)
def conv(x): return x ^ RAND

INF = float('inf')

# -----------------------------------------

def ask(l, r):
    output(f'? {l+1} {r+1}')
    res = list(map(int, input().split()))
    return res

# segment containing static ele will have odd num eles belonging

def solve():
    N = int(input())
    lo, hi = 0, N - 1
    while lo < hi:
        mi = (lo + hi) // 2
        left = ask(lo, mi)
        good = sum(1 for v in left if lo+1 <= v <= mi+1)
        if good % 2: hi = mi
        else: lo = mi + 1

    output(f'! {lo+1}')


def main():
    T = int(input())
    for _ in range(T):
        solve()
    
 
if __name__ == '__main__':
    main()