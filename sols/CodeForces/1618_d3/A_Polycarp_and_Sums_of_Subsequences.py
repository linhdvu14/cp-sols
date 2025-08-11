''' A. Polycarp and Sums of Subsequences
https://codeforces.com/contest/1618/problem/A
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

def solve(A):
    a, b = A[0], A[1]
    c = A[-1] - a - b
    return [a, b, c]


def main():
    T = int(input())
    for _ in range(T):
        A = list(map(int, input().split()))
        out = solve(A)
        print(*out)


if __name__ == '__main__':
    main()

