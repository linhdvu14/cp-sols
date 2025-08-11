''' G1. Magic Triples (Easy Version)
https://codeforces.com/contest/1822/problem/G1
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

INF = float('inf')

# -----------------------------------------

from random import randrange
class IntKeyDict(dict):
    rand = randrange(1 << 62)
    def __setitem__(self, k, v): super().__setitem__(k^self.rand, v)
    def __getitem__(self, k): return super().__getitem__(k^self.rand)
    def __contains__(self, k): return super().__contains__(k^self.rand)
    def __repr__(self): return str({k: v for k, v in self.items()})
    def get(self, k, default=None): return super().get(k^self.rand, default)
    def keys(self): return [k^self.rand for k in super().keys()]
    def items(self): return [(k^self.rand, v) for k, v in super().items()]
    def pop(self, k): return super().pop(k^self.rand)


def get_lpf(M, bound):
    primes = []
    lpf = [0] * (M + 1)  # least prime factor
    for i in range(2, M + 1):
        if lpf[i] == 0:
            if i <= bound: primes.append(i)
            lpf[i] = i
        for p in primes:
            if p * i > M or p > lpf[i]: break  # lpf[p*i] <= lpf[i] < p
            lpf[p * i] = p                     # set once per composite number
    return lpf

MAX = 10**6
MAX_B = int(MAX**0.5) + 2

LPF = get_lpf(MAX, MAX_B)
FACS = IntKeyDict()

def get_facs(x):
    if x in FACS: return FACS[x]
    facs = [1]
    while x > 1:
        p, cnt = LPF[x], 0
        while x % p == 0:
            x //= p
            cnt += 1
        for i in range(len(facs)):
            for j in range(1, cnt + 1):
                nf = facs[i] * p ** j
                if nf <= MAX_B: facs.append(nf)
    FACS[x] = facs
    return facs


def solve(N, A):
    cnt = IntKeyDict()
    for a in A: cnt[a] = cnt.get(a, 0) + 1

    A = sorted(cnt.keys())
    res = 0
    for a in A:
        n = cnt[a]
        res += n * (n - 1) * (n - 2)
        for f in get_facs(a):
            if f == 1: continue
            n1 = cnt.get(a // f, 0)
            n2 = cnt.get(a * f, 0)
            res += n * n1 * n2

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
