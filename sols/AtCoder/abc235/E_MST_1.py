''' E - MST + 1
https://atcoder.jp/contests/abc235/tasks/abc235_e
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

from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack: return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack: break
                to = stack[-1].send(to)
        return to
    return wrappedfunc

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
    N, M, Q = list(map(int, input().split()))

    edges = []
    for _ in range(M): edges.append([-1] + list(map(int, input().split())))
    for i in range(Q): edges.append([i] + list(map(int, input().split())))
    edges.sort(key=lambda x: x[3], reverse=True)

    uf = UnionFind(N)
    res = ['No'] * Q
    while edges:
        t, u, v, _ = edges.pop()
        u -= 1; v -= 1
        if t == -1: uf.union(u, v)
        elif uf.find(u) != uf.find(v): res[t] = 'Yes'

    return res



if __name__ == '__main__':
    res = main()
    print(*res, sep='\n')

