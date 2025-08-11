''' D. Touch Grass
https://tlx.toki.id/contests/troc-25/problems/D
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

# a*(K-b) + (K-a)*b = K(a+b) - 2ab = Ka + b(K-2a) -> max b for fixed a

def solve(R, C, K, A, B):
    row_mn1 = row_mx1 = cnt = sum(A[:K])
    for i in range(K, R):
        if A[i] == 1: cnt += 1
        if A[i-K] == 1: cnt -= 1
        row_mn1 = min(row_mn1, cnt)
        row_mx1 = max(row_mx1, cnt)
    
    col_mn1 = col_mx1 = cnt = sum(B[:K])
    for i in range(K, C):
        if B[i] == 1: cnt += 1
        if B[i-K] == 1: cnt -= 1
        col_mn1 = min(col_mn1, cnt)
        col_mx1 = max(col_mx1, cnt)

    res = max(
        row_mx1*(K-col_mn1) + (K-row_mx1)*col_mn1,
        row_mx1*(K-col_mx1) + (K-row_mx1)*col_mx1,
        row_mn1*(K-col_mn1) + (K-row_mn1)*col_mn1,
        row_mn1*(K-col_mx1) + (K-row_mn1)*col_mx1,
    )

    return res


def main():
    R, C, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    out = solve(R, C, K, A, B)
    print(out)


if __name__ == '__main__':
    main()

