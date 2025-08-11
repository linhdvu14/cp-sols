''' F. Copy of a Copy of a Copy
https://codeforces.com/contest/1772/problem/F
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
    def __repr__(self): return str({k: v for k, v in self.items()})
    def get(self, k, default=None): return super().get(k^self.rand, default)
    def keys(self): return [k^self.rand for k in super().keys()]
    def items(self): return [(k^self.rand, v) for k, v in super().items()]

INF = float('inf')

# -----------------------------------------

def main():
    R, C, K = list(map(int, input().split()))
    grids = []
    for _ in range(K + 1):
        _ = input()
        grid = [input().decode().strip() for _ in range(R)]
        grids.append(grid)

    def count_moves(grid):
        res = 0
        for r in range(1, R - 1):
            for c in range(1, C - 1):
                for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if grid[nr][nc] == grid[r][c]: break 
                else: res += 1
        return res 
    
    def find_diff(grid1, grid2):
        res = []
        for r in range(R):
            for c in range(C):
                if grid1[r][c] != grid2[r][c]:
                    res.append((r, c))
        return res
    
    moves = [count_moves(grids[u]) for u in range(K + 1)]
    idx = sorted(list(range(K + 1)), key=lambda i: moves[i], reverse=True) 
    
    res = []
    for i in range(1, K + 1):
        if moves[idx[i]] != moves[idx[i - 1]]:
            diffs = find_diff(grids[idx[i - 1]], grids[idx[i]])
            for x, y in diffs: res.append((1, x + 1, y + 1))
       
        res.append((2, idx[i] + 1))

    print(idx[0] + 1)
    print(len(res))
    for t in res: print(*t)


if __name__ == '__main__':
    main()

