''' F. Ira and Flamenco
https://codeforces.com/contest/1833/problem/F
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
MOD = 10**9 + 7

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


def solve(N, M, A):
    cnt = IntKeyDict()
    for a in A: cnt[a] = cnt.get(a, 0) + 1

    B = sorted(list(cnt.keys()))

    res = j = 0
    for i, b in enumerate(B):
        if not i or b != B[i - 1] + 1:
            j = i 
            ways = 1
        ways = ways * cnt[b] % MOD 
        if i - j + 1 > M:
            ways = ways * pow(cnt[B[j]], MOD - 2, MOD) % MOD
            j += 1
        if i - j + 1 == M:
            res += ways

    return res % MOD 


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        A = list(map(int, input().split()))
        res = solve(N, M, A)
        print(res)


if __name__ == '__main__':
    main()

