''' E. Grid Xor
https://codeforces.com/contest/1629/problem/E
'''

import io, os, sys
input = sys.stdin.readline 
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

# https://codeforces.com/blog/entry/99276?#comment-880317
# each cell should have odd number of chosen neighbors
# fix row 1 to all 0
# then choose (r, c) if (r-1, c) has even number of 1 neighbors

# but why is last row valid?
# https://codeforces.com/blog/entry/99276?#comment-880444

# can also fix orig value
# then white cells only depend on white cells
# black cells only depend on black cells

def solve(N, grid):
    res = 0
    chosen = [[0]*N for _ in range(N)]
    for r in range(1, N):
        for c in range(N):
            cnt = 0
            if r > 1: cnt += chosen[r-2][c]
            if c > 0: cnt += chosen[r-1][c-1]
            if c < N-1: cnt += chosen[r-1][c+1]
            if cnt % 2 == 0:
                chosen[r][c] = 1
                res ^= grid[r][c]
    
    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        grid = [list(map(int, input().split())) for _ in range(N)]
        out = solve(N, grid)
        print(out)


if __name__ == '__main__':
    main()

