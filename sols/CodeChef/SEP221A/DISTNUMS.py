''' Distinct Numbers
https://www.codechef.com/SEP221A/problems/DISTNUMS
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

def sieve(N):
    primes = []
    lpf = [0] * (N + 1)  # least prime factor
    for i in range(2, N + 1):
        if lpf[i] == 0:
            primes.append(i)
            lpf[i] = i
        for p in primes:
            if p*i > N or p > lpf[i]: break  # lpf[p*i] <= lpf[i] < p
            lpf[p*i] = p                     # set once per composite number
    return lpf


MOD = 10**9 + 7
LPF = sieve(10**7)

# N = p1^m1 + p2^m2 + ...
# ans = (p1^m1 + p1^(m1+1) + ... + p1^(m1 * 2^k)) * (p2^m2 + p2^(m2+1) + ... + p2^(m2 * 2^k)) * ...
# p^m (1 + p + ... + p^(m2^k - m)) = p^m (1 - p^(m2^k - m + 1)) / (1 - p)

def solve(N, K):
    res = 1
    
    while N > 1:
        p, m = LPF[N], 0
        while N % p == 0:
            m += 1
            N //= p
        res = (res * pow(p, m, MOD) * (1 - pow(p, m * pow(2, K, MOD-1) - m + 1, MOD)) * pow(1 - p, MOD-2, MOD)) % MOD

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        res = solve(N, K)
        print(res)


if __name__ == '__main__':
    main()

