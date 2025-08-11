''' D. Trees and Segments
https://codeforces.com/contest/1858/problem/D
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

def solve(N, K, S):
    def f(S, char):
        # dp[i][k] = max consecutive char on S[0..i] with at most k change on S[0..i]
        dp = [[0] * (K + 1) for _ in range(N + 1)]
        pos = [-1]
        for i, a in enumerate(S):
            if a != char: pos.append(i)
            for k in range(K + 1):
                j = pos[max(len(pos) - k - 1, 0)] + 1
                dp[i][k] = max(dp[i - 1][k], dp[i][k - 1], i - j + 1)
        return dp[:-1]

    pad = [0] * (K + 1)
    L0, L1 = f(S, '0') + [pad], f(S, '1') + [pad]
    R0, R1 = f(S[::-1], '0')[::-1] + [pad], f(S[::-1], '1')[::-1] + [pad]
    
    # dp[x] = max consecutive 1 if x consecutive 0
    dp = [-INF] * (N + 1)
    for i in range(-1, N):
        for k in range(K + 1):
            for c0, c1 in [[L0[i][k], R1[i + 1][K - k]], [R0[i + 1][K - k], L1[i][k]]]:
                dp[c0] = max(dp[c0], c1)

    res = [-INF] * N
    for i in range(N):
        for c0 in range(N + 1):
            res[i] = max(res[i], c0 * (i + 1) + dp[c0])

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        S = input().decode().strip()
        res = solve(N, K, S)
        print(*res)


if __name__ == '__main__':
    main()

