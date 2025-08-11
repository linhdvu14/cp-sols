''' E. Qpwoeirut and Vertices
https://codeforces.com/contest/1706/problem/E
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
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


class IntKeyDict(dict):
    from random import randrange
    rand = randrange(1 << 62)
    def __setitem__(self, k, v): super().__setitem__(k^self.rand, v)
    def __getitem__(self, k): return super().__getitem__(k^self.rand)
    def get(self, k, default=None): return super().get(k^self.rand, default)
    def keys(self): return [k^self.rand for k in super().keys()]
    def items(self): return [(k^self.rand, v) for k, v in super().items()]


INF = float('inf')

# -----------------------------------------

class UnionFind:
    def __init__(self, N):
        self.par = list(range(N))
        self.rank = [0] * N
    
    def find(self, u):
        r = u
        while self.par[r] != r: r = self.par[r]
        while u != r: u, self.par[u] = self.par[u], r
        return r 
    
    def union(self, u, v):
        ru, rv = self.find(u), self.find(v)
        if self.rank[ru] > self.rank[rv]: ru, rv = rv, ru
        self.par[ru] = rv
        self.rank[rv] += self.rank[ru]


class SparseTable:
    def __init__(self, data, func=min):
        self.func = func
        self.data = [list(data)]
        i, n = 1, len(data)
        while 2 * i <= n:
            prev = self.data[-1]
            nxt = [func(prev[j], prev[j + i]) for j in range(n - 2*i + 1)]
            self.data.append(nxt)
            i <<= 1
    
    def query(self, l, r):
        d = (r - l + 1).bit_length() - 1
        return self.func(self.data[d][l], self.data[d][r - (1 << d) + 1])


def solve(N, M, Q, edges, queries):
    # find mst where weight = edge number
    # then first time (u, v) is connected = max cost on path u..v in mst
    edges = [(i+1, u-1, v-1) for i, (u, v) in enumerate(edges)]
    uf = UnionFind(N)
    adj = [[] for _ in range(N)]

    for w, u, v in edges:
        if uf.find(u) == uf.find(v): continue
        uf.union(u, v)
        adj[u].append((v, w))
        adj[v].append((u, w))

    # upa[k][u] = 2^k ancestor of u
    # upw[k][u] = max edge weight on path u..upa[k][u]
    L = N.bit_length()
    depth = [0] * N
    upa = [[0] * N for _ in range(L+1)]
    upw = [[0] * N for _ in range(L+1)]

    @bootstrap
    def dfs(u, p=-1, d=0):
        depth[u] = d
        for v, w in adj[u]:
            if v == p: continue
            upa[0][v] = u
            upw[0][v] = w
            yield dfs(v, u, d+1)
        yield None

    dfs(0)
    for k in range(1, L+1):
        for u in range(N):
            upa[k][u] = upa[k-1][upa[k-1][u]]
            upw[k][u] = max(upw[k][u], upw[k-1][u], upw[k-1][upa[k-1][u]])
    
    # get max edge weight on path u..v on mst tree
    def f(u, v):
        res = 0
        if depth[u] < depth[v]: u, v = v, u
        for k in range(L, -1, -1):
            if depth[upa[k][u]] >= depth[v]:
                res = max(res, upw[k][u])
                u = upa[k][u]
        if u == v: return res
        for k in range(L, -1, -1):
            if upa[k][u] != upa[k][v]:
                res = max(res, upw[k][u], upw[k][v])
                u, v = upa[k][u], upa[k][v]
        return max(res, upw[0][u], upw[0][v])
    
    # rmq over f(i, i+1)
    A = [f(i, i+1) for i in range(N-1)]
    st = SparseTable(A, func=max)

    res = [0] * Q
    for i, (l, r) in enumerate(queries):
        if l == r: continue
        res[i] = st.query(l-1, r-2)
    
    return res


def main():
    T = int(input())
    for _ in range(T):
        N, M, Q = list(map(int, input().split()))
        edges = [list(map(int, input().split())) for _ in range(M)]
        queries = [list(map(int, input().split())) for _ in range(Q)]
        out = solve(N, M, Q, edges, queries)
        print(*out)


if __name__ == '__main__':
    main()

