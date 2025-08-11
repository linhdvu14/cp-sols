''' E. Singers' Tour
https://codeforces.com/contest/1618/problem/E
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

def solve(N, B):
    # sum of a[i]
    S = sum(B)
    m = N*(N+1) // 2
    if S % m != 0: return 'NO', []
    S //= m

    # b[1] - b[0] = S - N*a[1]
    res = [0]*N
    for i1 in range(N):
        i0 = (i1-1) % N
        Na1 = S + B[i0] - B[i1]
        if Na1 <= 0 or Na1 % N != 0: return 'NO', []
        res[i1] = Na1 // N

    return 'YES', res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        B = list(map(int, input().split()))
        s, arr = solve(N, B)
        print(s)
        if arr: print(*arr)


if __name__ == '__main__':
    main()

