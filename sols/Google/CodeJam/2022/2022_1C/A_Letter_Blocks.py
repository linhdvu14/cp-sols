''' Letter Blocks
https://codingcompetitions.withgoogle.com/codejam/round/0000000000877b42/0000000000afe6a1
'''

import io, os, sys
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

from string import ascii_uppercase
from itertools import groupby

def solve(N, S):
    for c in ascii_uppercase:
        left, right, mid, single, rem = [], [], [], [], []
        for s in S:
            if c not in s: rem.append(s)
            elif all(cs == c for cs in s): single.append(s)
            elif s[0] == c: left.append(s)
            elif s[-1] == c: right.append(s)
            else: mid.append(s)
        
        if len(left) > 1 or len(right) > 1 or len(mid) > 1: return 'IMPOSSIBLE'
        if mid and (left or right or single): return 'IMPOSSIBLE'

        cur = ''
        if mid: cur += mid.pop()
        else:
            if right: cur += right.pop()
            for s in single: cur += s
            if left: cur += left.pop()

        if cur: rem.append(cur)
        S = rem

    res = ''.join(S)
    blocks = [k for k, _ in groupby(res)]
    if len(blocks) != len(set(blocks)): return 'IMPOSSIBLE'
    return res


def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        S = input().decode().strip().split()
        out = solve(N, S)
        print(f'Case #{t+1}: {out}')


if __name__ == '__main__':
    main()

