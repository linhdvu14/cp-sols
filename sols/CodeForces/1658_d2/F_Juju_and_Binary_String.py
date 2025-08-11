''' F. Juju and Binary String
https://codeforces.com/contest/1658/problem/F
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


INF = float('inf')

# -----------------------------------------

# https://codeforces.com/blog/entry/101302?#comment-899678
# want to pick min num intervals with total length = M and total ones = tar
# consider all wrap-around subarrays of length M
# let c[i] = num 1s in A[i..i+M-1]
# each consecutive c[i]'s differ by at most 1, so there's a subarray with c[i] = x for all min(c[i]) <= x <= max(c[i])
# can show min(c[i]) <= tar <= max(c[i]) by contradiction
# if tar > min(c[i]), then N * tar > SUM_i c[i] -> N * (ones * M) // N > ones * M
# intuition: tar = avg number of 1s in M-subarray -> min <= avg <= max

def solve(N, M, A):
    ones = sum(A)
    if (ones * M) % N != 0: return -1, []
    tar = ones * M // N

    cur = sum(A[:M])
    if cur == tar: return 1, [(1, M)]
    segments = None
    for i in range(1, N):
        cur += A[(i + M - 1) % N] - A[i - 1]
        if cur == tar:
            if i + M - 1 < N: return 1, [(i + 1, i + M)]
            segments = [(1, M - N + i), (i+1, N)]

    if not segments: return -1, []
    return 2, segments


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        A = list(map(int, list(input().decode().strip())))
        r1, r2 = solve(N, M, A)
        print(r1)
        for tup in r2: print(*tup)


if __name__ == '__main__':
    main()

