''' D. Count GCD
https://codeforces.com/contest/1750/problem/D
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

def solve(N, M, A):
    for i in range(1, N):
        if A[i - 1] % A[i]:
            return 0

    res = 1
    for i in range(1, N):
        # count x in [1, M] s.t. gcd(x, A[i - 1]) = A[i]
        # count x in [1, M // A[i]] s.t. gcd(x, A[i - 1] // A[i]) = 1
        bound, n = M // A[i], A[i - 1] // A[i]

        primes = []
        p = 2
        while p * p <= n:
            if n % p == 0:
                primes.append(p)
                while n % p == 0: n //= p
            p += 1
        if n > 1: primes.append(n)  # len(primes) <= 9

        # inclusion exclusion
        mult = bound
        for mask in range(1, 1 << len(primes)):
            div = 1
            for i, p in enumerate(primes):
                if (mask >> i) & 1: 
                    div *= p
            if bin(mask).count('1') % 2: mult -= bound // div 
            else: mult += bound // div
        
        mult %= MOD
        res = (res * mult) % MOD

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        A = list(map(int, input().split()))
        res = solve(N, M, A)
        print(res)


if __name__ == '__main__':
    main()

