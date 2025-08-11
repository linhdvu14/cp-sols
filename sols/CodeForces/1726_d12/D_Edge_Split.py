''' D. Edge Split
https://codeforces.com/contest/1726/problem/D
'''

from ctypes import Union
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
    def __contains__(self, k): return super().__contains__(k^self.rand)
    def __repr__(self): return str({k: v for k, v in self.items()})
    def get(self, k, default=None): return super().get(k^self.rand, default)
    def keys(self): return [k^self.rand for k in super().keys()]
    def items(self): return [(k^self.rand, v) for k, v in super().items()]

INF = float('inf')

# -----------------------------------------

class UnionFind:
    def __init__(self, N):
        self.N = N
        self.rank = [1] * N  # for root nodes, height of tree rooted at this node
        self.par = list(range(N))
    
    def find(self, i):  # with path compression
        r = i
        while self.par[r] != r: r = self.par[r]
        while self.par[i] != r: i, self.par[i] = self.par[i], r
        return r
    
    def union(self, i, j):  # with rank compression
        ri, rj = self.find(i), self.find(j)
        if ri != rj:   
            if self.rank[ri] > self.rank[rj]: ri, rj = rj, ri
            self.par[ri] = rj
            self.rank[rj] += self.rank[ri]
        return ri != rj


# in best case, coloring edge (u, v) reduces c1 + c2 by 1 (using any color), when u and v are not alr connected in graph of chosen color
# if M < N + 2, color R spanning tree (N - 1 edges) and B for remaining edges; at most 2 B edges so always connect disjoint components
# if M = N + 2, color R spanning tree and 3 B edges s.t. B do not form triangle

def solve(N, M, edges):
    edges = [(u-1, v-1) for u, v in edges]

    # create R spanning tree
    res = [0] * M
    uf = UnionFind(N)
    for i, (u, v) in enumerate(edges):
        if not uf.union(u, v):
            res[i] = 1

    rem = [i for i in range(M) if res[i] == 1]
    if len(rem) < 3 or len(set(u for i in rem for u in edges[i])) != 3: return res

    # rehook in case of B triangle
    res = [0] * M
    res[rem[0]] = res[rem[1]] = 1
    uf = UnionFind(N)
    uf.union(*edges[rem[2]])

    for i, (u, v) in enumerate(edges):
        if i in rem: continue
        if not uf.union(u, v):
            res[i] = 1

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        edges = [list(map(int, input().split())) for _ in range(M)]
        res = solve(N, M, edges)
        print(*res, sep='')


if __name__ == '__main__':
    main()

