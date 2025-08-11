''' B. Missing Bigram
https://codeforces.com/contest/1618/problem/B
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

def solve(N, bigrams):
    for i in range(N-3):
        if bigrams[i][1] != bigrams[i+1][0]:
            bigrams.insert(i+1, bigrams[i][1]+bigrams[i+1][0])
            break
    res = ''.join(b[0] for b in bigrams) + bigrams[-1][1]
    if len(res) < N: res += 'a'
    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        bigrams = input().decode().strip().split()
        out = solve(N, bigrams)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

