''' E. Round Dance
https://codeforces.com/contest/1833/problem/E
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
class UnionFind:
    def __init__(self, N):
        self.N = N
        self.rank = [1] * N  # for root nodes, height of tree rooted at this node; equal to num eles in component
        self.par = list(range(N))
    
    def find(self, i):
        r = i
        while self.par[r] != r: r = self.par[r]
        while self.par[i] != r: i, self.par[i] = self.par[i], r
        return r
    
    def union(self, i, j):
        ri, rj = self.find(i), self.find(j)
        if ri != rj:   
            if self.rank[ri] > self.rank[rj]: ri, rj = rj, ri
            self.par[ri] = rj
            self.rank[rj] += self.rank[ri]
        return ri != rj

    def get_groups(self):
        groups = [[] for _ in range(self.N)]
        for i in range(self.N):
            r = self.find(i)
            groups[r].append(i)
        return [g for g in groups if g]


def solve(N, A):
    deg = [0] * N 
    uf = UnionFind(N)
    seen = set()
    for i, j in enumerate(A):
        j -= 1
        if i > j: i, j = j, i 
        if (i, j) in seen: continue
        seen.add((i, j))
        deg[i] += 1
        deg[j] += 1
        uf.union(i, j)
    
    cycles = lines = 0
    groups = uf.get_groups()
    for gr in groups:
        if all(deg[u] == 2 for u in gr): cycles += 1
        else: lines += 1
    
    return cycles + (lines > 0), cycles + lines


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        res = solve(N, A)
        print(*res)


if __name__ == '__main__':
    main()

