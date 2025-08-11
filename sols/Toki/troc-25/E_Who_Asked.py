''' E. Who Asked?
https://tlx.toki.id/contests/troc-25/problems/E
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

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

class FenwickTreeRange:
    '''1-base sum Fenwick tree for range update, range query'''
    def __init__(self, data):
        '''transform list into BIT'''
        self.N = N = len(data)
        self.val1 = [0] * (N + 1)
        self.val2 = [0] * (N + 1)
        for i in range(N): 
            self.add_range(i, i, data[i])

    def _add(self, val, i, x):
        while i <= self.N:
            val[i] = (val[i] + x) % MOD
            i += i & -i

    def _query(self, val, i):
        s = 0
        while i > 0:
            s = (s + val[i]) % MOD
            i -= i & -i
        return s

    def add_range(self, l, r, x):
        '''add x to data[l..r]'''
        l += 1; r += 1
        self._add(self.val1, l, x)
        self._add(self.val1, r+1, -x)
        self._add(self.val2, l, x*(l-1))
        self._add(self.val2, r+1, -x*r)
    
    def query_range(self, l, r):
        '''query sum(data[l..r])'''
        r += 1
        res = self._query(self.val1, r) * r - self._query(self.val2, r)
        res -= self._query(self.val1, l) * l - self._query(self.val2, l)
        return res % MOD


from collections import deque

def main():
    N = int(input())
    A = list(map(int, input().split()))

    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)

    # root tree at 0
    # track children's start and stop idx in level-order traversal
    par, left, right = [-1] * N, [-1] * N, [-1] * N
    order = [0]
    queue = deque([0])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if v == 0 or par[v] != -1: continue
            par[v] = u
            order.append(v)
            queue.append(v)
            if left[u] == -1: left[u] = v
            right[u] = v

    # node -> idx in order
    idx = [-1] * N
    for i, u in enumerate(order): idx[u] = i

    # fw tree on level order
    A = [A[u] for u in order]
    fw = FenwickTreeRange(A)
    
    # for each query, separately update par and children range
    res = []
    Q = int(input())
    for _ in range(Q):
        t, u = map(int, input().split())
        u -= 1
        l, r, p = left[u], right[u], par[u]
        if t == 1:
            v = fw.query_range(idx[u], idx[u])
            if l != -1: fw.add_range(idx[l], idx[r], v)
            if p != -1: fw.add_range(idx[p], idx[p], v)
        else:
            s = 0
            if l != -1: s += fw.query_range(idx[l], idx[r])
            if p != -1: s += fw.query_range(idx[p], idx[p])
            res.append(s % MOD)
    
    print(*res, sep='\n')


if __name__ == '__main__':
    main()