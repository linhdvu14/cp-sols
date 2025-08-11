''' C. Ticks 
https://codeforces.com/contest/1579/problem/C
'''

def solve(grid, R, C, K):
    status = [row[:] for row in grid]
    rem = sum(v for row in grid for v in row)

    for r in range(1, R):
        for c in range(1, C):
            if status[r][c] == 0: continue
            mxk = 0
            for k in range(1, R):
                if r-k < 0 or c-k < 0 or c+k >= C: break
                if grid[r-k][c-k] == 0 or grid[r-k][c+k] == 0: break
                if k >= K: mxk = k
            if mxk > 0:  # can put base here
                status[r][c] = 0
                rem -= 1
                for k in range(1, mxk+1):
                    rem -= status[r-k][c-k] + status[r-k][c+k]
                    status[r-k][c-k] = 0
                    status[r-k][c+k] = 0
    return rem == 0
 
def main():
    from sys import stdin
    
    T = int(stdin.readline().strip())
    for _ in range(T):
        R, C, K = map(int, stdin.readline().strip().split())
        grid = []
        for _ in range(R):
            row = stdin.readline().strip()
            row = [1 if v=='*' else 0 for v in row]  # 1 = painted
            grid.append(row)
        out = solve(grid, R, C, K)
        print('YES' if out else 'NO')

if __name__ == '__main__':
    main()
