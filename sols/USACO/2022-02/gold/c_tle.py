'''  Problem 3. Moo Network 
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
        if ri == rj: return False
        # rank compression: merge small tree to large tree
        if self.rank[ri] > self.rank[rj]: ri, rj = rj, ri
        self.parent[ri] = rj
        self.rank[rj] += self.rank[ri]
        return True


def main():
    N = int(input())

    rows = [[] for _ in range(11)]
    for i in range(N):
        x, y = map(int, input().split())
        rows[y].append((x, i))
    for i in range(11): rows[i].sort()

    # connect each point to nearest point on each row
    edges = []
    for y1, row1 in enumerate(rows):
        if not row1: continue
        for k in range(1, len(row1)):
            edges.append(((row1[k][0]-row1[k-1][0])*(row1[k][0]-row1[k-1][0]), row1[k][1], row1[k-1][1]))

        for y2, row2 in enumerate(rows):
            if y1 == y2 or not row2: continue

            k = 0
            for x1, i1 in row1:
                while k+1 < len(row2) and row2[k+1][0] <= x1: k += 1
                if k < len(row2) and row2[k][0] <= x1:
                    edges.append(((x1-row2[k][0])*(x1-row2[k][0]) + (y1-y2)*(y1-y2), i1, row2[k][1]))
            
            k = len(row2) - 1
            for x1, i1 in row1[::-1]:
                while k-1 >= 0 and row2[k-1][0] >= x1: k -= 1
                if k >= 0 and row2[k][0] >= x1:
                    edges.append(((x1-row2[k][0])*(x1-row2[k][0]) + (y1-y2)*(y1-y2), i1, row2[k][1]))

    edges = list(set((d, i, j) if i < j else (d, j, i) for d, i, j in edges))
    edges.sort()

    # kruskal
    res = cnt = 0
    uf = UnionFind(N)
    for d, i, j in edges:
        if not uf.union(i, j): continue
        res += d
        cnt += 1
        if cnt == N - 1: break
    
    print(res)



if __name__ == '__main__':
    main()

