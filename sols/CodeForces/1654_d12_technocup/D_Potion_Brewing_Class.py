''' D. Potion Brewing Class
https://codeforces.com/contest/1654/problem/D
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') not in [None, '0']

if DEBUG:
    from inspect import currentframe, getframeinfo
    from re import search

def debug(*args):
    if not DEBUG: return
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')


INF = float('inf')

# -----------------------------------------

MOD = 998244353
import typing
from collections import defaultdict

class ModInt:
    def __init__(self, v: int = 0) -> None:
        if v == 0: self._v = 0
        else: self._v = v % MOD

    @staticmethod
    def inv_gcd(a: int, b: int) -> typing.Tuple[int, int]:
        a %= b
        if a == 0: return (b, 0)

        s, t, m0, m1 = b, a, 0, 1
        while t:
            u = s // t
            s -= t * u
            m0 -= m1 * u
            s, t = t, s
            m0, m1 = m1, m0

        if m0 < 0: m0 += b // s
        return (s, m0)
    
    @staticmethod
    def raw(v: int) -> 'ModInt':
        x = ModInt()
        x._v = v
        return x

    def val(self) -> int:
        return self._v

    def inv(self) -> 'ModInt':
        '''v ^ (-1) % mod'''
        eg = self.inv_gcd(self._v, MOD)
        assert eg[0] == 1
        return ModInt(eg[1])

    def __iadd__(self, rhs: typing.Union['ModInt', int]) -> 'ModInt':  # +=
        if isinstance(rhs, ModInt): self._v += rhs._v
        else: self._v += rhs
        if self._v >= MOD: self._v -= MOD
        return self

    def __isub__(self, rhs: typing.Union['ModInt', int]) -> 'ModInt':
        if isinstance(rhs, ModInt): self._v -= rhs._v
        else: self._v -= rhs
        if self._v < 0: self._v += MOD
        return self

    def __imul__(self, rhs: typing.Union['ModInt', int]) -> 'ModInt':
        if isinstance(rhs, ModInt): self._v = self._v * rhs._v % MOD
        else: self._v = self._v * rhs % MOD
        return self

    def __itruediv__(self, rhs: typing.Union['ModInt', int]) -> 'ModInt': # /=
        if isinstance(rhs, ModInt): inv = rhs.inv()._v
        else: inv = self.inv_gcd(rhs, MOD)[1]
        self._v = self._v * inv % MOD
        return self

    def __pos__(self) -> 'ModInt':
        return self

    def __neg__(self) -> 'ModInt':
        return ModInt() - self

    def __pow__(self, n: int) -> 'ModInt':
        assert 0 <= n
        return ModInt(pow(self._v, n, MOD))

    def __add__(self, rhs: typing.Union['ModInt', int]) -> 'ModInt':
        if isinstance(rhs, ModInt):
            result = self._v + rhs._v
            if result >= MOD: result -= MOD
            return self.raw(result)
        else:
            return ModInt(self._v + rhs)

    def __sub__(self, rhs: typing.Union['ModInt', int]) -> 'ModInt':
        if isinstance(rhs, ModInt):
            result = self._v - rhs._v
            if result < 0: result += MOD
            return self.raw(result)
        else:
            return ModInt(self._v - rhs)

    def __mul__(self, rhs: typing.Union['ModInt', int]) -> 'ModInt':
        if isinstance(rhs, ModInt): return ModInt(self._v * rhs._v)
        else: return ModInt(self._v * rhs)

    def __truediv__(self, rhs: typing.Union['ModInt', int]) -> 'ModInt':
        if isinstance(rhs, ModInt): inv = rhs.inv()._v
        else: inv = self.inv_gcd(rhs, MOD)[1]
        return ModInt(self._v * inv)

    def __eq__(self, rhs: typing.Union['ModInt', int]) -> bool:  # type: ignore
        if isinstance(rhs, ModInt): return self._v == rhs._v
        else: return self._v == rhs % MOD

    def __ne__(self, rhs: typing.Union['ModInt', int]) -> bool:  # type: ignore
        if isinstance(rhs, ModInt): return self._v != rhs._v
        else: return self._v != rhs % MOD


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


def gcd(a, b):
    if a < b: a, b = b, a
    while b > 0: a, b = b, a % b
    return a


def batch_lpf(N):
    lpf = [0] * (N+1)
    primes = []
    for i in range(2, N+1):
        if lpf[i] == 0:
            lpf[i] = i
            primes.append(i)
        for p in primes:
            if i*p > N or lpf[i] < p: break
            lpf[i*p] = p
    return lpf

LPF = batch_lpf(2 * 10**5)

def solve(N, reqs):
    adj = [[] for _ in range(N)]
    for u, v, x, y in reqs:
        g = gcd(x, y)
        x //= g
        y //= g
        adj[u-1].append((v-1, x, y))
        adj[v-1].append((u-1, y, x))

    # take root val = 1 and all others as prod of fractions to calc sum
    # maintain max_cnt[p] = max(denom[p] - num[p], 0) for all prime p, over all nodes
    # ues max_cnt to normalize root to be lcm of all nodes' denom
    s = ModInt(0)
    max_cnt = defaultdict(int)

    @bootstrap
    def dfs(u, val=ModInt(1), p=-1, cur_cnt=defaultdict(int)):
        nonlocal s
        s += val
        for v, x, y in adj[u]:
            if v == p: continue
            
            z = y
            while z > 1:
                cur_cnt[LPF[z]] -= 1
                z //= LPF[z]

            z = x
            while z > 1:
                cur_cnt[LPF[z]] += 1
                max_cnt[LPF[z]] = max(max_cnt[LPF[z]], cur_cnt[LPF[z]])
                z //= LPF[z]
            
            yield dfs(v, val * y / x, u, cur_cnt)

            z = y
            while z > 1:
                cur_cnt[LPF[z]] += 1
                z //= LPF[z]

            z = x
            while z > 1:
                cur_cnt[LPF[z]] -= 1
                max_cnt[LPF[z]] = max(max_cnt[LPF[z]], cur_cnt[LPF[z]])
                z //= LPF[z]
        yield None

    dfs(0)
    norm = ModInt(1)
    for f, dup in max_cnt.items():
        norm *= pow(f, dup, MOD)

    res = s * norm
    return res.val()


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        reqs = [list(map(int, input().split())) for _ in range(N-1)]
        out = solve(N, reqs)
        print(out)


if __name__ == '__main__':
    main()

