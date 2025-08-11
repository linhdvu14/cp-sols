''' C. Wrong Addition
https://codeforces.com/contest/1619/problem/C
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

def solve(A, S):
    S = str(S)
    i = len(S)-1
    res = ''
    while A > 0:
        if i < 0: return -1
        A, a = divmod(A, 10)
        if int(S[i]) >= a:
            b = str(int(S[i]) - a)
            if len(b) > 1: return -1
            res += b
            i -= 1
        else:
            if i == 0: return -1
            b = str(int(S[i-1:i+1]) - a)
            if len(b) > 1: return -1
            res += b
            i -= 2
    res = res[::-1]
    if i >= 0: res = S[:i+1] + res
    return int(res)


def main():
    T = int(input())
    for _ in range(T):
        A, S = list(map(int, input().split()))
        out = solve(A, S)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

