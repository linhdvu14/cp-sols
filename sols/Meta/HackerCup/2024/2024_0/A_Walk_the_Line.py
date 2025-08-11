''' Problem A: Walk the Line
https://www.facebook.com/codingcompetitions/hacker-cup/2024/practice-round/problems/A
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

def solve(N, K, S):
    mn = min(S)
    if N <= 2: return 'YES' if mn <= K else 'NO'
    return 'YES' if mn * 2 * (N - 2) + mn <= K else 'NO'


def main():
    T = int(input())
    for t in range(T):
        N, K = list(map(int, input().split()))
        S = [int(input()) for _ in range(N)]
        if DEBUG and DEBUG_CASE and t != DEBUG_CASE: continue
        res = solve(N, K, S)
        print(f'Case #{t + 1}: {res}')


if __name__ == '__main__':
    main()

