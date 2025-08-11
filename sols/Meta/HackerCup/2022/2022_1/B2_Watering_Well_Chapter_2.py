''' Problem B2: Watering Well - Chapter 2
https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-1/problems/B2
'''

import os, sys
input = sys.stdin.readline
output = sys.stdout.write

def debug(*args):   
    if os.environ.get('debug') in [None, '0']: return
    from inspect import currentframe, getframeinfo
    from re import search
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')

INF = float('inf')

# -----------------------------------------

MOD = 10**9 + 7

def solve(N, Q, trees, wells):
    sa = sb = sab = 0
    for a, b in trees:
        sa = (sa + a) % MOD
        sb = (sb + b) % MOD
        sab = (sab + a*a + b*b) % MOD

    res = 0
    for x, y in wells:
        res = (res + N * (x*x + y*y) + sab - 2*x*sa - 2*y*sb) % MOD

    return res


def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        trees = [list(map(int, input().split())) for _ in range(N)]
        Q = int(input())
        wells = [list(map(int, input().split())) for _ in range(Q)]
        res = solve(N, Q, trees, wells)
        print(f'Case #{t+1}: {res}')


if __name__ == '__main__':
    main()

