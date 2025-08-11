''' Problem D1: Line of Delivery (Part 1)
https://www.facebook.com/codingcompetitions/hacker-cup/2024/practice-round/problems/D1
'''

import os, sys
input = sys.stdin.readline
output = sys.stdout.write

from inspect import currentframe, getframeinfo
from re import search
DEBUG = os.environ.get('debug') not in [None, '0']
DEBUG_CASE = int(os.environ.get('case', 0))

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

def solve(N, G, E):
    E.sort(reverse=True)
    res = None
    for i, e in enumerate(E):
        cand = (abs(e - G), i + 1)
        if not res or cand < res: res = cand
    return res[1], res[0]


def main():
    T = int(input())
    for t in range(T):
        N, G = list(map(int, input().split()))
        E = [int(input()) for _ in range(N)]
        if DEBUG and DEBUG_CASE and t != DEBUG_CASE: continue
        a, b = solve(N, G, E)
        print(f'Case #{t + 1}: {a} {b}')


if __name__ == '__main__':
    main()

