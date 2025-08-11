''' DMOPC '21 Contest 7 P1 - Chika Grids
https://dmoj.ca/problem/dmopc21c7p1
'''

import sys
input = sys.stdin.readline

INF = float('inf')


def solve(R, C, grid):
    for r in range(R):
        a = 0 if r == 0 else grid[r-1][0]
        for c in range(C):
            if grid[r][c] == 0:
                grid[r][c] = a + 1 if r == 0 else max(a, grid[r-1][c]) + 1
            elif grid[r][c] <= a or (r > 0 and grid[r][c] <= grid[r-1][c]): 
                return [[-1]]
            a = grid[r][c]

    return grid


def main():
    R, C = list(map(int, input().split()))
    grid = [list(map(int, input().split())) for _ in range(R)]
    out = solve(R, C, grid)
    for row in out: print(*row)


if __name__ == '__main__':
    main()

