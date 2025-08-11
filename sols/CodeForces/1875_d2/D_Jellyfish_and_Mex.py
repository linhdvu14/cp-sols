''' D. Jellyfish and Mex
https://codeforces.com/contest/1875/problem/D
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
    cnt = [0] * MAX
    for a in A:
        if a < MAX: 
            cnt[a] += 1
    
    M = MAX
    for i, c in enumerate(cnt):
        if not c:
            M = i
            break
    
    # dp[m] = ans if mex is m
    dp = [0] + [INF] * M
    for i in range(1, M + 1):
        for j in range(i):
            dp[i] = min(dp[i], dp[j] + (cnt[j] - 1) * i + j)

    return dp[M]


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        res = solve(N, A)
        print(res)


if __name__ == '__main__':
    main()

