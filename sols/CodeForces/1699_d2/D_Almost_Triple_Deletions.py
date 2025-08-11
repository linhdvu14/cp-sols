''' D. Almost Triple Deletions
https://codeforces.com/contest/1699/problem/D
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') not in [None, '0']

if DEBUG:
    from inspect import currentframe, getframeinfo
    from re import search

def debug(*args):
    if not DEBUG: return
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')


class IntKeyDict(dict):
    from random import randrange
    rand = randrange(1 << 62)
    def __setitem__(self, k, v): super().__setitem__(k^self.rand, v)
    def __getitem__(self, k): return super().__getitem__(k^self.rand)


INF = float('inf')

# -----------------------------------------

def solve_1(N, A):
    can_del = [[0]*N for _ in range(N)]
    for i in range(N):
        mx = 0
        cnt = [0] * (N+1)
        for j in range(i, N):
            cnt[A[j]] += 1
            mx = max(mx, cnt[A[j]])
            if (j - i + 1) % 2 == 0 and mx <= (j - i + 1) // 2: can_del[i][j] = 1

    # dp[i] = max remaining length from A[0..i] if keep A[i]
    dp = [-INF] * N
    res = 0
    for i in range(N):
        if i == 0 or can_del[0][i-1]: dp[i] = 1
        for j in range(i):
            if A[j] == A[i] and (j==i-1 or can_del[j+1][i-1]):
                dp[i] = max(dp[i], 1 + dp[j])
        if i == N-1 or can_del[i+1][N-1]: res = max(res, dp[i])

    return res



def solve_2(N, A):
    # A[i..j] is deletable if even length and majority count <= (j-i+1)//2
    # dp[i] = max remaining length from A[0..i] that contains A[i]
    # dp[i] = 1 + max_j dp[j], if can del j+1..i-1 and (A[i] == A[j] or i == N)
    # --> ans is dp[N]
    dp = [-1] * (N+1)
    dp[0] = dp[-1] = 0
    for i in range(N+1):
        if i > 0 and dp[i-1] == -1: continue
        cnt = [0] * (N+1)
        mx = 0
        for j in range(i, N+1):  # check if i..j-1 can be deleted
            if j > i:
                cnt[A[j-1]] += 1
                mx = max(mx, cnt[A[j-1]])
            if (j - i) % 2 or mx > (j - i) // 2: continue
            if i == 0 and j < N: dp[j] = max(dp[j], 1)
            elif j == N: dp[j] = max(dp[j], dp[i-1])
            elif A[i-1] == A[j]: dp[j] = max(dp[j], dp[i-1] + 1)

    return dp[-1]

solve = solve_2


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        print(out)


if __name__ == '__main__':
    main()

