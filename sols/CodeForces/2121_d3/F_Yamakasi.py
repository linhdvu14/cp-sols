''' F. Yamakasi
https://codeforces.com/contest/2121/problem/F
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

from inspect import currentframe, getframeinfo
from re import search
DEBUG = os.environ.get('debug') not in [None, '0']

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
from random import randrange
class IntKeyDict(dict):
    rand = randrange(1 << 62)
    def __setitem__(self, k, v): super().__setitem__(k^self.rand, v)
    def __getitem__(self, k): return super().__getitem__(k^self.rand)
    def __contains__(self, k): return super().__contains__(k^self.rand)
    def __repr__(self): return str({k: v for k, v in self.items()})
    def __init__(self, d): super().__init__({k^self.rand: v for k, v in d.items()})
    def get(self, k, default=None): return super().get(k^self.rand, default)
    def keys(self): return [k^self.rand for k in super().keys()]
    def items(self): return [(k^self.rand, v) for k, v in super().items()]
    def pop(self, k): return super().pop(k^self.rand)


def solve(N, S, X, A):
    res = s = i = 0
    ps = IntKeyDict({0: 1})
    
    while i < N:
        if A[i] > X:
            s = 0
            ps = IntKeyDict({0: 1})
            i += 1
        elif A[i] < X:
            s += A[i]
            ps[s] = ps.get(s, 0) + 1
            i += 1
        else:
            sj, j = s + A[i], i + 1
            res += ps.get(sj - S, 0)
            while j < N and A[j] < X:
                sj += A[j]
                res += ps.get(sj - S, 0)
                j += 1
            for k in range(i, j):
                s += A[k]
                ps[s] = ps.get(s, 0) + 1
            i = j

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, S, X = list(map(int, input().split()))
        A = list(map(int, input().split()))
        res = solve(N, S, X, A)
        print(res)


if __name__ == '__main__':
    main()
