''' D. Traps
https://codeforces.com/contest/1684/problem/D
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

# optimal to always rm K eles, e.g. A[i1], A[i2], ... A[ik]
# rm A[i1] reduces cost by: A[i1] - (N - i1 - 1) + (K-1) = A[i1] - (N - i1 - K)
# rm A[i2] reduces cost by: A[i2] - (N - i2 - 1) + (K-2) = A[i2] - (N - i2 - (K - 1))
# rm A[ik] reduces cost by: A[ik] - (N - ik - 1) + (K-K) = A[ik] - (N - ik - 1)

def solve(N, K, A):
    if K >= N: return 0
    gains = [a + i for i, a in enumerate(A)]
    gains.sort(reverse=True)
    res = sum(A) + N*K - K*(K+1) // 2 - sum(gains[:K])
    return res


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        out = solve(N, K, A)
        print(out)


if __name__ == '__main__':
    main()

