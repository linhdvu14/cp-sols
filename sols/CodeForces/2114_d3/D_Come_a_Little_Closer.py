''' D. Come a Little Closer
https://codeforces.com/contest/2114/problem/D
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

from inspect import currentframe, getframeinfo
from re import search
DEBUG = os.environ.get('debug') not in [None, '0']

def debug(*args):   
    if not DEBUG: return
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')

INF = float('inf')

# -----------------------------------------

def get_bounds(P, exclude=None):
    mnr = mnc = INF
    mxr = mxc = -INF
    for i, (r, c) in enumerate(P):
        if i == exclude: continue
        mnr = min(mnr, r)
        mxr = max(mxr, r)
        mnc = min(mnc, c)
        mxc = max(mxc, c)
    return mnr, mnc, mxr, mxc
    

def solve(N, P):
    mnr, mnc, mxr, mxc = get_bounds(P)
    res = (mxc - mnc + 1) * (mxr - mnr + 1)

    top, bottom, left, right = [], [], [], []
    for i, (r, c) in enumerate(P):
        if r == mnr: top.append(i)
        if r == mxr: bottom.append(i)
        if c == mnc: left.append(i)
        if c == mxc: right.append(i)
    
    for ls in [top, bottom, left, right]:
        if len(ls) != 1: continue
        mnr, mnc, mxr, mxc = get_bounds(P, ls[0])
        cand = (mxc - mnc + 1) * (mxr - mnr + 1)
        if cand != N - 1: res = min(res, cand)
        else: res = min(res, (mxc - mnc + 2) * (mxr - mnr + 1), (mxc - mnc + 1) * (mxr - mnr + 2))

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        P = [list(map(int, input().split())) for _ in range(N)]
        res = solve(N, P)
        print(res)


if __name__ == '__main__':
    main()

