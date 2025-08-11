''' D. Exact Change
https://codeforces.com/contest/1620/problem/D
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

def solve(N, A):
    res = INF

    # coin set has at most 2 ones, 2 twos
    for c1 in range(3):
        for c2 in range(3):
            c3 = 0  # min threes needed
            for a in A:
                a3 = INF
                for a1 in range(c1+1):
                    for a2 in range(c2+1):
                        v = a - a1 - 2*a2
                        if v >= 0 and v % 3 == 0:
                            a3 = min(a3, v//3)
                c3 = max(c3, a3)
            res = min(res, c1 + c2 + c3)

    return res




def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

