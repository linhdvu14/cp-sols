''' E. Moving Chips
https://codeforces.com/contest/1680/problem/E
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

# say best path ends at column i
# then cost has 2 components: best_path(0 -> i) and best_path(i -> N-1)
# same cost as best_path(0 -> N-1)
# note a column with 2 stars should be merged to 1 star

def solve(N, A, B):
    # trim
    l = min(i for i, (a, b) in enumerate(zip(A, B)) if a == '*' or b == '*')
    r = max(i for i, (a, b) in enumerate(zip(A, B)) if a == '*' or b == '*')
    A, B = A[l:r+1], B[l:r+1]

    # ca = min cost to merge all stars in columns 0..i-1 to cell (0, i)
    # cb = min cost to merge all stars in columns 0..i-1 to cell (1, i)
    ca = 1 if B[0] == '*' else 0
    cb = 1 if A[0] == '*' else 0
    for a, b in zip(A[1:], B[1:]):
        # (0, i-1) -> (0, i); (1, i) -> (0, i) if needed
        # (1, i-1) -> (1, i) -> (0, i)
        ca2 = min(ca + 1 + (b == '*'), cb + 2)
        cb2 = min(cb + 1 + (a == '*'), ca + 2)
        ca, cb = ca2, cb2
    
    return min(ca, cb)


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(input().decode().strip())
        B = list(input().decode().strip())
        out = solve(N, A, B)
        print(out)


if __name__ == '__main__':
    main()

