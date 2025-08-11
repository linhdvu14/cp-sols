''' D. Counting Rhyme
https://codeforces.com/contest/1884/problem/D
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
    cnt = [0] * (N + 1)
    for a in A: cnt[a] += 1

    # dp[a] = num pairs with gcd a
    dp = [0] * (N + 1)
    for a in range(N, 0, -1):
        tot = 0
        for b in range(a, N + 1, a):
            tot += cnt[b]
            dp[a] -= dp[b]
        dp[a] += tot * (tot - 1) // 2
    
    res = N * (N - 1) // 2
    for a in range(N + 1):
        if not cnt[a] or not dp[a]: continue
        for b in range(a, N + 1, a):
            res -= dp[b]
            dp[b] = 0

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        res = solve(N, A)
        print(res)


if __name__ == '__main__':
    main()

