''' E2. Divisible Numbers (hard version)
https://codeforces.com/contest/1744/problem/E2
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

def factorize(n):
    small, large = [], []
    for i in range(1, int(n**0.5) + 1, 2 if n & 1 else 1):
        if n % i == 0:
            small.append(i)
            large.append(n // i)
    if small[-1] == large[-1]: large.pop()
    return small + large[::-1]


def solve(a, b, c, d):
    facs_a = factorize(a)
    facs_b = factorize(b)
    tar = a * b 

    for fa in facs_a:
        for fb in facs_b:
            fx = fa * fb 
            x = (a // fx + 1) * fx 
            fy = tar // fx 
            y = (b // fy + 1) * fy 
            if x <= c and y <= d: return x, y
    
    return -1, -1


def main():
    T = int(input())
    for _ in range(T):
        a, b, c, d = list(map(int, input().split()))
        x, y = solve(a, b, c, d)
        print(x, y)


if __name__ == '__main__':
    main()

