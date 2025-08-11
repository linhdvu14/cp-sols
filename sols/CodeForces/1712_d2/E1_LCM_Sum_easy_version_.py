''' E1. LCM Sum (easy version)
https://codeforces.com/contest/1712/problem/E1
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

def get_lpf(N):
    lpf = [1] * (N + 1)
    primes = []
    for i in range(2, N+1):
        if lpf[i] == 1:
            lpf[i] = i
            primes.append(i)
        for p in primes:
            if p * i > N or lpf[i] < p: break
            lpf[p * i] = p 
    return lpf

LPF = get_lpf(2 * 10**5)

def get_divisors(x):
    cur = [1]
    while x > 1:
        p, cnt = LPF[x], 0
        while x % p == 0:
            cnt += 1
            x //= p 
        nxt = []
        for d in cur:
            for i in range(1, cnt+1):
                nxt.append(d * p**i)
        cur.extend(nxt)
    return cur


# a < b < c
# lcm(a, b, c) = c -> always bad
# lca(a, b, c) = 2c -> bad if a + b > c
# lca(a, b, c) = mc where m >= 3 -> always good

# consider lca(a, b, c) = 2c
# a < b < c = 2c/2 -> b must be 2c/m with m >= 3, a must be 2c/m with m >= 4
# a + b > c, a <= c/2 -> b > c/2 -> b = 2c/3
# a + b > c, b = 2c/3 -> a > c/3 -> a = c/2 or 2c/5
# a/b/c is 3/4/6 or 6/10/15

def solve(l, r):
    def count(c):
        bad = 0

        # lcm(a, b, c) = c
        divs = get_divisors(c)
        n = sum(1 for d in divs if l <= d < c)
        bad += n * (n - 1) // 2

        # lcm(a, b, c) = 2c
        if c % 6 == 0 and c // 2 >= l: bad += 1
        if c % 15 == 0 and 2 * c // 5 >= l: bad += 1

        return bad

    res = (r - l + 1) * (r - l) * (r - l - 1) // 6
    for c in range(l+2, r+1): res -= count(c)
    return res


def main():
    T = int(input())
    for _ in range(T):
        l, r = list(map(int, input().split()))
        out = solve(l, r)
        print(out)


if __name__ == '__main__':
    main()
