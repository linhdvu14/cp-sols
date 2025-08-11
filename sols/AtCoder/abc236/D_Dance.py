''' D - Dance
https://atcoder.jp/contests/abc236/tasks/abc236_d
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write


def main():
    N = int(input()) * 2
    grid = [[0]*N for _ in range(N)]
    for r in range(N-1):
        row = list(map(int, input().split()))
        for c, x in enumerate(row):
            grid[r][r+c+1] = x
    
    res = 0
    used = [False]*N
    def dfs(i, xor=0):
        nonlocal res
        if i >= N:
            res = max(res, xor)
        elif used[i]:
            dfs(i+1, xor)
        else:
            for j in range(i+1, N):
                if used[j]: continue
                used[j] = True
                dfs(i+1, xor ^ grid[i][j])
                used[j] = False

    dfs(0)
    print(res)



if __name__ == '__main__':
    main()

