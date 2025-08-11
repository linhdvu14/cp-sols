''' B. Number Factorization
https://codeforces.com/contest/1787/problem/B
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


def solve(N):
    cnt = IntKeyDict()
    
    p = 2
    while p * p <= N:
        while N % p == 0:
            cnt[p] = cnt.get(p, 0) + 1
            N //= p 
        p += 1
    if N > 1: cnt[N] = cnt.get(N, 0) + 1

    res = 0
    while cnt:
        b, e = 1, INF
        for k, v in cnt.items():
            b *= k 
            e = min(e, v)
        for k, v in cnt.items():
            cnt[k] -= e 
            if not cnt[k]: cnt.pop(k)
        res += b * e 

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        res = solve(N)
        print(res)


if __name__ == '__main__':
    main()

