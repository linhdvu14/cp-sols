''' E. Interview
https://codeforces.com/contest/1807/problem/E
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

def ask(idx):
    output('?', len(idx), *[i + 1 for i in idx])
    res = int(input())
    return res


def solve(N, A):
    ps = [0] * (N + 1)
    for i, a in enumerate(A): ps[i] = ps[i - 1] + a 

    res, lo, hi = -1, 1, N
    while lo <= hi:
        mi = (lo + hi) // 2
        got = ask(list(range(mi)))
        exp = ps[mi - 1]
        if got > exp:
            res = mi 
            hi = mi - 1
        else:
            lo = mi + 1 
    
    output(f'! {res}')


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        solve(N, A)

 

if __name__ == '__main__':
    main()

