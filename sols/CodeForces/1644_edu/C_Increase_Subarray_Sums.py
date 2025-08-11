''' C. Increase Subarray Sums
https://codeforces.com/contest/1644/problem/C
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

def solve(N, X, A):
    # max subarray sum with len == k
    MX = [0] + [-INF] * N
    for i in range(N):
        s = 0
        for j in range(i, N):
            s += A[j]
            MX[j-i+1] = max(MX[j-i+1], s)
    
    res = [0] * (N+1)
    for k in range(N+1):
        for i in range(N+1):
            res[k] = max(res[k], MX[i] + X * min(i, k))

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, X = list(map(int, input().split()))
        A = list(map(int, input().split()))
        out = solve(N, X, A)
        print(*out)


if __name__ == '__main__':
    main()

