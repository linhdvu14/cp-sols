''' D. MEX Sequences
https://codeforces.com/contest/1613/problem/D
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
MOD = 998244353

def solve(N, A):	
    # B[a] = num subsequences so far with val set {0,1,...,a}
    # C[a] = num subsequences so far with val set {0,1,...,a-2,a}
    B = [0]*(N+10)
    C = [0]*(N+10)
    B[-1] = 1

    # count num valid subsequences ending at each a:
    # * mex=a-1: {0,...,a-2}, {0,...,a-2,a}
    # * mex=a+1: {0,...,a-1}, {0,...,a}, {1,...,a,a+2}
    res = 0
    for a in A:
        add_b = B[a] + B[a-1]
        add_c = B[a-2] + C[a]
        add_c2 = C[a+2]

        B[a] = (B[a] + add_b) % MOD
        C[a] = (C[a] + add_c) % MOD
        C[a+2] = (C[a+2] + add_c2) % MOD

        res = (res + add_b + add_c + add_c2) % MOD

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

