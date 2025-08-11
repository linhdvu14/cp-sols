''' F - Rectangle GCD
https://atcoder.jp/contests/abc254/tasks/abc254_f
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

from math import gcd
from typing import TypeVar, Generic, List
T = TypeVar('T')

class Info:
    def __init__(self, v=None): 
        self.v = v
    
    def __add__(self, other): 
        if not self.v: return other
        if not other.v: return self
        return Info(gcd(self.v, other.v))

class SegmentTree(Generic[T]):
    def __init__(self, init_arr: List[T], default: T) -> None:
        '''initialize with data'''
        n = len(init_arr) 
        self.offset = sz = 1 << (n - 1).bit_length()
        self.default = default

        self.val = [default] * (2 * sz)
        self.val[sz : sz + n] = init_arr
        for i in reversed(range(sz)):
            self.val[i] = self.val[2*i] + self.val[2*i + 1]

    def query(self, l: int, r: int) -> T:
        '''range query l..r'''
        l += self.offset
        r += self.offset + 1
        res = self.default
        while l < r:
            if l & 1:
                res += self.val[l]
                l += 1
            if r & 1:
                r -= 1
                res += self.val[r]
            l >>= 1
            r >>= 1
        return res


# gcd(a1, b1, *, *) = gcd(a1+b1, b2-b1, b3-b2, b4-b3,..., a2-a1, a3-a2, a4-a3...)
def main():
    N, Q = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    segtree_A = SegmentTree([Info(A[i] - A[i-1]) for i in range(1, N)], Info())
    segtree_B = SegmentTree([Info(B[i] - B[i-1]) for i in range(1, N)], Info())

    res = [-1] * Q
    for i in range(Q):
        h1, h2, w1, w2 = list(map(int, input().split()))
        h1 -= 1; h2 -= 1; w1 -= 1; w2 -= 1
        g = A[h1] + B[w1]
        if h1 != h2: g = gcd(g, segtree_A.query(h1, h2 - 1).v)
        if w1 != w2: g = gcd(g, segtree_B.query(w1, w2 - 1).v)
        res[i] = g
    
    print(*res, sep='\n')


if __name__ == '__main__':
    main()

