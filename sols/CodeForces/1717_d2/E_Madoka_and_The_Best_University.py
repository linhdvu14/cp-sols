''' E. Madoka and The Best University
https://codeforces.com/contest/1717/problem/E
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

MOD = 10**9 + 7

from math import gcd
def lcm(a, b): return a * b // gcd(a, b)

# iterate over c and g = gcd(a, b)
# for each c and g, count num pairs of (a, b) s.t. a + b = N - c and gcd(a, b) = g
# i.e. num pairs of (a', b') s.t. a' + b' == (N - c) // g and gcd(a', b') == 1
# i.e. phi((N - c) // g)

def solve(N):
    phi = list(range(N + 1))
    phi[1] = 0
    for i in range(2, N + 1):
        if phi[i] == i:  # prime
            for j in range(i, N + 1, i):
                phi[j] -= phi[j] // i
    
    res = 0
    for g in range(1, N):
        for s in range(g, N, g):
            c = N - s 
            res = (res + lcm(c, g) * phi[(N - c) // g]) % MOD
            
    return res


def main():
    N = int(input())
    res = solve(N)
    print(res)


if __name__ == '__main__':
    main()

