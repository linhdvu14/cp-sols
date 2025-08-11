''' F. LEGOndary Grandmaster
https://codeforces.com/contest/1615/problem/F
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

MOD = 10**9 + 7

# https://codeforces.com/blog/entry/98253?#comment-872017
# num 0s on even positions + num 1s on odd positions doesn't change after an operation
# create S' s.t. S'[i] == 1 iff (i % 2 == 0 and S[i] == 0) or (i % 2 == 1 and S[i] == 1)
# then an op on S is equivalent to swapping 2 adjacent different indices on S'
# need to turn S' into T' with minimum num swaps

# S' can be turned into T' iff have same number of 1s
# let f(s) = number of 1s in s
# then cost to turn S' into T' is SUM_{i=1..n} |f(S'[:i]) - f(T'[:i])|

# let L(i, j) = num ways to label S'[:i] and T'[:i] s.t. f(S'[:i]) - f(T'[:i]) == j
#     R(i, j) = num ways to label S'[i:] and T'[i:] s.t. f(S'[i:]) - f(T'[i:]) == j
# then ans is SUM_{i=1..n} SUM_{j=-n..n} |j * L(i, j) * R(i, -j)|

# transitions
changes = {
    ('0', '0'): [0],
    ('0', '1'): [-1],
    ('0', '?'): [0, -1],
    ('1', '0'): [1],
    ('1', '1'): [0],
    ('1', '?'): [0, 1],
    ('?', '0'): [0, 1],
    ('?', '1'): [-1, 0],
    ('?', '?'): [0, 0, 1, -1],
}

def solve(N, S, T):
    # flip even indices
    for i in range(0, N, 2):
        if S[i] != '?': S[i] = '1' if S[i] == '0' else '0'
        if T[i] != '?': T[i] = '1' if T[i] == '0' else '0'

    L = [[0] * (2*N + 1) for _ in range(N+1)]
    L[0][0] = 1
    for i in range(N):
        ds = changes[S[i], T[i]]
        for j in range(-N, N+1):
            for d in ds:
                if -N <= j + d <= N:
                    L[i+1][j+d] = (L[i+1][j+d] + L[i][j]) % MOD
 
    R = [[0] * (2*N + 1) for _ in range(N+1)]
    R[N][0] = 1
    for i in range(N-1, -1, -1):
        ds = changes[S[i], T[i]]
        for j in range(-N, N+1):
            for d in ds:
                if -N <= j + d <= N:
                    R[i][j+d] = (R[i][j+d] + R[i+1][j]) % MOD

    res = 0
    for i in range(1, N+1):
        for j in range(-N, N+1):
            res = (res + abs(j * L[i][j] * R[i][-j])) % MOD

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = list(input().decode().strip())
        T = list(input().decode().strip())
        out = solve(N, S, T)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

