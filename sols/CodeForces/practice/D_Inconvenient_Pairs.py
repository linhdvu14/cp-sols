''' D. Inconvenient Pairs
https://codeforces.com/contest/1569/problem/D
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

from bisect import bisect_left

# should be both strictly on row streets or col streets
# if both row e.g. (x1, y1), (x2, y2) where x1, x2 are streets
# then x1 != x2, and no col street y s.t. y1 <= y <= y2

def solve(N, M, K, X, Y, pts):
    grp_x, grp_y = [], []
    for x, y in pts:
        i = bisect_left(X, x)
        j = bisect_left(Y, y)
        if X[i] == x and Y[j] == y: continue
        if X[i] == x: grp_x.append((x, j))
        else: grp_y.append((y, i))

    grp_x.sort()
    sy, dy = [0] * M, [0] * M
    prev, cnt = -1, {}
    for x, i in grp_x:
        if prev != -1 and x != prev: cnt.clear()
        sy[i] += 1
        dy[i] += cnt.get(i, 0)
        cnt[i] = cnt.get(i, 0) + 1
        prev = x

    grp_y.sort()
    sx, dx = [0] * N, [0] * N
    prev, cnt = -1, {}
    for y, i in grp_y:
        if prev != -1 and y != prev: cnt.clear()
        sx[i] += 1
        dx[i] += cnt.get(i, 0)
        cnt[i] = cnt.get(i, 0) + 1
        prev = y
    
    res = 0
    for i in range(N): res += sx[i] * (sx[i] - 1) // 2 - dx[i]
    for i in range(M): res += sy[i] * (sy[i] - 1) // 2 - dy[i]
    
    return res


def main():
    T = int(input())
    for _ in range(T):
        N, M, K = list(map(int, input().split()))
        X = list(map(int, input().split()))
        Y = list(map(int, input().split()))
        pts = [list(map(int, input().split())) for _ in range(K)]
        out = solve(N, M, K, X, Y, pts)
        print(out)


if __name__ == '__main__':
    main()

