''' Problem 2. Connecting Two Barns '''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

if DEBUG:
    from varname.core import argname
    from inspect import currentframe

def debug(var, *more_vars):
    if not DEBUG: return
    var_names = argname('var', '*more_vars', func=debug)
    values = (var, *more_vars)
    name_and_values = [f'{var_name}={value}'  for var_name, value in zip(var_names, values)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(name_and_values)}')


INF = float('inf')

# -----------------------------------------

class UnionFind:
    def __init__(self, N):
        self.N = N
        self.rank = [1]*N  # for root nodes, height of tree rooted at this node
        self.parent = [i for i in range(N)]
    
    def find(self, i):  
        r = i
        while self.parent[r] != r:
            r = self.parent[r]	
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


def solve(N, M, edges):
    uf = UnionFind(N)
    for u, v in edges:
        uf.union(u-1, v-1)

    ra, rb = uf.find(0), uf.find(N-1)
    if ra==rb: return 0
    
    # min cost to connect each rc to ra and rb
    groups = [uf.find(i) for i in range(N)]
    cost_A, cost_B = {}, {}

    last_A = last_B = -1
    for i in range(N):
        rc = groups[i]
        if rc == ra: last_A = i
        if rc == rb: last_B = i
        if last_A != -1: cost_A[rc] = min(cost_A.get(rc, INF), (i - last_A)**2)
        if last_B != -1: cost_B[rc] = min(cost_B.get(rc, INF), (i - last_B)**2)
    
    last_A = last_B = -1
    for i in range(N-1, -1, -1):
        rc = groups[i]
        if rc == ra: last_A = i
        if rc == rb: last_B = i
        if last_A != -1: cost_A[rc] = min(cost_A.get(rc, INF), (i - last_A)**2)
        if last_B != -1: cost_B[rc] = min(cost_B.get(rc, INF), (i - last_B)**2)
    
    res = INF
    for rc, ca in cost_A.items():
        res = min(res, ca + cost_B.get(rc, INF))
    return res


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        edges = [list(map(int, input().split())) for _ in range(M)]
        out = solve(N, M, edges)
        output(f'{out}\n')



if __name__ == '__main__':
    main()

