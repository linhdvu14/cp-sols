''' Touchbar Typing
https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caea6/0000000000b76f44
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

from heapq import heappush

def solve(N, S, M, K):
    # dp[i][j] = min cost to type S[..i] with S[i] at K[j] 
    # dp[i][j] = min_k dp[i-1][k] + abs(j-k)
    dp = [[INF] * M for _ in range(N)]
    for i, d in enumerate(K):
        if d == S[0]: dp[0][i] = 0
    
    for i in range(1, N):
        # k < j -> dp[i][j] = min_k (dp[i-1][k] - k) + j
        pool = []
        for j in range(M):
            heappush(pool, dp[i-1][j] - j)
            if K[j] == S[i] and pool: dp[i][j] = min(dp[i][j], pool[0] + j)
        
        # k > j -> dp[i][j] = min_k (dp[i-1][k] + k) - j
        pool = []
        for j in range(M-1, -1, -1):
            heappush(pool, dp[i-1][j] + j)
            if K[j] == S[i] and pool: dp[i][j] = min(dp[i][j], pool[0] - j)

    return min(dp[N-1])


def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        S = list(map(int, input().split()))
        M = int(input())
        K = list(map(int, input().split()))
        out = solve(N, S, M, K)
        print(f'Case #{t+1}: {out}')


if __name__ == '__main__':
    main()

