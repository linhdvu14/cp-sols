''' Problem D: Today is Gonna be a Great Day
https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/D
'''

import os, sys
input = sys.stdin.readline  # strip() if str
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


class LazySegmentTreeRecursive:
    '''with lazy add'''
    def __init__(self, N):
        self.N = N
        sz = 1 << ((N - 1).bit_length() + 1)
        self.lazy = [0] * sz
        self.mn = [INF] * sz
        self.mx = [-INF] * sz
        self.mni = [-1] * sz
        self.mxi = [-1] * sz  

    @bootstrap
    def build(self, init_arr, ti=0, tl=0, tr=-1):  
        if tr == -1: tr = self.N - 1
        if tl == tr: 
            self.mn[ti] = self.mx[ti] = init_arr[tl]
            self.mni[ti] = self.mxi[ti] = tl
        else:
            tm = (tl + tr) // 2
            yield self.build(init_arr, 2*ti + 1, tl, tm)
            yield self.build(init_arr, 2*ti + 2, tm + 1, tr)
            self._pull(ti)
        yield None

    @bootstrap
    def _pull(self, ti):
        '''TODO: change here'''
        li, ri = 2*ti + 1, 2*ti + 2
        if self.mn[li] <= self.mn[ri]: self.mn[ti], self.mni[ti] = self.mn[li], self.mni[li]
        else: self.mn[ti], self.mni[ti] = self.mn[ri], self.mni[ri]
        if self.mx[li] >= self.mx[ri]: self.mx[ti], self.mxi[ti] = self.mx[li], self.mxi[li]
        else: self.mx[ti], self.mxi[ti] = self.mx[ri], self.mxi[ri]

    def _push(self, ti, tl, tr, x):
        '''TODO: change here'''
        if not x: return 
        self.mn[ti], self.mx[ti] = MOD - self.mx[ti], MOD - self.mn[ti]
        self.mni[ti], self.mxi[ti] = self.mxi[ti], self.mni[ti]
        if tl != tr:
            self.lazy[ti*2 + 1] ^= 1
            self.lazy[ti*2 + 2] ^= 1

    def push(self, ti, tl, tr):
        '''update parent val; push parent's lazy update to children'''
        self._push(ti, tl, tr, self.lazy[ti])
        self.lazy[ti] = 0

    @bootstrap
    def query(self, ql, qr, ti=0, tl=0, tr=-1) -> int: 
        '''range query ql..qr intersect tl..tr (seg idx ti)'''
        if tr == -1: tr = self.N - 1
        self.push(ti, tl, tr)

        if ql > tr or qr < tl: yield -INF, -1
        if ql <= tl <= tr <= qr: yield self.mx[ti], self.mxi[ti]
        
        tm = (tl + tr) // 2
        l_mx, l_mxi = yield self.query(ql, qr, 2*ti + 1, tl, tm)
        r_mx, r_mxi = yield self.query(ql, qr, 2*ti + 2, tm + 1, tr)
        if l_mx >= r_mx: yield l_mx, l_mxi
        yield r_mx, r_mxi

    @bootstrap
    def update(self, ql, qr, ti=0, tl=0, tr=-1):
        if tr == -1: tr = self.N - 1
        self.push(ti, tl, tr)

        if ql > tr or qr < tl: yield None
        if ql <= tl <= tr <= qr: 
            self._push(ti, tl, tr, 1)
        else:
            tm = (tl + tr) // 2
            yield self.update(ql, qr, 2*ti + 1, tl, tm)
            yield self.update(ql, qr, 2*ti + 2, tm + 1, tr)
            self._pull(ti)
        yield None


def solve():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())

    segtree = LazySegmentTreeRecursive(N)
    segtree.build(A)

    res = Q
    for _ in range(Q):
        l, r = list(map(int, input().split()))
        segtree.update(l - 1, r - 1)
        _, x = segtree.query(0, N - 1)
        res += x

    return res


def main():
    T = int(input())
    for t in range(T):
        res = solve()
        print(f'Case #{t + 1}: {res}')


if __name__ == '__main__':
    main()

