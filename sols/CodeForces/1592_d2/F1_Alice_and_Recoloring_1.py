''' F1. Alice and Recoloring 1
https://codeforces.com/contest/1592/problem/F1
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode() if str
output = sys.stdout.write


def solve(R, C, grid):
    # convert B->1, W->0
    # want grid to be all 0
    grid = [[1 if v=='B' else 0 for v in row] for row in grid]

    # convert grid[r][c] = (grid[r][c] + grid[r+1][c] + grid[r][c+1] + grid[r+1][c+1]) % 2
    # want grid to be all 0
    ngrid = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            s = grid[r][c]
            if r+1 < R: s += grid[r+1][c]
            if c+1 < C: s += grid[r][c+1]
            if r+1 < R and c+1 < C: s += grid[r+1][c+1]
            ngrid[r][c] = s % 2
    grid = ngrid

    # each (0, 0) op change 1 cell
    # each (R-1, C-1) op change 3 cells: (r, c), (r, C-1), (R-1, c), (R-1, C-1)
    # should call (R-1, C-1) op at most once, and only when 4 corners are all 1
    res = sum(sum(row) for row in grid)
    if grid[R-1][C-1] == 1:
        for r in range(R-1):
            for c in range(C-1):
                if grid[r][c] == grid[r][C-1] == grid[R-1][c] == 1:
                    return res - 1
    return res



def main():
    R, C = map(int, input().split())
    grid = [list(input().decode().strip()) for _ in range(R)]
    out = solve(R, C, grid)
    output(str(out) + '\n')

if __name__ == '__main__':
    main()