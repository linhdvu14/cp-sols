''' D1. Hot Start Up (easy version)
https://codeforces.com/contest/1799/problem/D1
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

# dp[i][k] = min cost if ends are (k, A[i]) after move i
# append A[i] to either
# - A[i-1] --> dp[i][k] = min(dp[i][k], dp[i-1][k] + (hot[A[i]] if A[i] == A[i-1] else cold[A[i]]))
# - k --> dp[i][A[i-1]] = min(dp[i][A[i-1]], dp[i-1][k] + (hot[A[i]] if A[i] == k else cold[A[i]]))

def solve(N, K, A, cold, hot):
    dp = [INF] * (K + 1) 
    for i, a in enumerate(A):
        if not i: 
            dp[0] = cold[a]
        else:
            pa = A[i - 1]
            ndp = [INF] * (K + 1)
            for k in range(K + 1):
                ndp[k] = min(ndp[k], dp[k] + (hot[a] if a == pa else cold[a]))
                ndp[pa] = min(ndp[pa], dp[k] + (hot[a] if a == k else cold[a]))
            dp = ndp

    return min(dp)


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        cold = [0] + list(map(int, input().split()))
        hot = [0] + list(map(int, input().split()))
        res = solve(N, K, A, cold, hot)
        print(res)


if __name__ == '__main__':
    main()

