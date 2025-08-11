''' E. Rubik String
https://codeforces.com/gym/103449/problem/E
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

OPP = {'W': 'WY', 'Y': 'YW', 'B': 'BG', 'G': 'GB', 'O': 'OR', 'R': 'RO'}

def solve(N, S):
    res = cnt = 0
    for i in range(1, N):
        if S[i] not in OPP[S[i-1]]:
            res += (cnt + 1) // 2
            cnt = 0
        else:
            cnt += 1
    res += (cnt + 1) // 2
    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input().decode().strip()
        out = solve(N, S)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

