''' E. Wish I Knew How to Sort
https://codeforces.com/contest/1754/problem/E
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

MOD = 998244353

def solve(N, A):
    # f(n) = expected num steps if there are n out-of-place 0's and n out-of-place 1's
    # p(n) = n^2 / (N*(N-1)//2) = prob of picking a good (0, 1) pair
    # f(n) = p(n) * (1 + f(n-1)) + (1 - p(n)) * (1 + f(n))
    # f(n) = 1/p(n) + f(n-1) = 1/p(n) + 1/p(n-1) + ... + 1/p(1)
    zero = N - sum(A)
    bad = sum(A[:zero])
    denom = pow(N * (N - 1) // 2, MOD - 2, MOD)
    res = 0
    for n in range(1, bad + 1):
        p = (n * n * denom) % MOD 
        res = (res + pow(p, MOD - 2, MOD)) % MOD

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        res = solve(N, A)
        print(res)


if __name__ == '__main__':
    main()

