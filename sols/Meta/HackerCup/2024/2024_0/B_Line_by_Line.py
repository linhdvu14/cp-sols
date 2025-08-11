''' Problem B: Line by Line
https://www.facebook.com/codingcompetitions/hacker-cup/2024/practice-round/problems/B
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

# p^(n-1) = q^n -> q = p^[(n-1)/n]
def solve(N, P):
    q = pow(P / 100, (N - 1) / N)
    return q * 100 - P


def main():
    T = int(input())
    for t in range(T):
        N, P = list(map(int, input().split()))
        if DEBUG and DEBUG_CASE and t != DEBUG_CASE: continue
        res = solve(N, P)
        print(f'Case #{t + 1}: {res}')


if __name__ == '__main__':
    main()

