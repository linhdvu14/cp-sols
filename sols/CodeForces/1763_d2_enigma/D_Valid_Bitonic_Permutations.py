''' D. Valid Bitonic Permutations
https://codeforces.com/contest/1763/problem/D
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

def precalc_nCk(N, mod):
    fact, inv_fact = [1] * (N + 1), [1] * (N + 1)
    for i in range(1, N + 1): fact[i] = i * fact[i - 1] % mod
    inv_fact[-1] = pow(fact[-1], mod - 2, mod)
    for i in range(N - 1, 0, -1): inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod
    return fact, inv_fact


MOD = 10**9 + 7
MAX = 120
FACT = INV_FACT = None

def nCk(n, k): 
    if not FACT: FACT, INV_FACT = precalc_nCk(MAX, MOD)
    return 0 if k > n else FACT[n] * INV_FACT[k] * INV_FACT[n - k] % MOD


def solve_1(m, ia, ib, a, b):
    if a > b: a, b, ia, ib = b, a, m + 1 - ib, m + 1 - ia

    res = 0

    # x=1..a-1, y=a+1..b-1, z=b+1..m-1
    nx, ny, nz = a - 1, b - 1 - a, m - 1 - b

    if b < m: 
        # (p: x1) a (q: y1, z1) m (r: z2) b (s: x2, y2)
        for im in range(ia + 1, ib):
            p, q, r, s = ia - 1, im - ia - 1, ib - im - 1, m - ib 
            x1, z2 = p, r 
            x2, z1 = nx - x1, nz - z2
            y1, y2 = q - z1, s - x2 
            if min(x1, x2, y1, y2, z1, z2) >= 0: res = (res + nCk(nx, x1) * nCk(ny, y1) * nCk(nz, z1)) % MOD
        
        # (p: x1) a (q: y1) b (r: z1) m (s: x2, y2, s2)
        for im in range(ib + 1, m):
            p, q, r, s = ia - 1, ib - ia - 1, im - ib - 1, m - ib 
            x1, y1, z1 = p, q, r 
            x2, y2, z2 = nx - x1, ny - y1, nz - z1 
            if min(x1, x2, y1, y2, z1, z2) >= 0: res = (res + nCk(nx, x1) * nCk(ny, y1) * nCk(nz, z1)) % MOD
    
    elif 2 <= ib <= m - 1:  # (p: x1) a (q: y1) b=m (r: x2, y2)
        p, q, r = ia - 1, ib - ia - 1, m - ib
        x1, y1 = p, q
        x2, y2 = nx - x1, ny - y1
        if min(x1, x2, y1, y2) >= 0: res = (res + nCk(nx, x1) * nCk(ny, y1)) % MOD        

    return res


# https://codeforces.com/blog/entry/110278?#comment-983580
def solve_2(M, ia, ib, a, b):
    def is_valid(pos, val): 
        if (pos == ia) != (val == a): return False
        if (pos == ib) != (val == b): return False
        if val == M and (pos == 1 or pos == M): return False
        return True

    # dp[l][r] = num valid ways to place 1..l+r vals s.t. l vals on left/increasing and r vals on right/decreasing
    dp = [[0] * M for _ in range(M)]
    dp[0][0] = 1
    for i in range(1, M): 
        if is_valid(i, i): dp[i][0] = dp[i - 1][0]
        if is_valid(M - i + 1, i): dp[0][i] = dp[0][i - 1]

    res = 0
    for l in range(1, M):
        for r in range(1, M - l + 1):
            if is_valid(l, l + r): dp[l][r] = (dp[l][r] + dp[l - 1][r]) % MOD 
            if is_valid(M - r + 1, l + r): dp[l][r] = (dp[l][r] + dp[l][r - 1]) % MOD
            if l + r == M: res = (res + dp[l][r]) % MOD

    return res * pow(2, MOD - 2, MOD) % MOD


solve = solve_2

def main():
    T = int(input())
    for _ in range(T):
        m, ia, ib, a, b = list(map(int, input().split()))
        res = solve(m, ia, ib, a, b)
        print(res)


if __name__ == '__main__':
    main()

