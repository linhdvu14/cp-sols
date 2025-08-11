''' E. Expand the Path
https://codeforces.com/contest/1644/problem/E
'''

import io, os, sys
from plistlib import FMT_XML
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') not in [None, '0']

if DEBUG:
    from inspect import currentframe, getframeinfo
    from re import search

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

# https://codeforces.com/contest/1644/submission/147307844

def solve(N, S):
    if len(set(S)) == 1: return N
    
    # find final pos
    fr = fc = 1
    for c in S:
        if c == 'D': fr += 1
        else: fc += 1
    
    # all cells on path S reachable
    # all cells inside rectangle (fr, fc) - (N, N) reachable
    res = len(S) + (N - fr + 1) * (N - fc + 1)

    # on vertical segments (cells followed by D), extend right until fc reaches N
    # on horizontal segments (cells followed by R), extend down until fr reaches N
    turn = False
    for i, c in enumerate(S):
        if i > 0 and c != S[i-1]: turn = True
        if not turn: continue
        if c == 'D': res += N - fc
        else: res += N - fr

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input().decode().strip()
        out = solve(N, S)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

