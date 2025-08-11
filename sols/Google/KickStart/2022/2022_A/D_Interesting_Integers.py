''' Interesting Integers
https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e73ea
'''

import io, os, sys
from unicodedata import digit
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

def solve(A, B):
    # count how many nums <= N s.t. p % s == 0
    def solve_leq(N):
        N = str(N)
        L = len(N)

        # dp[idx][free][s][prod] = remaining ways
        # prod ~ 2000 states
        dp = [[[{} for _ in range(110)] for _ in range(2)] for _ in range(L)] 

        def dfs(idx=0, free=0, s=0, p=1):
            if idx == L: return 1 if (s and p % s == 0) else 0
            if p in dp[idx][free][s]: return dp[idx][free][s][p]
            res = 0
            x = int(N[idx])
            bound = 9 if free else x
            for d in range(bound+1):
                nfree = 1 if (free or d < x) else 0
                ns = s + d
                np = p * d if ns > 0 else 1
                res += dfs(idx+1, nfree, ns, np)
            dp[idx][free][s][p] = res
            return res
        
        return dfs()

    return solve_leq(B) - solve_leq(A-1)


def main():
    T = int(input())
    for i in range(T):
        A, B = list(map(int, input().split()))
        out = solve(A, B)
        print(f'Case #{i+1}: {out}')


if __name__ == '__main__':
    main()
