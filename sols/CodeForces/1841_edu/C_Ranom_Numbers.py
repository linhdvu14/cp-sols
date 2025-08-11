''' C. Ranom Numbers
https://codeforces.com/contest/1841/problem/C
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

VAL = [1, 10, 100, 1000, 10000]

def solve(S):
    N = len(S)
    S = [ord(c) - ord('A') for c in S]

    suff_sum = [0] * (N + 1)
    suff_max = [0] * (N + 2)
    for i in range(N - 1, -1, -1):
        c = S[i]
        suff_sum[i] = suff_sum[i + 1] + (VAL[c] if c >= suff_max[i + 1] else -VAL[c])
        suff_max[i] = max(suff_max[i + 1], c)
    
    # dp[c] = SUM VAL[i] s.t. c = S[i] >= max(S[i..])
    dp = [0] * 5
    ps = 0
    res = -INF
    for i, c in enumerate(S):
        for c1 in range(5):
            cand = ps + (VAL[c1] if c1 >= suff_max[i + 1] else -VAL[c1]) + suff_sum[i + 1]
            for c2 in range(5): cand += dp[c2] if c2 >= max(c1, suff_max[i + 1]) else -dp[c2]
            res = max(res, cand)
        for c1 in range(S[i]):
            ps -= dp[c1]
            dp[c1] = 0
        dp[c] += VAL[c]

    return res


def main():
    T = int(input())
    for _ in range(T):
        S = input().decode().strip()
        res = solve(S)
        print(res)


if __name__ == '__main__':
    main()
