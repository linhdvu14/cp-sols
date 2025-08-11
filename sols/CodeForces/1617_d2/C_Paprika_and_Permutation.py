''' C. Paprika and Permutation
https://codeforces.com/contest/1617/problem/C
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
    count = {}
    for a in A: count[a] = count.get(a, 0) + 1
    
    small = []
    for a in range(1, N+1):
        if count.get(a, 0) > 0:
            count[a] -= 1
        else:
            small.append(a)
    
    big = []    
    for a, c in count.items():
        big += [a]*c
    
    small.sort()
    big.sort()
    for s, b in zip(small, big):
        if b <= 2*s: return -1
    return len(small)
        


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

