''' D. Professor Higashikata
https://codeforces.com/contest/1847/problem/D
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
import operator

class SegmentTree:
    def __init__(self, N, default, func):
        self.N = N
        self.default = default
        self.func = func
        self.offset = sz = 1 << (N - 1).bit_length()
        self.val = [default] * (2 * sz)

    def build(self, init_arr):
        self.val[self.offset : self.offset + len(init_arr)] = init_arr
        for i in reversed(range(self.offset)):
            self.val[i] = self.func(self.val[2*i], self.val[2*i + 1])

    def get(self, i):
        '''get nums[i]'''
        return self.val[i + self.offset]

    def set(self, i, x):
        '''set nums[i] = x'''
        i += self.offset
        self.val[i] = x
        i >>= 1
        while i:
            self.val[i] = self.func(self.val[2*i], self.val[2*i + 1])
            i >>= 1

    def query(self, l, r):
        '''range query l..r'''
        l += self.offset
        r += self.offset + 1
        res = self.default
        while l < r:
            if l & 1:
                res = self.func(res, self.val[l])
                l += 1
            if r & 1:
                r -= 1
                res = self.func(res, self.val[r])
            l >>= 1
            r >>= 1
        return res


def solve(N, M, Q, S, segs, queries):
    S = list(map(int, list(S)))
    segs = [(l - 1, r - 1) for l, r in segs]

    # order S[i] by first occurrence in T
    segtree = SegmentTree(N, default=INF, func=min)
    segtree.build(list(range(N)))

    pos = []
    pos_mp = [-1] * N
    for l, r in segs:
        i = segtree.query(l, r)
        while i <= r:
            pos.append(i)
            pos_mp[i] = len(pos) - 1
            segtree.set(i, INF)
            i = segtree.query(i + 1, r)

    # track swaps needed, considering only first occurrence
    T = [S[p] for p in pos]
    segtree = SegmentTree(len(T), default=0, func=operator.add)
    segtree.build(T)
    one_s, one_t = sum(S), sum(T)

    res = [0] * Q
    for qi, si in enumerate(queries):
        si -= 1
        S[si] ^= 1
        one_s += 1 if S[si] else -1

        ti = pos_mp[si]
        if ti != -1:
            T[ti] ^= 1
            one_t += 1 if T[ti] else -1
            segtree.set(ti, T[ti])

        one = min(one_s, len(T))
        if not one: res[qi] = 0
        else: res[qi] = one - segtree.query(0, one - 1)

    return res


def main():
    N, M, Q = list(map(int, input().split()))
    S = input().decode().strip()
    segs = [list(map(int, input().split())) for _ in range(M)]
    queries = [int(input()) for _ in range(Q)]
    res = solve(N, M, Q, S, segs, queries)
    print(*res, sep='\n')


if __name__ == '__main__':
    main()
