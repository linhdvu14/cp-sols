''' C. Circular Mirror
https://codeforces.com/contest/1725/problem/C
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
    for i in range(1, N+1): fact[i] = i * fact[i-1] % p
    inv_fact = [1] * (N+1)  # (1 / n!) % p
    inv_fact[-1] = pow(fact[-1], p-2, p)
    for i in range(N-1, 0, -1): inv_fact[i] = inv_fact[i + 1] * (i + 1) % p
    return fact, inv_fact

MOD = 998244353


def main():
    N, M = list(map(int, input().split()))
    D = list(map(int, input().split()))

    pos = [0]
    for d in D: pos.append(pos[-1] + d)
    sz = pos.pop()

    # no diagonal, can have any color
    if sz & 1: print(pow(M, N, MOD)); return

    # count diagonals
    sz //= 2
    cnt = r = 0
    for p in pos:
        if p >= sz: break
        while r < N and p + sz > pos[r]: r += 1
        if r < N and p + sz == pos[r]: cnt += 1
    rem = N - 2 * cnt

    FACT, INV_FACT = precalc_nCk(max(cnt, M), MOD)
    def nCk(n, k): return (FACT[n] * INV_FACT[k] * INV_FACT[n - k]) % MOD

    # num ways s.t. exactly k diagonals have same color endpoints
    res = 0
    for k in range(min(M, cnt) + 1):
        # k diagonals with same color endpoints -> k different colors
        m = nCk(cnt, k) * nCk(M, k) * FACT[k] % MOD

        # cnt-k diagonals with diff color endpoints -> M-k color choices
        m = m * pow((M - k) * (M - k - 1) % MOD, cnt - k, MOD) % MOD

        # N-2*cnt non-diagonal points -> M-k color choices
        if rem: m = m * pow(M - k, rem, MOD) % MOD

        res = (res + m) % MOD

    print(res)


if __name__ == '__main__':
    main()

