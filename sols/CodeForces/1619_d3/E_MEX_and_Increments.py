''' E. MEX and Increments
https://codeforces.com/contest/1619/problem/E
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
    counts = [0]*(N+1)
    for a in A: counts[a] += 1

    res = [-1]*(N+1)
    stack = []  # (num, dup)
    s = 0
    for a, cnt in enumerate(counts):
        # cover 0..a-1
        if a > 0 and counts[a-1] == 0:
            if not stack: break
            pa, pcnt = stack.pop()
            s += a-1 - pa
            if pcnt > 1: stack.append((pa, pcnt-1))
        
        # erase a
        res[a] = s + cnt
        if cnt > 1: stack.append((a, cnt-1))

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        print(*out)


if __name__ == '__main__':
    main()

