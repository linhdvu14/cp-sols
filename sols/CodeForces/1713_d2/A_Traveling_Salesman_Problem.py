''' A. Traveling Salesman Problem
https://codeforces.com/contest/1713/problem/A
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
    def __contains__(self, k): return super().__contains__(k^self.rand)

INF = float('inf')

# -----------------------------------------

def solve(N, points):
    X = sorted([x for x, y in points if y == 0])
    Y = sorted([y for x, y in points if x == 0])
    
    res = 0
    if X:
        if X[0] < 0: res -= 2 * X[0]
        if X[-1] > 0: res += 2 * X[-1]
    if Y:
        if Y[0] < 0: res -= 2 * Y[0]
        if Y[-1] > 0: res += 2 * Y[-1]

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        points = [list(map(int, input().split())) for _ in range(N)]
        out = solve(N, points)
        print(out)


if __name__ == '__main__':
    main()

