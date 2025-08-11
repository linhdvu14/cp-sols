''' F. Reverse
https://codeforces.com/contest/1618/problem/F
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

def is_ok(x, y):
    '''check if y has form 1..1x1..1 (possibly zero 1)'''
    if len(y) < len(x): return False
    nx, ny = len(x), len(y)
    for i in range(ny-nx+1):
        if i>0 and y[i-1] == '0': return False
        if y[i:i+nx] == x and all(c=='1' for c in '1'+y[i+nx:]): return True
    return False


def solve(x, y):
    if x == y: return True
    x, y = bin(x)[2:], bin(y)[2:]

    if x[-1] == '1': 
        return is_ok(x, y) or is_ok(x[::-1], y)

    # first op appends 1
    if is_ok(x+'1', y) or is_ok('1' + x[::-1], y):
        return True

    # first op appends 0 -> strip all 0
    end = len(x)
    while end > 0 and x[end-1] == '0': end -= 1
    x = x[:end]
    return is_ok(x, y) or is_ok(x[::-1], y)

def main():
    x, y = list(map(int, input().split()))
    out = solve(x, y)
    print('YES' if out else 'NO')

if __name__ == '__main__':
    main()

