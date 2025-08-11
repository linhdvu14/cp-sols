''' E. Make It Connected
https://codeforces.com/contest/1761/problem/E
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
        self.sz = [1] * N  # for root nodes, height of tree rooted at this node; equal to num eles in component
        self.par = list(range(N))
    
    def find(self, i):  # with path compression
        r = i
        while self.par[r] != r: r = self.par[r]
        while self.par[i] != r: i, self.par[i] = self.par[i], r
        return r
    
    def union(self, i, j):  # with sz compression
        ri, rj = self.find(i), self.find(j)
        if ri != rj:   
            if self.sz[ri] > self.sz[rj]: ri, rj = rj, ri
            self.par[ri] = rj
            self.sz[rj] += self.sz[ri]
        return ri != rj

# https://codeforces.com/blog/entry/109256?#comment-974716
def solve():
    N = int(input())
    uf = UnionFind(N)
    deg = [0] * N

    for i in range(N):
        S = input().decode().strip()
        for j in range(i):
            if S[j] == '1':
                deg[i] += 1
                deg[j] += 1
                uf.union(i, j)
    
    cc_mp = [uf.find(i) for i in range(N)]
    if len(set(cc_mp)) == 1: return []

    clique = -1
    for i, c in enumerate(cc_mp):
        # isolated node
        if deg[i] == 0: return [i]

        # non-clique, perform ops once on min-deg node
        if deg[i] < uf.sz[c] - 1: return [min((deg[i], i) for i, cc in enumerate(cc_mp) if cc == c)[1]]

        # keep smallest clique
        if clique == -1 or uf.sz[clique] > uf.sz[c]: clique = c

    # > 2 cliques, perform 1 ops each per 2 different cliques
    if len(set(cc_mp)) > 2:
        res = []
        for i, c in enumerate(cc_mp):
            if not res or c != cc_mp[res[-1]]: res.append(i)
            if len(res) == 2: break 
        return res

    # 2 cliques, reduce smaller clique
    return [i for i, c in enumerate(cc_mp) if c == clique]



def main():
    T = int(input())
    for _ in range(T):
        res = solve()
        print(len(res))
        if res: print(*[i + 1 for i in res])


if __name__ == '__main__':
    main()

