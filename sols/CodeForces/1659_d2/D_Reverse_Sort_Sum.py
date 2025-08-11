''' D. Reverse Sort Sum
https://codeforces.com/contest/1659/problem/D
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

# if A[i] = 1 -> B_k[i] = 0 once k reaches the i-th 0 in A --> C[i] = idx of the i-th 0
# if A[i] = 0 and A[0]..A[i-1] all 0 -> C[i] = 0
# if A[i] = 0 and A[0]..A[i-1] has a 1 -> B_k[i] = 0 for first i k's and once k reaches the i-th 0 in A -> C[i] = idx of the i-th 0 - i

def solve(N, C):
    A = [1] * (N + 1)
    for i, c in enumerate(C):
        if A[i] == 1: 
            if c == 0: A[i] = 0
            else: A[c] = 0
        else: 
            A[c + i] = 0
    return A[:N]


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        C = list(map(int, input().split()))
        out = solve(N, C)
        print(*out)


if __name__ == '__main__':
    main()

