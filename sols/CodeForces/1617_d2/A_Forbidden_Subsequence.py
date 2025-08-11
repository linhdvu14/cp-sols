''' A. Forbidden Subsequence
https://codeforces.com/contest/1617/problem/A
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

def solve(S, T):
    cnt = [0]*26
    for c in S: cnt[ord(c)-ord('a')] += 1
    res = [chr(i+ord('a'))*c for i, c in enumerate(cnt)]
    if T == 'abc' and res[0] and res[1] and res[2]: res[1], res[2] = res[2], res[1]
    return ''.join(res)


def main():
    T = int(input())
    for _ in range(T):
        S = input().decode().strip()
        T = input().decode().strip()
        out = solve(S, T)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

