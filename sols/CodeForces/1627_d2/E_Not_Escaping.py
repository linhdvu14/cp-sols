''' E. Not Escaping
https://codeforces.com/contest/1627/problem/E
'''

import io, os, sys
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

from collections import deque

def solve(R, C, K, X, ladders):
    ladders = deque(sorted([(a-1, b-1, c-1, d-1, h) for a, b, c, d, h in ladders]))
 
    # dp[r] = [](c, cost to reach (r, c)) where (r, c) is ladder start or end
    dp = [[] for _ in range(R)]
    dp[0].append([0, 0])

    # process all ladders originating from row r
    for r in range(R-1):
        out = []
        while ladders and ladders[0][0] == r:
            _, c1, r2, c2, h = ladders.popleft()
            out.append([c1, INF, r2, c2, h])
        if not dp[r]: continue
        dp[r] += out
        dp[r].sort()

        # min cost to reach each c from left and right
        mn, pc = INF, -1
        for tup in dp[r]:
            mn += (tup[0] - pc) * X[r]
            pc = tup[0]
            mn = min(mn, tup[1])
            tup[1] = mn
        
        mn, pc = INF, -1
        for tup in dp[r][::-1]:
            mn += (pc - tup[0]) * X[r]
            pc = tup[0]
            mn = min(mn, tup[1])
            tup[1] = mn

        # update cost for all ladder ends originating from this row
        for tup in dp[r]:
            if len(tup) < 5: continue
            _, cost, r2, c2, h = tup
            dp[r2].append([c2, cost - h])
    
    if not dp[R-1]: return 'NO ESCAPE'
    res = min((C-1-c) * X[R-1] + cost for c, cost in dp[R-1])
    return res


def main():
    T = int(input())
    for _ in range(T):
        R, C, K = list(map(int, input().split()))
        X = list(map(int, input().split()))
        ladders = [list(map(int, input().split())) for _ in range(K)]
        out = solve(R, C, K, X, ladders)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

