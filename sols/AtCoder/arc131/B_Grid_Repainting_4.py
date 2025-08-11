''' B - Grid Repainting 4
https://atcoder.jp/contests/arc131/tasks/arc131_b
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc


def main():
    R, C = list(map(int, input().split()))
    grid = [list(input().decode().strip()) for _ in range(R)]

    
    def is_ok(r, c):
        for rr, cc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if not (0 <= rr < R and 0 <= cc < C): continue
            if grid[rr][cc] == grid[r][c]: return False
        return True

    @bootstrap
    def dfs(r, c):
        for d in '12345':
            grid[r][c] = d
            if not is_ok(r, c): continue
            ok = True
            for rr, cc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if not (0 <= rr < R and 0 <= cc < C): continue
                if grid[rr][cc] != '.': continue
                child_ok = yield dfs(rr, cc)
                if not child_ok:
                    ok = False
                    break
            if ok: yield True
        yield False
    
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '.': 
                dfs(r, c)
    
    for row in grid: print(''.join(row))



if __name__ == '__main__':
    main()

