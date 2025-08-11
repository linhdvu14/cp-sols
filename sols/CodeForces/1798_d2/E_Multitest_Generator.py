''' E. Multitest Generator
https://codeforces.com/contest/1798/problem/E
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

def solve(N, A):
    # - max tests that A[i:] can split into with 0 op; -1 if cannot split evenly
    # - max tests that A[i:] can split into with 1 op
    dp = [[0, 0] for _ in range(N + 1)]

    res = [2] * N
    mx0 = 0
    for i in range(N - 1, -1, -1):
        c0, c1 = dp[i + 1]
        if A[i] == c0: res[i] = 0
        elif c0 != -1: res[i] = 1
        elif c1 >= A[i]: res[i] = 1
        
        j = i + A[i] + 1
        c0 = 1 + dp[j][0] if j <= N and dp[j][0] != -1 else -1
        c1 = 1 + max(mx0, dp[j][1]) if j <= N else 1 + mx0
        dp[i] = [c0, c1]
        mx0 = max(mx0, c0)

    return res[:-1]


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        res = solve(N, A)
        print(*res)


if __name__ == '__main__':
    main()

