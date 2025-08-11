''' B. Vittorio Plays with LEGO Bricks
https://codeforces.com/contest/1776/problem/B
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
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

# join V trees at root, pulling left and right trees towards center
def main():
    N, H = list(map(int, input().split()))
    A = list(map(int, input().split()))

    # dp[l][r] = min bricks to cover l..r
    dp = [[INF] * N for _ in range(N)]
    for i in range(N): dp[i][i] = H
    for d in range(1, N):
        for l in range(N - d):
            r = l + d
            save = max(H + 1 - (A[r] - A[l] + 1) // 2, 0)
            dp[l][r] = min(dp[l][m] + dp[m + 1][r] for m in range(l, r)) - save

    print(dp[0][-1])


if __name__ == '__main__':
    main()

