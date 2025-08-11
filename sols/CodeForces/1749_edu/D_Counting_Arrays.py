''' D. Counting Arrays
https://codeforces.com/contest/1749/problem/D
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

def is_prime(n):
    '''Miller-Rabin primality test'''
    if n < 5 or n & 1 == 0 or n % 3 == 0: return 2 <= n <= 3
    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p == 1 or p == n - 1 or a % n == 0: continue
        for _ in range(s):
            p = (p * p) % n
            if p == n - 1: break
        else: return False
    return True


# build unambiguous array a[1], a[2], a[3], ...
# a[1] can be anything
# a[2] needs gcd(a[2], 2) > 1
# a[3] needs gcd(a[3], 3) > 1, gcd(a[3], 2) > 1
# a[n] needs gcd(a[n], k) > 1 for k = 2..n
def solve(N, M):
    if M == 1: return N - 1

    res = (M * (1 - pow(M, N, MOD)) * pow(1 - M, MOD - 2, MOD)) % MOD
    p = q = 1
    for n in range(1, N + 1):
        if q > M: break 
        if is_prime(n): q *= n
        p = (p * (M // q)) % MOD
        res = (res - p) % MOD

    return res


def main():
    N, M = list(map(int, input().split()))
    res = solve(N, M)
    print(res)


if __name__ == '__main__':
    main()

