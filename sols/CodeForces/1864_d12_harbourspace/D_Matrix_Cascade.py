''' D. Matrix Cascade
https://codeforces.com/contest/1864/problem/D 
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

# x - i >= y - j -> x - y >= i - j
# x - i >= j - y -> x + y >= i + j
def solve(N, grid):
    # dp[d][s] = total flips over all (r, c) s.t. r - c <= d and r + c <= s
    dp1 = [0] * (2 * N)
    dp2 = [0] * (2 * N)

    res = 0
    for d in range(1 - N, N):
        for s in range(2 * N - 1):
            dp2[s] = dp2[s - 1] + dp1[s] - dp1[s - 1]
            r, c = (s + d) // 2, (s - d) // 2
            if (s + d) & 1 or not (0 <= c < N and 0 <= r < N): continue
            if (dp2[s] + int(grid[r][c])) & 1:
                dp2[s] += 1
                res += 1
        dp1, dp2 = dp2, [0] * (2 * N)

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        grid = [input().decode().strip() for _ in range(N)]
        res = solve(N, grid)
        print(res)


if __name__ == '__main__':
    main()

