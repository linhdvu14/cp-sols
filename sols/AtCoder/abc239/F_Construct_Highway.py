''' F - Construct Highway
https://atcoder.jp/contests/abc239/tasks/abc239_f
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

class UnionFind:
    def __init__(self, N):
        self.N = N
        self.rank = [1]*N  # for root nodes, height of tree rooted at this node
        self.parent = list(range(N))
        self.count = N  # num cc
    
    def find(self, i):  
        r = i
        while self.parent[r] != r: r = self.parent[r]	
        # path compression: connect all parents from i..r to r	
        while self.parent[i] != r:
            p = self.parent[i]
            self.parent[i] = r
            i = p
        return r

    def union(self, i, j): 
        ri, rj = self.find(i), self.find(j)
        if ri == rj: return
        # rank compression: merge small tree to large tree
        if self.rank[ri] > self.rank[rj]: ri, rj = rj, ri
        self.parent[ri] = rj
        self.rank[rj] += self.rank[ri]
        self.count -= 1
    
    def get_cc(self):
        groups = [[] for _ in range(self.N)]
        for i in range(self.N):
            r = self.find(i)
            groups[r].append(i)
        return [g for g in groups if g]


def main():
    N, M = list(map(int, input().split()))
    D = list(map(int, input().split()))
    uf = UnionFind(N)
    for _ in range(M):
        u, v = list(map(int, input().split()))
        uf.union(u-1, v-1)
        D[u-1] -= 1
        D[v-1] -= 1
    
    if sum(D) != 2 * (N - M - 1): return [[-1]]

    ones, twos = [], []
    for g in uf.get_cc():
        ng = []
        for u in g: ng += [u] * D[u]
        if len(ng) == 1: ones.append(ng)
        elif len(ng) > 1: twos.append(ng)
        else: return [[-1]]

    res = []
    while ones and twos:
        o = ones.pop()
        t = twos.pop()
        x, y = o[0], t.pop()
        res.append((x+1, y+1))
        if len(t) == 1: ones.append(t)
        else: twos.append(t)

    if not (len(ones) == 2 and len(twos) == 0): return [[-1]]
    x, y = ones[0][0], ones[-1][0]
    res.append((x+1, y+1))

    return res
    



if __name__ == '__main__':
    out = main()
    for tup in out: print(*tup)


