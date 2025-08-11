''' A. Equal or Not Equal
https://codeforces.com/contest/1620/problem/A
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

def solve1(S):
    n = sum(1 for c in S[:-1] if c=='N')
    if n == 0: return S[-1] == 'E'
    if n == 1: return S[-1] == 'N'
    return True


def solve(S):
    c = S.count('N')
    return c != 1


def main():
    T = int(input())
    for _ in range(T):
        S = input().decode().strip()
        out = solve(S)
        print('YES' if out else 'NO')


if __name__ == '__main__':
    main()

