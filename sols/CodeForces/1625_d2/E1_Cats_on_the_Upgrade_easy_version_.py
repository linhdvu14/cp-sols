''' E1. Cats on the Upgrade (easy version)
https://codeforces.com/contest/1625/problem/E1
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
from typing import List


class SegmentTreeInfo:
    def __init__(self, parent=INF, sum=0, cnt=0): 
        self.parent = parent  # over all ( inside this substring, what's the leftmost parent idx
        self.cnt = cnt        # over all ( inside this substring, how many are direct child of self.parent
        self.sum = sum        # over all ( inside this substring that are direct child of self.parent, what's the sum of their subtree RBS count (recursive, subtree lies inside substring but not necessarily all covered by segtree segment)

    def __add__(self, other): 
        res = SegmentTreeInfo()
        # if have same par, obvious
        # if l is par of r, this step adds r's direct children (l's grandchildren)
        # l's direct children includes r and already counted in l.sum
        res.sum = self.sum + other.sum

        if self.parent < other.parent: res.parent, res.cnt = self.parent, self.cnt
        elif self.parent > other.parent: res.parent, res.cnt = other.parent, other.cnt
        else: res.parent, res.cnt = self.parent, self.cnt + other.cnt
        return res
    
    def __repr__(self):
        return f'SegmentTreeInfo(parent={self.parent},sum={self.sum},cnt={self.cnt})'


class SegmentTree:
    def __init__(self, lo: int, hi: int, init_arr: List[SegmentTreeInfo] = None) -> None:
        '''init segtree intervals, optionally with data'''
        self.lo, self.hi = lo, hi
        self.mi = mi = (lo + hi) // 2
        self.info = SegmentTreeInfo()
        if lo == hi and init_arr: self.info = init_arr[lo]
        elif lo < hi:
            self.left = SegmentTree(lo, mi)
            self.right = SegmentTree(mi+1, hi)

    def query(self, qlo: int, qhi: int) -> SegmentTreeInfo:
        '''range query qlo..qhi intersect self.lo..self.hi'''
        if qlo < self.lo or qhi > self.hi: return SegmentTreeInfo()
        if qlo == self.lo and qhi == self.hi: return self.info
        res = SegmentTreeInfo()
        if qlo <= self.mi: res += self.left.query(qlo, min(qhi, self.mi))
        if qhi > self.mi: res += self.right.query(max(qlo, self.mi+1), qhi)
        return res
    
    def update(self, qi: int, v: SegmentTreeInfo):
        '''update this segment and children when data[qi]=v'''
        if qi < self.lo or qi > self.hi: return
        if qi == self.lo == self.hi: self.info = v
        else:
            if qi <= self.mi: self.left.update(qi, v)
            else: self.right.update(qi, v)
            self.info = SegmentTreeInfo()  # update from child
            if self.left: self.info += self.left.info
            if self.right: self.info += self.right.info


def solve():
    N, Q = map(int, input().split())
    S = input().decode().strip()

    # build bracket tree: go down 1 level for (, up for )
    # each vertex is a RBS
    # par[i] = index of parent ( for S[i] = (; might be set when bracket invalid
    # match[i] = index of matching bracket of S[i]; only set when bracket valid
    par = [-1] * N
    match = [-1] * N
    stack = []
    for i, c in enumerate(S):
        if c == '(':
            stack.append(i)
        elif stack:  # skip unmatched brackets
            j = stack.pop()
            match[i], match[j] = j, i
            if j > 0:
                if S[j-1] == '(': par[j] = j-1                    # parent and child
                elif match[j-1] != -1: par[j] = par[match[j-1]]   # siblings

    # count num children under each RBS
    deg = [0] * N
    for i in range(N):
        if par[i] != -1:  # opening bracket
            deg[par[i]] += 1

    # update at each RBS opening
    segtree = SegmentTree(0, N-1)
    for i in range(N):
        if i < match[i]:  # opening bracket
            segtree.update(i, SegmentTreeInfo(par[i], deg[i] * (deg[i] + 1) // 2, 1))

    # segtree.query(l, r) = num RBS within S[l..r]
    res = []
    for _ in range(Q):
        _, l, r = map(int, input().split())
        v = segtree.query(l-1, r-1)
        res.append(v.sum + v.cnt * (v.cnt + 1) // 2)
    
    print('\n'.join(map(str, res)))


if __name__ == '__main__':
    solve()
 