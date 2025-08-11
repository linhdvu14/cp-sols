''' F. Let's Play the Hat?
https://codeforces.com/contest/1619/problem/F
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

def solve(N, M, K):
    numB = N%M          
    numS = M - N%M
    sizeB = N//M + 1
    sizeS = N//M
    i = 0  # round robin assign i..i+sizeB-1 to big tables
    for _ in range(K):
        for j in range(numB):
            g = [(i + sizeB*j + k) % N + 1 for k in range(sizeB)]
            print(sizeB, end=' ')
            print(*g)
        for j in range(numS):
            g = [(i + numB*sizeB + j*sizeS + k) % N + 1 for k in range(sizeS)]
            print(sizeS, end=' ')
            print(*g)
        i = (i + numB*sizeB) % N
    print()


def main():
    T = int(input())
    for _ in range(T):
        N, M, K = list(map(int, input().split()))
        solve(N, M, K)


if __name__ == '__main__':
    main()

