''' E - Max Min 
https://atcoder.jp/contests/abc247/tasks/abc247_e
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

MOD = 998244353

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
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))

    # find cycles in bipartite graph
    # left:  0..N-1  -> cards
    # right: N..2N-1 -> numbers
    uf = UnionFind(2*N)
    for i, (p, q) in enumerate(zip(P, Q)):
        p += N - 1
        q += N - 1
        uf.union(i, p)
        uf.union(i, q)

    # num nodes in each cycle
    sizes = [len(g)//2 for g in uf.get_cc()]

    # node = card, edge = connect 2 cards that share a number
    # count num ways to select nodes s.t. each edge has at least 1 endpoint chosen
    res = 1
    for n in sizes:
        # dp[0][u] = num valid ways to choose for line 0..u, with node u not chosen
        # dp[1][u] = num valid ways to choose for line 0..u, with node u chosen
        ways = 0

        # choose node 0, then node n-1 can be chosen or not chosen
        dp = [[0]*n for _ in range(2)]
        dp[1][0] = 1
        for u in range(1, n):
            dp[0][u] = dp[1][u-1]
            dp[1][u] = (dp[0][u-1] + dp[1][u-1]) % MOD
        ways += dp[0][n-1] + dp[1][n-1]

        # do not choose node 0, then node n-1 must be chosen
        dp = [[0]*n for _ in range(2)]
        dp[0][0] = 1
        for u in range(1, n):
            dp[0][u] = dp[1][u-1]
            dp[1][u] = (dp[0][u-1] + dp[1][u-1]) % MOD
        ways += dp[1][n-1]

        res = (res * ways) % MOD

    print(res)


if __name__ == '__main__':
    main()

