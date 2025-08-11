''' F. Flipping Range
https://codeforces.com/contest/1631/problem/F
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

def gcd(a, b):
    '''assume a, b >= 0'''
    if a < b: a, b = b, a
    while b > 0: a, b = b, a % b
    return a


# all flip intervals are multiples of g = gcd(B)
# need to find max sum A after flipping some intervals of size g
# let s[i] = 1 if A[i] is flipped in optimal construction, 0 otherwise; i=0..N-1
# let f[i] = s[i] ^ s[i+g] ^ s[i+2g] ^ ... ^ s[i+mg]; i=0..g-1; i+mg <= N-1
# then f[i] must be either all 0 or all 1

# let dp[i][0] = max (s[i] * A[i] + S[i+g] * A[i+g] + S[i+2g] * A[i+2g] ...) s.t. f[i] == 0
#     dp[i][1] = same sum s.t. f[i] == 1
# then ans is max (SUM_{i=0..g-1} dp[i][0], SUM_{i=0..g-1} dp[i][1])

def solve(N, M, A, B):
    g = B[0]
    for b in B: g = gcd(g, b)

    s0 = s1 = 0
    for i in range(g):
        v0, v1 = A[i], -A[i]
        for j in range(i+g, N, g):
            nv0 = max(v0 + A[j], v1 - A[j])
            nv1 = max(v0 - A[j], v1 + A[j])
            v0, v1 = nv0, nv1
        s0 += v0
        s1 += v1

    return max(s0, s1)


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        out = solve(N, M, A, B)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

