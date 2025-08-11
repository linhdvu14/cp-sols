''' B. Avoid Local Maximums
https://codeforces.com/contest/1635/problem/B
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

def solve(N, A):
    cnt = 0
    for i in range(1, N-1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            cnt += 1
            A[i+1] = max(A[i], A[i+2]) if i+2 < N else 10**9
    return cnt, A


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        r1, r2 = solve(N, A)
        print(r1)
        print(*r2)


if __name__ == '__main__':
    main()

