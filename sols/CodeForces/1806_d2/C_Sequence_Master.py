''' C. Sequence Master
https://codeforces.com/contest/1806/problem/C
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

# a1 * a2 * ... * an + (a1 + a2 + ... + an) = SUM_ai, for all subsets [a1, a2, ... an]
# Case 1: all ai = x -> x^n = 2nx
#   Case 1.1: n = 1 -> x = *
#   Case 1.2: n = 2 -> x = 0, x = 2
#   Case 1.3: n > 2 -> x = 0
# Case 2: exists some x != y among ai's
#   -> prod of any (n - 1) other ai's is -1
#   -> n even, all other ai's equal -1
#   -> (-1) * (2n - 2) + x + y = (-1)^n - n 
#                              = x * (-1)^(n - 1) - (n - 1) + x
#                              = y * (-1)^(n - 1) - (n - 1) + y
#                              = xy * (-1)^(n - 2) - (n - 2) + x + y
#   -> x + y = n - 1; xy = -n
#   -> x = -1, y = n

def solve(N, A):
    res = sum(abs(a) for a in A)
    if N == 1: res = min(res, abs(A[0] - A[1]))
    if N == 2: res = min(res, sum(abs(a - 2) for a in A))
    if N % 2 == 0:
        mx = max(A)
        res = min(res, sum(abs(a + 1) for a in A) - abs(mx + 1) + abs(mx - N))

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

