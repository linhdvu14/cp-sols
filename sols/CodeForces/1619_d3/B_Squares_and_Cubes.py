''' B. Squares and Cubes
https://codeforces.com/contest/1619/problem/B
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

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

def solve(N):
    c2 = c3 = c6 = 1
    while (c2+1)**2 <= N: c2 += 1
    while (c3+1)**3 <= N: c3 += 1        
    while (c6+1)**6 <= N: c6 += 1        
    return c2 + c3 - c6


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        out = solve(N)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

