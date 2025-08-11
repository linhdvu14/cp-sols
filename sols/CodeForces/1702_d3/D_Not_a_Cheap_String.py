''' D. Not a Cheap String
https://codeforces.com/contest/1702/problem/D
'''

import io, os, sys
from tkinter import N
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

# for int dict key
from random import randrange
RAND = randrange(1 << 62)
def conv(x): return x ^ RAND

INF = float('inf')

# -----------------------------------------

def solve(S, P):
    tot = 0
    for c in S: tot += ord(c) - ord('a') + 1

    kept = [1] * len(S)
    for i in range(25, -1, -1):
        for j, c in enumerate(S):
            if ord(c) - ord('a') == i and tot > P:
                tot -= i + 1
                kept[j] = 0

    return [c for i, c in enumerate(S) if kept[i]]


def main():
    T = int(input())
    for _ in range(T):
        S = input().decode().strip()
        P = int(input())
        out = solve(S, P)
        print(*out, sep='')


if __name__ == '__main__':
    main()

