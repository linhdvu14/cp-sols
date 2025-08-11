''' F - Cumulative Cumulative Cumulative Sum
https://atcoder.jp/contests/abc256/tasks/abc256_f
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

from typing import TypeVar, Generic, List
T = TypeVar('T')

class Info:
    def __init__(self, v1=0, v2=0, v3=0): 
        self.v1 = v1 % MOD
        self.v2 = v2 % MOD
        self.v3 = v3 % MOD
    
    def __add__(self, other): 
        return Info(self.v1 + other.v1, self.v2 + other.v2, self.v3 + other.v3)


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
    
    def get(self, i: int) -> T:
        '''get nums[i]'''
        return self.val[i + self.offset]

    def set(self, i: int, x: T) -> None:
        '''set nums[i] = x'''
        # upd correct leaf then prop to ancestors
        i += self.offset
        self.val[i] = x
        i >>= 1
        while i:
            self.val[i] = self.val[2*i] + self.val[2*i + 1]
            i >>= 1

    def query(self, l: int, r: int) -> T:
        '''range query l..r'''
        # add all nodes under bst then center in
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


# A[i]'s contribution to x >= i:
# B[x]: 1
# C[x]: x - i + 1
# D[x]: SUM_{k=i..x} (k - i + 1) * d = (x - i + 1) * (x - i + 2) // 2
# --> D[x] = SUM_{i=0..x} (x - i + 1) * (x - i + 2) * A[i] // 2
#          = 1/2 SUM_{i=0..x} i^2 A[i] - (2x + 3)/2 SUM_{i=0..x} iA[i] + (x+1)(x+2)/2 SUM_{i=0..x} A[i]
# segtree query (0, x) returns (SUM_{i=0..x} i^2 A[i], SUM_{i=0..x} i*A[i], SUM_{i=0..x} A[i])
def main():
    N, Q = list(map(int, input().split()))
    A = list(map(int, input().split()))

    segtree = SegmentTree[Info]([Info(i*i*a, i*a, a) for i, a in enumerate(A)], Info())
    INV_TWO = pow(2, MOD-2, MOD)

    res = []
    for _ in range(Q):
        ts = list(map(int, input().split()))
        if ts[0] == 1:
            x, a = ts[1] - 1, ts[2]
            segtree.set(x, Info(x*x*a, x*a, a))
        else:
            x = ts[1] - 1
            v = segtree.query(0, x)
            d = ((v.v1 - (2 * x + 3) * v.v2 + (x + 1) * (x + 2) * v.v3) * INV_TWO) % MOD
            res.append(d)
            
    print(*res, sep='\n')


# https://atcoder.jp/contests/abc256/submissions/32577323
# D[x] = SUM_{i=0..x} (x - i + 1) * (x - i + 2) * A[i] // 2 
#      = 1*2*A[x]//2 + 2*3*A[x-1]//2 + ... + (x+1)*(x+2)*A[0]//2
# segtree query (l, r) returns 1*2*A[r]//2 + 2*3*A[r-1]//2 + ... + (r-l+1)*(r-l+2)*A[l]//2


if __name__ == '__main__':
    main()


