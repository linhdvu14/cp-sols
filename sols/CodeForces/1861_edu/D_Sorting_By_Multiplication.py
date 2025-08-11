''' D. Sorting By Multiplication
https://codeforces.com/contest/1861/problem/D
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def debug(*args):   
    if os.environ.get('debug') in [None, '0']: return
    from inspect import currentframe, getframeinfo
    from re import search
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
    # L[i] = how many A[j] >= A[j - 1] for j <= i
    L = [0] * (N + 1)
    for i in range(1, N):
        L[i] = L[i - 1]
        if A[i] >= A[i - 1]: L[i] += 1

    # R[i] = how many A[j] >= A[j + 1] for j >= i
    R = [0] * (N + 1)
    for i in range(N - 2, -1, -1):
        R[i] = R[i + 1]
        if A[i] >= A[i + 1]: R[i] += 1

    # make A[..i-1] negative, A[i..] positive
    res = R[0]
    for i in range(1, N):
        res = min(res, L[i - 1] + 1 + R[i])

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        res = solve(N, A)
        print(res)


if __name__ == '__main__':
    main()