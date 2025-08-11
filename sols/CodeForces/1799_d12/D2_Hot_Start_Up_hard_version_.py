''' D2. Hot Start Up (hard version)
https://codeforces.com/contest/1799/problem/D2
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
    print(f'{prefix}{", ".join(var_and_vals)}', file=sys.stderr, flush=True)

INF = float('inf')

# -----------------------------------------

def solve(N, K, A, cold, hot):
    dp = [INF] * (K + 1) 
    add = mn = 0

    # mn = min(dp) w/o add
    for i, a in enumerate(A):
        if not i: 
            dp[0] = mn = cold[a]
        else:
            pa = A[i - 1]
            t = min(mn + cold[a], dp[a] + hot[a]) + add
            add += hot[a] if a == pa else cold[a]
            dp[pa] = min(dp[pa] + add, t) - add
            mn = min(mn, dp[pa])

            # t = min(mn + cold[a], dp[a] + hot[a])
            # add = hot[a] if a == pa else cold[a]
            # for k in range(K + 1): dp[k] += add
            # dp[pa] = min(dp[pa], t)
            # mn = min(mn + add, dp[pa])

    return mn + add


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

