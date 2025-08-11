''' D1. The Endspeaker (Easy Version)
https://codeforces.com/contest/2027/problem/D1
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

from inspect import currentframe, getframeinfo
from re import search
DEBUG = os.environ.get('debug') not in [None, '0']

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
from bisect import bisect_right

def solve(N, M, A, B):
    if max(A) > B[0]: return -1

    ps = [0] * (N + 1)
    for i, a in enumerate(A): ps[i + 1] = ps[i] + a

    dp = [INF] * N + [0]
    for k in range(M - 1, -1, -1):
        for i in range(N - 1, -1, -1):
            j = bisect_right(ps, ps[i] + B[k]) - 1
            if j > i: dp[i] = min(dp[i], M - k - 1 + dp[j])
    
    return dp[0]



def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        res = solve(N, M, A, B)
        print(res)


if __name__ == '__main__':
    main()

