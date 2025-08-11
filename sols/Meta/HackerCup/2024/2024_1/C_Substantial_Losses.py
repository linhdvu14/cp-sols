''' Problem C: Substantial Losses
https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-1/problems/C
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
MOD = 998244353

# f(x) = first time at distance x from G
def solve(W, G, L):
    step = (2 * (L + 1) - 1) % MOD 
    dist = (W - G) % MOD
    return dist * step % MOD


def main():
    T = int(input())
    for t in range(T):
        W, G, L = list(map(int, input().split()))
        if DEBUG and DEBUG_CASE and t != DEBUG_CASE: continue
        res = solve(W, G, L)
        print(f'Case #{t + 1}: {res}')


if __name__ == '__main__':
    main()

