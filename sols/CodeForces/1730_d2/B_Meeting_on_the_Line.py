''' B. Meeting on the Line
https://codeforces.com/contest/1730/problem/B
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

# f(x0) = max_(x, t) abs(x - x0) + t --> downturned triangle
def solve_1(N, X, A):
    E = 1e-7

    def f(x0):
        res = -INF 
        for a, x in zip(A, X):
            res = max(res, a + abs(x - x0))
        return res

    l, r = min(X), max(X)
    while r - l > E:
        m1 = l + (r - l) / 3
        m2 = r - (r - l) / 3
        f1 = f(m1)
        f2 = f(m2)
        if f1 > f2: l = m1
        else: r = m2
    
    return l


# https://codeforces.com/blog/entry/107261?#comment-956111
def solve_2(N, X, A):
    mn, mx = INF, -INF
    for x, t in zip(X, A):
        mn = min(mn, x - t)
        mx = max(mx, x + t)

    return (mn + mx) / 2   


solve = solve_2

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        X = list(map(int, input().split()))
        A = list(map(int, input().split()))
        res = solve(N, X, A)
        print(res)


if __name__ == '__main__':
    main()

