''' E. Crazy Robot
https://codeforces.com/contest/1613/problem/E
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

INF = float('inf')

from collections import deque

def solve(R, C, grid):
    queue = deque([])  # winning cells

    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'L':
                queue.append((r, c))
                break
    
    # win if have deterministic path to L
    # bfs from winning cells
    while queue:
        r, c = queue.popleft()
        for r1, c1 in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if not (0 <= r1 < R and 0 <= c1 < C): continue
            if grid[r1][c1] != '.': continue   # alr added to queue
            unk = 0
            for r2, c2 in [(r1+1, c1), (r1-1, c1), (r1, c1+1), (r1, c1-1)]:
                if not (0 <= r2 < R and 0 <= c2 < C): continue
                if grid[r2][c2] == '.': unk += 1
            if unk <= 1:  # (r1, c1) deterministic
                grid[r1][c1] = '+'
                queue.append((r1, c1))
        
    # output
    for row in grid: print(''.join(row))



def main():
    T = int(input())
    for _ in range(T):
        R, C = list(map(int, input().split()))
        grid = [list(input().decode().strip()) for _ in range(R)]
        solve(R, C, grid)


if __name__ == '__main__':
    main()

