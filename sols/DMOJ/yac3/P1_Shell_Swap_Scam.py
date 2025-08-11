''' Yet Another Contest 3 P1 - Shell Swap Scam
https://dmoj.ca/problem/yac3p1
'''

import os, sys
input = sys.stdin.readline  # strip() if str

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

def main():
    N, M, A, B = list(map(int, input().split()))
    swaps = [[] for _ in range(M)]
    idx = -1
    for i in range(M):
        ts = list(map(int, input().split()))
        if len(ts) == 1: idx = i 
        swaps[i] = ts

    # final pos of A
    a = A
    for i in range(idx):
        if len(swaps[i]) == 1: 
            if a == N: swaps[i] = (a - 1, a - 2)
            elif a == N-1: swaps[i] = (a - 1, a + 1)
            else: swaps[i] = (a + 1, a + 2)
        else:
            u, v = swaps[i]
            if a == u: a = v
            elif a == v: a = u
    
    # final pos of B
    b = B
    for i in range(M-1, idx, -1):
        if len(swaps[i]) == 1: 
            if b == N: swaps[i] = (b - 1, b - 2)
            elif b == N-1: swaps[i] = (b - 1, b + 1)
            else: swaps[i] = (b + 1, b + 2)
        else:
            u, v = swaps[i]
            if b == u: b = v
            elif b == v: b = u

    if a == b: 
        i = j = 1
        while i == a or i == b: i += 1
        while j == a or j == b or j == i: j += 1
        swaps[idx] = (i, j)
    else: swaps[idx] = (a, b)

    for s in swaps: print(*s)


if __name__ == '__main__':
    main()
