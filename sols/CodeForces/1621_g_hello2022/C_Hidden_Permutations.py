''' C. Hidden Permutations
https://codeforces.com/contest/1621/problem/C
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

def query(x):
    output(f'? {x}')
    return int(input())

# each pos cycles through orig permutation
def solve():
    N = int(input())
    P = [-1] * (N+1)

    idx = 1
    while True:
        while idx <= N and P[idx] != -1: idx += 1
        if idx > N: break
        start = u = query(idx)
        while True:
            P[u] = query(idx)
            u = P[u]
            if u == start: break

    s = ' '.join(map(str, P[1:]))
    output(f'! {s}')


def main():
    T = int(input())
    for _ in range(T):
        solve()
    
 
if __name__ == '__main__':
    main()