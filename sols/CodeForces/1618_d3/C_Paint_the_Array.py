''' C. Paint the Array
https://codeforces.com/contest/1618/problem/C
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

def gcd(a, b):  # assume non-neg
    if a < b: a, b = b, a
    while b > 0: a, b = b, a % b
    return a

def gcd_list(A):
    g = A[0]
    for i in range(1, len(A)):
        g = gcd(g, A[i])
    return g

def solve(N, A):
    # even pos
    g = gcd_list([A[i] for i in range(0, N, 2)])
    if g > 1:
        valid = True
        for i in range(1, N, 2):
            if A[i] % g == 0: 
                valid = False
                break
        if valid: return g

    # odd pos
    g = gcd_list([A[i] for i in range(1, N, 2)])
    if g > 1:
        valid = True
        for i in range(0, N, 2):
            if A[i] % g == 0: 
                valid = False
                break
        if valid: return g

    return 0


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

