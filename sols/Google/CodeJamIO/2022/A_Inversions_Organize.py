''' Inversions Organize
https://codingcompetitions.withgoogle.com/codejamio/round/00000000009d9870/0000000000a33e95
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

def solve(N, grid):
    count = [[0]*2 for _ in range(2)]
    for r in range(2*N):
        for c in range(2*N):
            if grid[r][c] == 'O': continue
            count[r//N][c//N] += 1
    return abs(count[0][0] - count[1][1]) + abs(count[0][1] - count[1][0])


def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        grid = [input().decode().strip() for _ in range(2*N)]
        out = solve(N, grid)
        print(f'Case #{t+1}: {out}')


if __name__ == '__main__':
    main()

