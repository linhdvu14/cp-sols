''' D. New Year's Problem
https://codeforces.com/contest/1619/problem/D
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

from heapq import heappush, heappop

# rank each friend's shop preference
# init frontier with each friend's top shop
# loosen frontier until a shop is repeated
def solve(M, N, P):
    used = [0]*M
    heap = []

    res = INF
    for n in range(N):
        mx = max(P[m][n] for m in range(M))
        for m in range(M):
            v = P[m][n]
            if v == mx:
                used[m] += 1
                res = min(res, v)
            else:
                heappush(heap, (-v, m))
    
    if any(c > 1 for c in used): return res

    while heap:
        v, m = heappop(heap)
        res = min(res, -v)
        used[m] += 1
        if used[m] > 1: break

    return res


def main():
    T = int(input())
    for _ in range(T):
        _ = input()
        M, N = list(map(int, input().split()))
        P = [list(map(int, input().split())) for _ in range(M)]
        out = solve(M, N, P)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

