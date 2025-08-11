''' D2. Too Many Impostors (hard version)
https://codeforces.com/contest/1617/problem/D2
'''

# to test: 
# pypy3 template.py
# or: python interactive_runner.py python local_testing_tool.py 0 -- python3 a.py

import functools
import os, sys
input = sys.stdin.readline  # io.BytesIO(os.read(0,os.fstat(0).st_size)).readline doesn't work
output = functools.partial(print, flush=True)

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

def query(i, j, k):
    output(f'? {i+1} {j+1} {k+1}')
    return int(input())


def solve():
    N = int(input())
    truth = [-1]*N

    # check groups of 3 consecutive (N/3 queries)
    # find 2 consecutive groups with opposite majority
    groups = []
    gi = -1  # gi and gi+3
    for i in range(0, N, 3):
        c = query(i, i+1, i+2)
        if gi == -1 and len(groups) > 0 and c != groups[-1]: gi = i-3
        groups.append(c)
    
    # find an opposite pair, each in gi and gi+3 (2 queries)
    i0 = i1 = -1
    prev = groups[gi//3]
    for j in range(1, 4):
        cur = query(gi+j, gi+j+1, gi+j+2) if j < 3 else groups[gi//3+1]
        if cur != prev:  # qi+j and qi+j+1 are opposite
            if prev == 0: i0, i1 = gi+j-1, gi+j+2
            if prev == 1: i1, i0 = gi+j-1, gi+j+2
            break

    # determine groups gi and gi+3 (<= 4 queries)
    if groups[i0//3] == 1:
        truth[i0-i0%3] = truth[i0-i0%3+1] = truth[i0-i0%3+2] = 1
        truth[i1-i1%3] = truth[i1-i1%3+1] = truth[i1-i1%3+2] = 0
    else:
        for j in range(3):
            for k in [i0-i0%3+j, i1-i1%3+j]:
                if k == i0 or k == i1: continue
                truth[k] = query(k, i0, i1)
    truth[i0] = 0
    truth[i1] = 1
    
    # determine remaining groups (2N/3 - 4 queries)
    for i, gv in enumerate(groups):
        if i*3 == gi or i*3 == gi+3: continue
        if gv == 0:
            c = query(i*3, i*3+1, i1)
            if c == 0:
                truth[i*3] = truth[i*3+1] = 0
                truth[i*3+2] = query(i*3+2, i0, i1)
            else:
                truth[i*3+2] = 0
                truth[i*3] = query(i*3, i0, i1)
                truth[i*3+1] = 1 - truth[i*3]
        else:
            c = query(i*3, i*3+1, i0)
            if c == 1:
                truth[i*3] = truth[i*3+1] = 1
                truth[i*3+2] = query(i*3+2, i0, i1)
            else:
                truth[i*3+2] = 1
                truth[i*3] = query(i*3, i0, i1)
                truth[i*3+1] = 1 - truth[i*3]            


    res = [i+1 for i, c in enumerate(truth) if c == 0]
    n, s = len(res), ' '.join(map(str, res))
    output(f'! {n} {s}')


def main():
    T = int(input())
    for _ in range(T):
        solve()
    
 
if __name__ == '__main__':
    main()