''' C - Graph Isomorphism
https://atcoder.jp/contests/abc232/tasks/abc232_a
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

from itertools import permutations

def main():
    N, M = list(map(int, input().split()))

    A = sorted([sorted(list(map(int, input().split()))) for _ in range(M)])
    B = [list(map(int, input().split())) for _ in range(M)]

    perms = permutations(list(range(1, N+1)))
    for perm in perms:
        B2 = sorted([sorted([perm[b[0]-1], perm[b[1]-1]]) for b in B])
        if A == B2: 
            print('Yes')
            return

    print('No')


if __name__ == '__main__':
    main()

