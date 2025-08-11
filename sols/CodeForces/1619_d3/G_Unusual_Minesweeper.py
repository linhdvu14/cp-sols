''' G. Unusual Minesweeper
https://codeforces.com/contest/1619/problem/G
'''

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
    def __init__(self, P):
        self.N = len(P)
        self.rank = [1]*self.N  # for root nodes, height of tree rooted at this node
        self.parent = [i for i in range(self.N)]
        self.time = [tup[-1] for tup in P]
    
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
        self.time[rj] = min(self.time[rj], self.time[ri])


from collections import deque

def solve(N, K, P):
    uf = UnionFind(P)

    # merge chained mines into a cc
    # cc time = earliest explosion time over all mines in cc
    rows, cols = {}, {}
    for i, (r, c, _) in enumerate(P):
        if r not in rows: rows[r] = []
        if c not in cols: cols[c] = []
        rows[r].append((c, i))
        cols[c].append((r, i))
    
    for points in rows.values():
        points.sort()
        for i in range(len(points)-1):
            if points[i+1][0]-points[i][0] <= K:
                uf.union(points[i+1][1], points[i][1])

    for points in cols.values():
        points.sort()
        for i in range(len(points)-1):
            if points[i+1][0]-points[i][0] <= K:
                uf.union(points[i+1][1], points[i][1])

    # inc time counter, each step detonate last cc
    par = list(set([uf.find(i) for i in range(N)]))
    times = deque(sorted([uf.time[p] for p in par]))
    
    res = 0
    while times:
        times.pop()
        while times and times[0] <= res:
            times.popleft()
        if times: res += 1

    return res


def main():
    T = int(input())
    for _ in range(T):
        _ = input()
        N, K = list(map(int, input().split()))
        P = [list(map(int, input().split())) for _ in range(N)]
        out = solve(N, K, P)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

