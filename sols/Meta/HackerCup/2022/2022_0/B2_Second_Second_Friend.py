''' Problem B2: Second Second Friend
https://www.facebook.com/codingcompetitions/hacker-cup/2022/qualification-round/problems/B2
'''

import io, os, sys
input = sys.stdin.readline #io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def debug(*args):   
    if os.environ.get('debug') in [None, '0']: return
    from inspect import currentframe, getframeinfo
    from re import search
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')

INF = float('inf')

# -----------------------------------------

def solve(R, C, grid):
    bad = []
    nei = [[-1] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            nei[r][c] = (r > 0) + (r < R-1) + (c > 0) + (c < C-1)
            if grid[r][c] == '#' or nei[r][c] < 2:
                nei[r][c] = 0
                bad.append((r, c))
    
    while bad:
        r, c = bad.pop()
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if not (0 <= nr < R and 0 <= nc < C): continue
            if nei[nr][nc] == 0: continue
            nei[nr][nc] -= 1
            if nei[nr][nc] < 2:
                nei[nr][nc] = 0
                bad.append((nr, nc))

    for r in range(R):
        for c in range(C):
            if grid[r][c] == '^' and nei[r][c] == 0: return 'Impossible', None
            if nei[r][c] >= 2: grid[r][c] = '^'

    return 'Possible', grid


def main():
    T = int(input())
    for t in range(T):
        R, C = list(map(int, input().split()))
        grid = [list(input().strip()) for _ in range(R)]
        r1, r2 = solve(R, C, grid)
        print(f'Case #{t+1}: {r1}')
        if r2:
            for r in r2: print(*r, sep='')


if __name__ == '__main__':
    main()

