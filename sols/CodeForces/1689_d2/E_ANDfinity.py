''' E. ANDfinity
https://codeforces.com/contest/1689/problem/E
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

    def get_num_cc(self):
        return self.count

BITS = 30

def solve(N, A):
    # increment any 0
    res = 0
    for i, a in enumerate(A):
        if a > 0: continue
        A[i] = 1
        res += 1

    # connect all bits in a single ele
    def is_connected(A):
        if any(a == 0 for a in A): return False
        bits = set(i for i in range(BITS) if any((a >> i) & 1 for a in A))
        bits = {b: i for i, b in enumerate(sorted(list(bits)))}
        uf = UnionFind(len(bits))
        for a in A:
            pi = -1
            for i in range(BITS):
                if (a >> i) & 1:
                    if pi != -1: uf.union(bits[i], bits[pi])
                    pi = i
        return uf.get_num_cc() == 1
    
    # check if alr connected
    if is_connected(A): return res, A 

    # check if can connect with 1 op
    for i, a in enumerate(A):
        A[i] = a - 1
        if is_connected(A): return res + 1, A 
        A[i] = a + 1
        if is_connected(A): return res + 1, A 
        A[i] = a

    # find all eles with max lsb
    mx, idx = -1, []
    for i, a in enumerate(A):
        lsb = a & (-a)
        if lsb > mx: mx, idx = lsb, []
        if lsb == mx: idx.append(i)
    
    A[idx[0]] -= 1
    if len(idx) == 1: return res + 1, A 
    A[idx[1]] += 1  # connect to idx[0]
    return res + 2, A


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        r1, r2 = solve(N, A)
        print(r1)
        print(*r2)


if __name__ == '__main__':
    main()

