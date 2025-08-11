''' D - Circumferences
https://atcoder.jp/contests/abc259/tasks/abc259_d
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
        self.rank = [1]*N  # for root nodes, height of tree rooted at this node
        self.par = list(range(N))
        self.count = N  # num cc
    
    def find(self, i):  # with path compression
        r = i
        while self.par[r] != r: r = self.par[r]
        while self.par[i] != r: i, self.par[i] = self.par[i], r
        return r

    def union(self, i, j):  # with rank compression
        ri, rj = self.find(i), self.find(j)
        if ri == rj: return
        if self.rank[ri] > self.rank[rj]: ri, rj = rj, ri
        self.par[ri] = rj
        self.rank[rj] += self.rank[ri]
        self.count -= 1


def main():
    N = int(input())
    xs, ys, xt, yt = list(map(int, input().split()))
    circles = [list(map(int, input().split())) for _ in range(N)]
    
    s = t = -1
    uf = UnionFind(N)
    for i in range(N):
        x1, y1, r1 = circles[i]
        if s == -1 and (xs - x1)**2 + (ys - y1)**2 == r1**2: s = i
        if t == -1 and (xt - x1)**2 + (yt - y1)**2 == r1**2: t = i
        for j in range(i):
            x2, y2, r2 = circles[j]
            if (x1, y1) != (x2, y2) and (r1 - r2)**2 <= (x1 - x2)**2 + (y1 - y2)**2 <= (r1 + r2)**2:
                uf.union(i, j)
    
    return uf.find(s) == uf.find(t)



if __name__ == '__main__':
    out = main()
    print('Yes' if out else 'No')

