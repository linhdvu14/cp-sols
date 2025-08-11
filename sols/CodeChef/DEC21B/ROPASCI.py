''' Rock Paper Scissors
https://www.codechef.com/DEC21B/problems/ROPASCI
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

WINNER = {'R': 'P', 'P': 'S', 'S': 'R'}

def solve(N, S):
    res = ['']*N
    last = {}
    for i in range(N-1, -1, -1):
        c = S[i]
        p = WINNER[c]
        res[i] = last[c] = last.get(p, c)
    return ''.join(res)


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input().decode().strip()
        out = solve(N, S)
        print(out)


if __name__ == '__main__':
    main()

