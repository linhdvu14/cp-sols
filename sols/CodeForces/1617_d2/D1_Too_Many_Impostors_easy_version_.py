''' D1. Too Many Impostors (easy version)
https://codeforces.com/contest/1617/problem/D1
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
    from varname.core import argname
    from inspect import currentframe

def debug(var, *more_vars):
    if not DEBUG: return
    var_names = argname('var', '*more_vars', func=debug)
    values = (var, *more_vars)
    name_and_values = [f'{var_name}={value}'  for var_name, value in zip(var_names, values)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(name_and_values)}')


INF = float('inf')

# -----------------------------------------

def solve():
    N = int(input())

    output(f'? 1 2 3')
    prev = int(input())
    idx = -1
    for i in range(2, N):
        output(f'? {i} {i+1} {i+2}')
        cur = int(input())
        if cur != prev:
            idx = i  # i and i+1 are different
            break
    
    res = [-1]*(N+1)
    pos0 = pos1 = -1
    for i in range(1, N+1):
        if i == idx or i == idx+1: continue
        output(f'? {i} {idx} {idx+1}')
        res[i] = c = int(input())
        if c == 0 and pos0 == -1: pos0 = i
        if c == 1 and pos1 == -1: pos1 = i
    
    output(f'? {idx} {pos0} {pos1}')
    res[idx] = int(input())
    res[idx+1] = 1 - res[idx]

    res = [i for i, c in enumerate(res) if c == 0]
    n, s = len(res), ' '.join(map(str, res))
    output(f'! {n} {s}')


def main():
    T = int(input())
    for _ in range(T):
        solve()
    
 
if __name__ == '__main__':
    main()