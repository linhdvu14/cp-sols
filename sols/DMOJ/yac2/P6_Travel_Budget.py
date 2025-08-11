''' Yet Another Contest 2 P6 - Travel Budget
https://dmoj.ca/problem/yac2p6
'''

import os, sys
input = sys.stdin.readline  # strip() if str

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


# -----------------------------------------

INF = 10**20 # WA if float('inf')
from typing import Tuple, List
from bisect import bisect_left

class LiChaoTree:
    def __init__(self, X: List[int]) -> None:
        X = sorted(list(set(X)))
        n = len(X)
        self.offset = sz = 1 << n.bit_length()
        self.X = X + [INF] * (sz - n)
        self.data = [None] * (2 * sz)

    def _add(self, line: Tuple[int, int], i: int, l: int, r: int) -> None:
        while True:
            if self.data[i] is None: self.data[i] = line; break
            m = (l + r) // 2
            lx, mx, rx = self.X[l], self.X[m], self.X[r - 1]
            lu = self.f(line, lx) < self.f(self.data[i], lx)
            mu = self.f(line, mx) < self.f(self.data[i], mx)
            ru = self.f(line, rx) < self.f(self.data[i], rx)
            if lu and ru: self.data[i] = line; break
            if not lu and not ru: break
            if mu: self.data[i], line = line, self.data[i]
            if lu != mu: r, i = m, i << 1
            else: l, i = m, i << 1 | 1

    def add_line(self, line: Tuple[int, int]) -> None:
        '''insert line'''
        self._add(line, 1, 0, self.offset)

    def add_seg(self, line: Tuple[int, int], l: int, r: int) -> None:
        '''insert line to segment [l, r)'''
        l = bisect_left(self.X, l)
        r = bisect_left(self.X, r)
        l0, r0 = l + self.offset, r + self.offset
        size = 1
        while l0 < r0:
            if l0 & 1:
                self._add(line, l0, l, l + size)
                l0 += 1
                l += size
            if r0 & 1:
                r0 -= 1
                r -= size
                self._add(line, r0, r, r + size)
            l0 >>= 1
            r0 >>= 1
            size <<= 1

    def query(self, x: int) -> int:
        '''find min f(x)'''
        i = bisect_left(self.X, x) + self.offset
        res = INF
        while i > 0:
            if self.data[i] is not None: res = min(res, self.f(self.data[i], x))
            i >>= 1
        return res

    def f(self, line: Tuple[int, int], x: int) -> int:
        return line[0] * x + line[1]



def main(N, A):    
    X = []
    for p, s, _, _ in A: X.extend([p, p + s + 1])
    lctree = LiChaoTree(X)
    
    for i, (p, s, c, d) in enumerate(A):
        if i == 0:
            lctree.add_seg((c, d), 0, s + 1)
        else:
            # min cost so far to get to p and hire this car
            # subtract cost to drive this car from 0..p
            cost = lctree.query(p) + d - c * p
            lctree.add_seg((c, cost), p, p + s + 1)
    
    return lctree.query(A[-1][0])



if __name__ == '__main__':
    N = int(input())
    A = [tuple(map(int, input().split())) for _ in range(N)]
    out = main(N, A)
    print(out)

