''' C. Card Game
https://codeforces.com/contest/1739/problem/C 
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

def precalc_nCk(N, p):
    fact = [1] * (N+1)  # n! % p
    inv_fact = [1] * (N+1)  # (1 / n!) % p
    for i in range(1, N+1):
        fact[i] = (i * fact[i-1]) % p
        inv_fact[i] = pow(fact[i], p-2, p)
    return fact, inv_fact

MOD = 998244353
MAX = 120
FACT, INV_FACT = precalc_nCk(MAX, MOD)

def nCk(n, k): 
    if k > n: return 0
    return (FACT[n] * INV_FACT[k] * INV_FACT[n-k]) % MOD


def solve(N):
    a, b = 1, 0
    n = 2
    while n * 2 <= N:
        # win if have max
        a2 = nCk(n * 2 - 1, n - 1)

        # lose if don't have max or max-1
        b2 = nCk(n * 2 - 2, n)

        # if have max and max-1, depend on prev
        a2 = (a2 + b) % MOD
        b2 = (b2 + a) % MOD

        a, b = a2, b2
        n += 1

    return a, b, 1
        


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        res = solve(N)
        print(*res)


if __name__ == '__main__':
    main()

