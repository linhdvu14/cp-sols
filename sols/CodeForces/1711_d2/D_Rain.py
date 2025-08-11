''' D. Rain
https://codeforces.com/contest/1711/problem/D
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
    def get(self, k, default=None): return super().get(k^self.rand, default)
    def keys(self): return [k^self.rand for k in super().keys()]
    def items(self): return [(k^self.rand, v) for k, v in super().items()]

INF = float('inf')

# -----------------------------------------

# https://codeforces.com/blog/entry/105232?#comment-937477
# https://codeforces.com/contest/1710/submission/165570885

def solve(N, M, rains):
    # 2nd order difference array
    diff = {}
    for x, p in rains:
        diff[x - p + 1] = diff.get(x - p + 1, 0) + 1
        diff[x + p + 1] = diff.get(x + p + 1, 0) + 1
        diff[x + 1] = diff.get(x + 1, 0) - 2
    diff = sorted(diff.items())

    # reconstruct accumulation at possible rain centers
    # after removing rain (x, p), pos (y, a) is good iff a - (p - |x - y|) <= m, for all pos with original a > m
    # iff a - m - p <= x - y <= m + p - a
    # iff x - p <= y - a + m and x + p >= y + a - m
    # -> track min(y - a + m) and max(y + a - m) 
    mn, mx = INF, -INF
    accum = add = px = 0
    for x, d in diff:
        accum += add * (x - px)
        add += d
        px = x
        if accum > M:
            mn = min(mn, x - 1 - accum + M)
            mx = max(mx, x - 1 + accum - M)
    
    res = [0] * N
    for i, (x, p) in enumerate(rains):
        if x - p <= mn and x + p >= mx:
            res[i] = 1
    
    return res



def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        rains = [list(map(int, input().split())) for _ in range(N)]
        out = solve(N, M, rains)
        print(*out, sep='')


if __name__ == '__main__':
    main()

