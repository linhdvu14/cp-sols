''' C. Differential Sorting
https://codeforces.com/contest/1635/problem/C
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

# A[-2] and A[-1] cannot be changed
# if A[-2] <= A[-1] < 0 and A not alr valid, the rightmost invalid num can only be changed to pos num (> A[-2])
# so cannot be made valid

def solve(N, A):
    if all(a <= b for a, b in zip(A, A[1:])): return 0, []
    y, z = A[-2], A[-1]
    if y > z or z < 0: return -1, []
    return N-2, [(i+1, N-1, N) for i in range(N-2)]


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        r1, r2 = solve(N, A)
        print(r1)
        for r in r2: print(*r)


if __name__ == '__main__':
    main()

