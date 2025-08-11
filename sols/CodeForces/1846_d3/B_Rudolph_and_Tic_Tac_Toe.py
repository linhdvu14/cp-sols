''' B. Rudolph and Tic-Tac-Toe
https://codeforces.com/contest/1846/problem/B
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

def solve(grid):
    def ok(A): return len(A) == 1 and A[0] != '.'

    for i in range(3):
        s = list(set(grid[i][j] for j in range(3)))
        if ok(s): return s[0]
        s = list(set(grid[j][i] for j in range(3)))
        if ok(s): return s[0]

    s = list(set(grid[i][i] for i in range(3)))
    if ok(s): return s[0]

    s = list(set(grid[i][2 - i] for i in range(3)))
    if ok(s): return s[0]

    return 'DRAW'


def main():
    T = int(input())
    for _ in range(T):
        grid = [input().decode().strip() for _ in range(3)]
        res = solve(grid)
        print(res)


if __name__ == '__main__':
    main()

