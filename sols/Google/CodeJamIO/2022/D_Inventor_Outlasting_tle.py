''' Inventor Outlasting
https://codingcompetitions.withgoogle.com/codejamio/round/00000000009d9870/0000000000a33fb0
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
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

from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack: return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack: break
                to = stack[-1].send(to)
        return to
    return wrappedfunc


# 0 = white, 1 = green, 2 = grey
def solve(R, C, grid):
    @bootstrap
    def dfs(r, c):
        assert grid[r][c] == 0
        grid[r][c] = 2
        restore = [(r, c, 0)]
        
        for dr, dc in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            nr, nc = r + dr, c + dc
            while True:
                if not (0 <= nr < R and 0 <= nc < C): break
                if grid[nr][nc] == 2: break
                restore.append((nr, nc, grid[nr][nc]))
                grid[nr][nc] = 2
                nr += dr
                nc += dc
        
        win = True
        for r in range(R):
            for c in range(C):
                if grid[r][c] != 0: continue
                v = yield dfs(r, c)
                if v:
                    win = False
                    break
        
        for r, c, v in restore: grid[r][c] = v  
        yield win
    
    res = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 0 and dfs(r, c):
                res += 1

    return res


def main():
    T = int(input())
    for t in range(T):
        R, C = list(map(int, input().split()))
        grid = []
        for _ in range(R):
            row = input().decode().strip()
            row = [0 if v == 'X' else 1 for v in row]
            grid.append(row)
        out = solve(R, C, grid)
        print(f'Case #{t+1}: {out}')


if __name__ == '__main__':
    main()

