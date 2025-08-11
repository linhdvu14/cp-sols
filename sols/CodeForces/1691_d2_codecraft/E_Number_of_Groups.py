''' E. Number of Groups
https://codeforces.com/contest/1691/problem/E
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


# when add a seg, merge with all remaining segs of other colors
# clear all segs of other colors except rightmost reaching one
# each line is connected to its cc only once

def solve(N, segs):
    endpoints = []
    for i, (_, l, r) in enumerate(segs):
        endpoints.append((r + 1, 0, i))
        endpoints.append((l, 1, i))
    endpoints.sort()

    uf = UnionFind(N)
    cur = [set(), set()]
    for _, is_start, i in endpoints:
        c = segs[i][0]
        if not is_start: 
            cur[c].discard(i)
        else:
            cur[c].add(i)
            mxi = mxr = -1
            for j in cur[1-c]:
                uf.union(i, j)
                if segs[j][2] > mxr: mxi, mxr = j, segs[j][2]
            cur[1-c].clear()
            if mxi != -1: cur[1-c].add(mxi)

    return uf.get_num_cc()


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        segs = [list(map(int, input().split())) for _ in range(N)]
        out = solve(N, segs)
        print(out)


if __name__ == '__main__':
    main()

