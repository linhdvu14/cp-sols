''' E. Split Into Two Sets
https://codeforces.com/contest/1702/problem/E
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

# for int dict key
from random import randrange
RAND = randrange(1 << 62)
def conv(x): return x ^ RAND

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


def solve(N, dominos):
    cnt = {}
    for a, b in dominos:
        if a == b: return 'NO'
        cnt[a] = cnt.get(a, 0) + 1
        cnt[b] = cnt.get(b, 0) + 1
    
    if any(v > 2 for v in cnt.values()): return 'NO'

    uf = UnionFind(N + 1)
    for a, b in dominos:
        uf.union(a, b)

    # check for odd length cycles
    groups = uf.get_cc()
    for g in groups:
        if len(g) >= 2 and len(g) % 2: 
            return 'NO'

    return 'YES'


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        dominos = [list(map(int, input().split())) for _ in range(N)]
        out = solve(N, dominos)
        print(out)


if __name__ == '__main__':
    main()

