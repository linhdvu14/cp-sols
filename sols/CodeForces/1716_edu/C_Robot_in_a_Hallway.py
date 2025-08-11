''' C. Robot in a Hallway
https://codeforces.com/contest/1716/problem/C 
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

class IntKeyDict(dict):
    from random import randrange
    rand = randrange(1 << 62)
    def __setitem__(self, k, v): super().__setitem__(k^self.rand, v)
    def __getitem__(self, k): return super().__getitem__(k^self.rand)
    def __contains__(self, k): return super().__contains__(k^self.rand)
    def get(self, k, default=None): return super().get(k^self.rand, default)
    def keys(self): return [k^self.rand for k in super().keys()]
    def items(self): return [(k^self.rand, v) for k, v in super().items()]

INF = float('inf')

# -----------------------------------------

def solve(C, grid):
    # time after entering cell
    for r in range(2):
        for c in range(C):
            grid[r][c] += 1
    grid[0][0] = 0

    # dp[r][c] = total wait time if snake from (r, c) back to (r^1, c)
    dp = [[0] * C for _ in range(2)]
    for r in range(2): dp[r][C-1] = max(0, grid[r^1][C-1] - 1 - grid[r][C-1])

    for c in range(C-2, -1, -1):
        for r in range(2):
            dp[r][c] = max(0, dp[r][c+1] + (grid[r][c+1] - 1 - grid[r][c]))  # (r, c) -> (r, c+1) -> (r^1, c+1)
            t = grid[r][c] + dp[r][c] + (C-c-1) * 2   # time at (r^1, c+1)
            dp[r][c] += max(0, grid[r^1][c] - 1 - t)  # (r^1, c+1) -> (r^1, c)
    
    # path = snake + hook
    res = INF
    t = r = 0
    rem = 2*C - 1
    for c in range(C-1):
        res = min(res, t + max(0, dp[r][c] - max(0, t - grid[r][c])) + rem)
        r ^= 1
        t = max(t + 1, grid[r][c])
        t = max(t + 1, grid[r][c+1])
        rem -= 2

    t = max(t + 1, grid[r^1][C-1])
    res = min(res, t)

    return res


def main():
    T = int(input())
    for _ in range(T):
        C = int(input())
        grid = [list(map(int, input().split())) for _ in range(2)]
        out = solve(C, grid)
        print(out)



if __name__ == '__main__':
    main()
