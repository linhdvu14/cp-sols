''' E. Matrix and Shifts
https://codeforces.com/contest/1660/problem/E
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

# equiv to 1 horizontal shift and 1 vertical shift
# try all possible diagonals

def solve(N, A):
    all_ones = sum(sum(row) for row in A)
    res = N * N

    for c in range(N):
        diag_ones = r = 0
        for _ in range(N):
            diag_ones += A[r][c]
            r = (r + 1) % N
            c = (c + 1) % N
        res = min(res, N + all_ones - 2 * diag_ones)

    return res


def main():
    T = int(input())
    for _ in range(T):
        _ = input()
        N = int(input())
        A = []
        for _ in range(N): A.append(list(map(int, list(input().decode().strip()))))
        out = solve(N, A)
        print(out)


if __name__ == '__main__':
    main()

