''' Cheerio Contest 3 P4 - Bit Flips
https://dmoj.ca/problem/cheerio3p4
'''

import os, sys
input = sys.stdin.readline  # strip() if str

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

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # cnt[b][i] = num vals in A[0:i] with bit b - 1 set
    cnt = [[0] * (N + 1) for _ in range(31)]
    for b in range(30):
        n = 0
        for i, a in enumerate(A):
            n += (a >> b) & 1
            cnt[b + 1][i + 1] = n

    # dp[b][i][j] = min cost to sort A[i:j] considering only last b bits
    dp = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(31)]

    for b in range(1, 31):
        for i in range(N):
            for j in range(i + 1, N + 1):
                mn = INF 
                for k in range(i, j + 1):  # make bit b zero in [i:k] and one in [k:j]
                    l = cnt[b][k] - cnt[b][i] + dp[b - 1][i][k]
                    r = j - k - (cnt[b][j] - cnt[b][k]) + dp[b - 1][k][j]
                    mn = min(mn, l + r)
                dp[b][i][j] = mn 

    print(dp[-1][0][N])


if __name__ == '__main__':
    main()
