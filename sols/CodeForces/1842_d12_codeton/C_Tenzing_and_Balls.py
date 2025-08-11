''' C. Tenzing and Balls
https://codeforces.com/contest/1842/problem/C
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
    # dp[i] = max removals on 0..i
    # mx[v] = max dp[i - 1] - i over all i s.t. A[i] = v seen so far
    dp = [0] * (N + 1)
    mx = [-INF] * (N + 1)

    for i, a in enumerate(A):
        dp[i] = max(dp[i - 1], i + mx[a] + 1)
        mx[a] = max(mx[a], dp[i - 1] - i)

    return dp[N - 1]


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        res = solve(N, A)
        print(res)


if __name__ == '__main__':
    main()

