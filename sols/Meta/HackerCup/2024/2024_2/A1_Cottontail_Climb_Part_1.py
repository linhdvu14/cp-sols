''' Problem A1: Cottontail Climb (Part 1)
https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-2/problems/A1
'''

import os, sys
input = sys.stdin.readline
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

TEN = [10**i for i in range(20)]

def solve(A, B, M):
    res = 0
    for mid in range(1, 10):
        n = mid
        if A <= n <= B and n % M == 0: res += 1
        for i, d in enumerate(range(mid - 1, 0, -1)):
            n = n * 10 + d + d * TEN[(i + 1) * 2]
            if n > B: break
            if A <= n <= B and n % M == 0: res += 1

    return res


def main():
    T = int(input())
    for t in range(T):
        A, B, M = list(map(int, input().split()))
        res = solve(A, B, M)
        print(f'Case #{t + 1}: {res}')


if __name__ == '__main__':
    main()

