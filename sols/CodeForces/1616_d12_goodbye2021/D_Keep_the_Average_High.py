''' D. Keep the Average High
https://codeforces.com/contest/1616/problem/D
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

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


INF = float('inf')

# -----------------------------------------

def solve_tle(N, A, X):
    # sum(A[i]..A[j]) = pref[j+1] - pref[i]
    pref = [0]
    for a in A: pref.append(pref[-1] + a)

    # good[i][j] = do all subsegments of A[i]..A[j] have average >= X
    good = [[False]*N for _ in range(N)]
    for d in range(1, N):  # check i..i+d
        for i in range(N-d):
            good[i][i+d] = pref[i+d+1] - pref[i] >= X*(d+1)
            if d > 1 and (not good[i][i+d-1] or not good[i+1][i+d]):
                good[i][i+d] = False

    # dp[i][b] = min drops in A[0]..A[i] if A[i] is dropped (0) or kept (1)
    dp = [[INF]*2 for _ in range(N)]
    dp[0][0] = 1
    dp[0][1] = 0

    for i in range(1, N):
        dp[i][0] = min(dp[i-1][0], dp[i-1][1]) + 1

        # keep i-d..i, drop i-d-1
        for d in range(1, i+1):
            if not good[i-d][i]: break
            if d == i:
                dp[i][1] = 0
            else:
                dp[i][1] = min(dp[i][1], dp[i-d-1][0])

    return N - min(dp[-1])


# subtract all elements by x, then a segment is good if all subsegments have sum >= 0
# if S is good, then S'=S+[x] is good iff sum(S'[-2:]) >= 0 and sum(S'[-3:]) >= 0
# say S' has bad suffix of length N >= 2, i.e. sum(S'[-N:]) < 0
# * if N == 2 or N == 3: obvious
# * if N >= 4: let S' = [...a, b, c, d], then sum([...a, b]) >= 0, so c+d < 0
# in general, if min subsegment size is M, then S' is good iff sum(S'[-i:]) >= 0 for i=M..2M-1

# good segment is extended by checking a fixed number of suffixes -> optimal to greedily extend as far as possible

def solve(N, A, X):
    A = [a-X for a in A]
    res = start = 0
    for i in range(N):
        good = True
        if i - start >= 1 and A[i] + A[i-1] < 0: good = False
        if i - start >= 2 and A[i] + A[i-1] + A[i-2] < 0: good = False
        if not good:  # exclude i
            res += 1
            start = i + 1
    return N - res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        X = int(input())
        out = solve(N, A, X)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

