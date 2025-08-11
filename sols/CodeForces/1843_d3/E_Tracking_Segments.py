''' E. Tracking Segments
https://codeforces.com/contest/1843/problem/E
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def debug(*args):   
    if os.environ.get('debug') in [None, '0']: return
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
from itertools import accumulate

def solve(N, M, segs, Q, ops):
    def is_ok(n):
        A = [0] * N 
        for i in range(n): A[ops[i] - 1] = 1
        ps = [0] + list(accumulate(A))
        for l, r in segs:
            one = ps[r] - ps[l - 1]
            zero = r - l + 1 - one
            if one > zero: return True 
        return False 

    res, lo, hi = -1, 0, Q
    while lo <= hi:
        mi = (lo + hi) // 2 
        if is_ok(mi):
            res = mi 
            hi = mi - 1
        else:
            lo = mi + 1

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        segs = [list(map(int, input().split())) for _ in range(M)]
        Q = int(input())
        ops = [int(input()) for _ in range(Q)]
        res = solve(N, M, segs, Q, ops)
        print(res)


if __name__ == '__main__':
    main()

