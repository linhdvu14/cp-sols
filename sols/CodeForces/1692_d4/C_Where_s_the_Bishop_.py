''' C. Where's the Bishop?
https://codeforces.com/contest/1692/problem/C
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


def main():
    T = int(input())
    for _ in range(T):
        _ = input()
        grid = [input().decode().strip() for _ in range(8)]
        for r in range(1, 7):
            for c in range(1, 7):
                if grid[r][c] == grid[r-1][c-1] == grid[r-1][c+1] == grid[r+1][c-1] == grid[r+1][c+1] == '#':
                    print(r+1, c+1)
                    break



if __name__ == '__main__':
    main()

