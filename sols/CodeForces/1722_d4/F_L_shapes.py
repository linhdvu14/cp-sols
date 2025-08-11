''' F. L-shapes
https://codeforces.com/contest/1722/problem/F
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

def solve(R, C, grid):
    seen = [[0] * C for _ in range(R)]

    def bfs(r, c):
        st = [(r, c)]
        seen[r][c] = 1
        cnt = 0
        mnr = mnc = INF
        mxr = mxc = -INF
        while st:
            r, c = st.pop()
            cnt += 1
            mnr = min(mnr, r); mxr = max(mxr, r)
            mnc = min(mnc, c); mxc = max(mxc, c)
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    nr, nc = r + dr, c + dc 
                    if not (0 <= nr < R and 0 <= nc < C): continue
                    if seen[nr][nc] or grid[nr][nc] == '.': continue
                    seen[nr][nc] = 1
                    st.append((nr, nc))
        return cnt == 3 and mxr - mnr == 1 and mxc - mnc == 1

    for r in range(R):
        for c in range(C):
            if grid[r][c] == '.' or seen[r][c]: continue
            if not bfs(r, c): return False

    return True


def main():
    T = int(input())
    for _ in range(T):
        R, C = list(map(int, input().split()))
        grid = [input().decode().strip() for _ in range(R)]
        res = solve(R, C, grid)
        print('YES' if res else 'NO')


if __name__ == '__main__':
    main()

