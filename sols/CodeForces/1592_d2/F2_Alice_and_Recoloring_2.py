''' F2. Alice and Recoloring 2
https://codeforces.com/contest/1592/problem/F2
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode() if str
output = sys.stdout.write


def find_matching(adj, L, R):
    # is it possible to find a longer alternative path starting from l
    def dfs(l):
        if seen[l]: return False   # cycle found
        seen[l] = True
        for r in adj[l]:
            # can add (l, r) to matching if
            # * r not yet in matching, or 
            # * can find a longer alt path from match[r], and rm (match[r], r)
            if match[r] == -1 or dfs(match[r]):
                match[r] = l
                return True
        return False

    # match each node
    # match[r] = l node s.t. edge (l, r) included in current matching
    # seen[l] = whether node l was visited
    match = [-1]*R
    for l in range(L):
        seen = [False]*L
        dfs(l)
    
    # final edges in matching
    return [(l, r) for r, l in enumerate(match) if l != -1]


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

    # all (R-1, C-1) ops are rectangles with distinct x and y (else 4 correct for cost 4)
    # and only when 3 corners except (R-1, C-1) are 1 (else 4 correct for cost 5)
    # --> find all (r, c) pairs where (r, c), (r, C-1), (R-1, c) are all 1
    adj = [[] for r in range(R)]
    for r in range(R-1):
        for c in range(C-1):
            if grid[r][c] == grid[r][C-1] == grid[R-1][c] == 1:
                adj[r].append(c)
    
    # find max bipartite match for (R-1, C-1) ops
    # convert rest with (0, 0) ops
    matching = find_matching(adj, R, C)
    op2 = len(matching)
    op1 = sum(sum(row) for row in grid) - op2*3
    if grid[R-1][C-1] == 0 and op2 % 2 == 1: op1 += 1
    if grid[R-1][C-1] == 1 and op2 % 2 == 1: op1 -= 1
    return op1 + 2*op2

def main():
    R, C = map(int, input().split())
    grid = [list(input().decode().strip()) for _ in range(R)]
    out = solve(R, C, grid)
    output(str(out) + '\n')

if __name__ == '__main__':
    main()

