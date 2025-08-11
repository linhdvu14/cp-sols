''' D. Two-Colored Dominoes
https://codeforces.com/contest/1863/problem/D
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
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

# num vertical pieces spanning rows (r, r + 1) must be even
# similar for horizontal

def solve(R, C, grid):
    rows = [[] for _ in range(R)]
    cols = [[] for _ in range(C)]
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'U': rows[r].append(c)
            if grid[r][c] == 'L': cols[c].append(r)
    
    for r, cs in enumerate(rows):
        if len(cs) & 1: return [[-1]]
        for i, c in enumerate(cs):
            if i & 1: grid[r][c], grid[r + 1][c] = 'B', 'W'
            else: grid[r][c], grid[r + 1][c] = 'W', 'B'
    
    for c, rs in enumerate(cols):
        if len(rs) & 1: return [[-1]]
        for i, r in enumerate(rs):
            if i & 1: grid[r][c], grid[r][c + 1] = 'B', 'W'
            else: grid[r][c], grid[r][c + 1] = 'W', 'B'
    
    return grid


def main():
    T = int(input())
    for _ in range(T):
        R, C = list(map(int, input().split()))
        grid = [list(input().decode().strip()) for _ in range(R)]
        res = solve(R, C, grid)
        for r in res: print(*r, sep='')


if __name__ == '__main__':
    main()

