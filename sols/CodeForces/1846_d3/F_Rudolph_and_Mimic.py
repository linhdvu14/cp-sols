''' F. Rudolph and Mimic
https://codeforces.com/contest/1846/problem/F
'''

import functools
import os, sys
input = sys.stdin.readline  # strip() if str; io.BytesIO(os.read(0,os.fstat(0).st_size)).readline doesn't work
output = functools.partial(print, flush=True)

DEBUG = os.environ.get('debug') not in [None, '0']

def debug(*args):   
    if not DEBUG: return
    from inspect import currentframe, getframeinfo
    from re import search
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')

INF = float('inf')

# -----------------------------------------

from collections import Counter

def remove(idx):
    idx = [i + 1 for i in idx]
    output(f'- {len(idx)}', *idx)
    A = list(map(int, input().split()))
    return A


def guess(i):
    output(f'! {i + 1}')


def solve(N, A):
    def diff(A, B):
        ca = Counter(A)
        cb = Counter(B)
        diff = list((cb - ca).elements())
        assert len(diff) < 2
        return diff[0] if diff else None
    
    # mimic is currently val
    while True:
        B = remove([])
        val = diff(A, B)
        A = B
        if val: break 
    
    # remove everything but val
    idx = [i for i, a in enumerate(A) if a != val]
    A = remove(idx)

    while True:
        for i, a in enumerate(A):
            if a != val:
                guess(i)
                return
        A = remove([])


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        solve(N, A)


if __name__ == '__main__':
    main()

