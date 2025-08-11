''' G. MinOr Tree
https://codeforces.com/contest/1624/problem/G
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

class UnionFind:
    def __init__(self, N):
        self.N = N
        self.rank = [1]*N  # for root nodes, height of tree rooted at this node
        self.parent = [i for i in range(N)]
        self.count = N  # num cc
    
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
        self.count -= 1

    def get_num_cc(self):
        return self.count


def solve(N, edges):
    mask = 0
    
    # build res from msb to lsb
    for i in range(32):
        # try setting i-th msb bit to 0
        mask <<= 1

        # use only edges that maintains prefix mask
        uf = UnionFind(N)
        for u, v, w in edges:
            if (w >> (31 - i)) | mask == mask:
                uf.union(u-1, v-1)
        
        # graph not connected, need to set i-th msb bit to 1
        if uf.get_num_cc() > 1:
            mask |= 1

    return mask


def main():
    T = int(input())
    for _ in range(T):
        _ = input()
        N, M = list(map(int, input().split()))
        edges = [list(map(int, input().split())) for _ in range(M)]
        out = solve(N, edges)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

