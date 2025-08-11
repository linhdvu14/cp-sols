''' F. Our Wrenally
https://tlx.toki.id/contests/troc-29/problems/F
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

def count_prime_factors(n):
    res = 0
    d = 2
    while n >= d:
        while n % d == 0:
            res += 1
            n //= d 
        d += 1
    return res


# each division creates identical pieces: (a, b) -> (a/m, b), (a/m, b), ...
# (a, b) is winning if (a/m, b) is losing, regardless of m
# (a, b) -> (a/m1, b) -> (a/m1, b/n1) -> (a/m1/m2, b/n1) -> (a/m1/m2, b/n1/n2) -> ... -> (1, x) or (x, 1)
# each side wants longest path to 1

def main():
    a, b = list(map(int, input().split()))
    ca, cb = count_prime_factors(a), count_prime_factors(b)
    print('Mimi' if ca > cb else 'Shasha')

if __name__ == '__main__':
    main()
