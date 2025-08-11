'''  Problem 1. Lonely Photo '''

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

def solve(N, S):
    res = 0
    for i, c in enumerate(S):
        l = r = 0
        while i-l > 0 and S[i-l-1] != c: l += 1
        while i+r < N-1 and S[i+r+1] != c: r += 1
        res += (l+1)*(r+1) - 1
        if l > 0: res -= 1
        if r > 0: res -= 1

    return res


def main():
    N = int(input())
    S = input().decode().strip()
    out = solve(N, S)
    print(out)


if __name__ == '__main__':
    main()

