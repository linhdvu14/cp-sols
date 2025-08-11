''' D2. The Endspeaker (Hard Version)
https://codeforces.com/contest/2027/problem/D2
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
from bisect import bisect_right

MOD = 10**9 + 7

from typing import TypeVar, Generic, List
T = TypeVar('T')


class Info:
    def __init__(self, cost=0, cnt=0): 
        self.cost = cost
        self.cnt = cnt
    
    def __add__(self, other): 
        if self.cost < other.cost: return Info(self.cost, self.cnt)
        if self.cost == other.cost: return Info(self.cost, (self.cnt + other.cnt) % MOD)
        return Info(other.cost, other.cnt)
    
    def __repr__(self):
        return f'Info(cost={self.cost}, cnt={self.cnt})'


class SegmentTree(Generic[T]):
    def __init__(self, N: int, default: T) -> None:
        self.N = N
        self.default = default
        self.offset = sz = 1 << (N - 1).bit_length()
        self.val = [default for _ in range(2 * sz)]
    
    def _combine(self, l: T, r: T) -> T:
        '''combine value from 2 child segments TODO: change here'''
        return l + r

    def build(self, init_arr: List[T]) -> None:
        self.val[self.offset : self.offset + len(init_arr)] = init_arr
        for i in reversed(range(self.offset)):
            self.val[i] = self._combine(self.val[2*i], self.val[2*i + 1])

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
            self.val[i] = self._combine(self.val[2*i], self.val[2*i + 1])
            i >>= 1

    def query(self, l: int, r: int) -> T:
        '''range query l..r'''
        # add all nodes under bst then center in
        l += self.offset
        r += self.offset + 1
        res = self.default
        while l < r:
            if l & 1:
                res = self._combine(res, self.val[l])
                l += 1
            if r & 1:
                r -= 1
                res = self._combine(res, self.val[r])
            l >>= 1
            r >>= 1
        return res



def solve(N, M, A, B):
    if max(A) > B[0]: return [-1]

    ps = [0] * (N + 1)
    for i, a in enumerate(A): ps[i + 1] = ps[i] + a

    segtree = SegmentTree(N + 1, Info(INF, 1))
    segtree.set(N, Info(0, 1))

    for k in range(M - 1, -1, -1):
        for i in range(N - 1, -1, -1):
            j = bisect_right(ps, ps[i] + B[k]) - 1
            if j > i: 
                v1 = segtree.query(i, i)
                v2 = segtree.query(i, j)
                v = segtree._combine(v1, Info(M - k - 1 + v2.cost, v2.cnt))
                segtree.set(i, v)
    
    res = segtree.query(0, 0)
    return res.cost, res.cnt



def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        res = solve(N, M, A, B)
        print(*res)


if __name__ == '__main__':
    main()

