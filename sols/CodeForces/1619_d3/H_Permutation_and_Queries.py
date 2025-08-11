''' H. Permutation and Queries
https://codeforces.com/contest/1619/problem/H
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

# https://codeforces.com/contest/1619/submission/140140161
def main():
    N, Q = list(map(int, input().split()))
    K = int(N**0.5)+1

    # next[i] = p[i]
    next = [-1] + list(map(int, input().split()))

    # prev[p[i]] = i
    prev = [-1]*(N+1)
    for i in range(1, N+1):
        prev[next[i]] = i
    
    # skip[i] = p^k[i]
    skip = [-1]*(N+1)
    for i in range(1, N+1):
        j = i
        for _ in range(K): j = next[j]
        skip[i] = j

    for _ in range(Q):
        t, i, j = list(map(int, input().split()))

        if t == 1:
            i, j = next[i], next[j]
            pi, pj = prev[i], prev[j]

            # swap (prev[i], prev[j]), (next[prev[i]], next[prev[j]])
            prev[i], prev[j] = pj, pi
            next[pi], next[pj] = j, i

            # update skip parent for i..i+K, j..j+K
            pi, pj = i, j
            for _ in range(K): pi, pj = prev[pi], prev[pj]
            for _ in range(K):
                skip[pi], skip[pj] = i, j
                pi, pj = next[pi], next[pj]
                i, j = next[i], next[j]

        else:
            # use skip and next to jump ahead
            for _ in range(j//K): i = skip[i]
            for _ in range(j%K): i = next[i]

            print(i)


if __name__ == '__main__':
    main()

