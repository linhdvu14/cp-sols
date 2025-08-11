''' F. Robot on the Board 2
https://codeforces.com/contest/1607/problem/F
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

from collections import deque

def solve(R, C, NEXT):
    N = R*C

    # dist[x] = max moves if start from cell x
    dist = [-1]*N

    # probe from unvisited cell x
    # stop when fall off or revisit a cell
    # when stop, update dist for all cells visited in this pass
    def dfs(x):
        chain = deque([x])
        while True:
            x = NEXT[x]
            if x == -1 or dist[x] > -1: break
            dist[x] = 0
            chain.append(x)
        
        add = 0 if x == -1 else dist[x]   # > 0 if revisit a cell from previous passes
        cycle_len = 0                     # > 0 if revisit a cell from this pass
        M = len(chain)
        for i, px in enumerate(chain):
            if px == x:
                cycle_len = M - i
            if cycle_len == 0:
                dist[px] = M - i + add
            else:
                dist[px] = cycle_len

    for x in range(N):
        if dist[x] != -1: continue
        dfs(x)
    
    mx_x, mx_d = None, -1
    for x in range(N):
        if dist[x] > mx_d:
            mx_x, mx_d = x, dist[x]
    r, c = divmod(mx_x, C)
    return r, c, mx_d


def main():
    T = int(input())
    for _ in range(T):
        _ = input()
        R, C = list(map(int, input().split()))

        # next move
        NEXT = [-1]*(R*C)
        nr, nc = -1, -1
        for r in range(R):
            row = input().decode().strip()
            for c, arrow in enumerate(row):                
                if arrow == 'U': nr, nc = r-1, c
                if arrow == 'D': nr, nc = r+1, c
                if arrow == 'L': nr, nc = r, c-1
                if arrow == 'R': nr, nc = r, c+1
                if not (0 <= nr < R and 0 <= nc < C): continue
                NEXT[r*C + c] = nr*C + nc
        
        r, c, d = solve(R, C, NEXT)
        output(f'{r+1} {c+1} {d}\n')


if __name__ == '__main__':
    main()

