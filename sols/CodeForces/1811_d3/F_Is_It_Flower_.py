''' F. Is It Flower?
https://codeforces.com/contest/1811/problem/F
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
    
    def size(self, i):
        return self.rank[self.find(i)]


def solve(N, M, edges):
    edges = [[u - 1, v - 1] for u, v in edges]

    k = -1
    sq = int(N**0.5)
    for s in range(sq - 1, sq + 2):
        if s * s == N:
            k = s 
            break
    if k < 3: return 'NO'

    deg = [0] * N
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
    
    cnt2 = cnt4 = 0
    for u in range(N):
        if deg[u] == 2: cnt2 += 1
        elif deg[u] == 4: cnt4 += 1
    if cnt4 != k or cnt2 + cnt4 != N: return 'NO'

    uf2 = UnionFind(N)
    uf4 = UnionFind(N)
    for u, v in edges:
        if deg[u] == deg[v] == 2: uf2.union(u, v)
        elif deg[u] == deg[v] == 4: uf4.union(u, v)
    
    for u in range(N):
        if deg[u] == 2 and uf2.size(u) != k - 1: return 'NO'
        if deg[u] == 4 and uf4.size(u) != k: return 'NO'
    
    for u, v in edges:
        if deg[u] != deg[v]:
            uf2.union(u, v)
    
    for u in range(N):
        if deg[u] == 2 and uf2.size(u) != k: return 'NO'

    return 'YES'



def main():
    T = int(input())
    for _ in range(T):
        _ = input()
        N, M = list(map(int, input().split()))
        edges = [list(map(int, input().split())) for _ in range(M)]
        res = solve(N, M, edges)
        print(res)


if __name__ == '__main__':
    main()

