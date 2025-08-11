''' B. GCD Problem
https://codeforces.com/contest/1617/problem/B
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
    # k, k+1, 1
    if N % 2 == 0: return [(N-1)//2, (N-1)//2 + 1, 1]

    # 2k-1, 2k+1, 1
    if N % 4 == 1: return [(N-1)//2 - 1, (N-1)//2 + 1, 1]

    # 2k-1, 2k+3, 1
    return [(N-1)//2 - 2, (N-1)//2 + 2, 1]


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        out = solve(N)
        print(*out)


if __name__ == '__main__':
    main()

