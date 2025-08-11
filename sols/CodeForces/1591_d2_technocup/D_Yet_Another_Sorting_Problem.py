''' D. Yet Another Sorting Problem
https://codeforces.com/contest/1591/problem/D
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


def merge(a, b):
    c, cnt = [], 0

    na, nb, ia, ib = len(a), len(b), 0, 0
    while ia < na and ib < nb:
        if a[ia] > b[ib]:
            c.append(b[ib])
            cnt += na - ia
            ib += 1
        else:
            c.append(a[ia])
            ia += 1
    if ia < na: c.extend(a[ia:])
    if ib < nb: c.extend(b[ib:])
    
    return c, cnt


def mergesort(A):
    '''return sorted array A, num inversions'''
    if len(A) < 2: return A, 0

    mid = (len(A)+1) // 2
    a, ca = mergesort(A[:mid])
    b, cb = mergesort(A[mid:])
    c, cc = merge(a, b)
    return c, ca+cb+cc
    

def solve(N, A):
    # can always sort if has dup
    # to put b in correct pos c, rotate (a, a, c) then (a, a, b)
    if len(set(A)) < N: return 'YES'

    # each rotation reduces num inversions by 2
    _, inv = mergesort(A)
    return 'YES' if inv % 2 == 0 else 'NO'


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

