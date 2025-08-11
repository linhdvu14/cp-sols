''' DMOPC '21 Contest 8 P2 - Kanna Market
https://dmoj.ca/problem/dmopc21c8p2
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

MOD = 10**9 + 7

def solve(N, M, grid):
    def solve_parity(p):
        s = mx = cnt = 0
        mn = M + 1
        for i in range(p, N, 2):
            a, b = grid[0][i], grid[1][i]
            if a == b == 0: cnt += 1
            elif a == 0 or b == 0:
                mx = max(mx, a + b)
                mn = min(mn, a + b)
            else:
                if s != 0 and s != a + b: return 0
                s = a + b

        if s != 0: 
            if mx > 0 and not (1 <= s - mx <= M and 1 <= s - mn <= M): return 0
            l1, r1 = 1, min(M, s)
            l2, r2 = s - min(M, s), s - 1
            l, r = max(l1, l2), min(r1, r2)
            if l > r: return 0
            return pow(r - l + 1, cnt, MOD)
        
        res = 0
        for s in range(mx+1, 2*M+1):
            if mx > 0 and not (1 <= s - mx <= M and 1 <= s - mn <= M): continue
            l1, r1 = 1, min(M, s)
            l2, r2 = s - min(M, s), s - 1
            l, r = max(l1, l2), min(r1, r2)
            if l <= r: res = (res + pow(r - l + 1, cnt, MOD)) % MOD

        return res
    
    even = solve_parity(0)
    odd = solve_parity(1)
    return (even * odd) % MOD


def main():
    N, M = list(map(int, input().split()))
    grid = [list(map(int, input().split())) for _ in range(2)]
    out = solve(N, M, grid)
    print(out)


if __name__ == '__main__':
    main()

