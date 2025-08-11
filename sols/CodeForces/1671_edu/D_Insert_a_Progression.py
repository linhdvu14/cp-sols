''' D. Insert a Progression
https://codeforces.com/contest/1671/problem/D
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

# extra cost to place 1..X

def solve(N, X, A):
    # place x = mn..mx for free
    mn, mx = min(A), max(A)
    res = sum(abs(A[i] - A[i-1]) for i in range(1, N))
    
    # extra cost to place x = 1..mn-1 == extra cost to place 1
    # should place between mn and its neighbor, at beginning, or at end
    # * orig cost = A[i+1] - A[i]
    # * new cost = (A[i+1] - 1) + (A[i] - 1)
    # -> extra cost = 2 * A[i] - 2
    if mn > 1: res += min(A[0] - 1, A[-1] - 1, 2*(mn-1))

    # extra cost to place x = mx+1..X == extra cost to place X
    if mx < X: res += min(X - A[0], X - A[-1], 2*(X-mx))

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, X = list(map(int, input().split()))
        A = list(map(int, input().split()))
        out = solve(N, X, A)
        print(out)


if __name__ == '__main__':
    main()

