''' G1. Subsequence Addition (Easy Version)
https://codeforces.com/contest/1807/problem/G1
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

MAX = 5000

def solve(N, A):
    A.sort()
    if A[0] != 1: return 'NO'

    dp = [0] * (MAX + 1)
    dp[1] = 1
    for i in range(1, N):
        a = A[i]
        if not dp[a]: return 'NO'
        dp2 = dp[:]
        for m in range(MAX + 1):
            if dp[m] and m + a <= MAX:
                dp2[m + a] = 1
        dp = dp2

    return 'YES'


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        res = solve(N, A)
        print(res)


if __name__ == '__main__':
    main()

