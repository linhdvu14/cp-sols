''' Valleys and Hills
https://www.codechef.com/DEC21B/problems/VANDH
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

def solve(H, V):
    if V == H: return '10'*(V+1)
    if V < H: return '01'*(V+1) + '0' + '010'*(H-V-1)
    return '10'*(H+1) + '1' + '101'*(V-H-1)

def main():
    T = int(input())
    for _ in range(T):
        H, V = list(map(int, input().split()))
        out = solve(H, V)
        print(len(out))
        print(out)


if __name__ == '__main__':
    main()

