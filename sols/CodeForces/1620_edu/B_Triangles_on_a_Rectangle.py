''' B. Triangles on a Rectangle
https://codeforces.com/contest/1620/problem/B
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

def solve(W, H, WP, HP):
    cands = [
        (WP[0][-1]-WP[0][0])*H,
        (WP[1][-1]-WP[1][0])*H,
        (HP[0][-1]-HP[0][0])*W,
        (HP[1][-1]-HP[1][0])*W,
    ]
    return max(cands)


def main():
    T = int(input())
    for _ in range(T):
        W, H = list(map(int, input().split()))
        WP = [list(map(int, input().split()))[1:] for _ in range(2)]
        HP = [list(map(int, input().split()))[1:] for _ in range(2)]
        out = solve(W, H, WP, HP)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

