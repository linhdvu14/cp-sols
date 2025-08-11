''' G - Distance Queries on a Tree
https://atcoder.jp/contests/abc294/tasks/abc294_g
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

class FenwickTreeRange:
    '''0-base sum Fenwick tree for range update, range query'''
    def __init__(self, data):
        self.N = N = len(data)
        self.val1 = [0] * (N + 1)
        self.val2 = [0] * (N + 1)
        for i in range(N): 
            self.add_range(i, i, data[i])

    def _add(self, val, i, x):
        while i <= self.N:
            val[i] += x
            i += i & -i

    def _query(self, val, i):
        s = 0
        while i > 0:
            s += val[i]
            i -= i & -i
        return s

    def add_range(self, l, r, x):
        '''add x to data[l..r]'''
        l += 1; r += 1
        self._add(self.val1, l, x)
        self._add(self.val1, r+1, -x)
        self._add(self.val2, l, x*(l-1))
        self._add(self.val2, r+1, -x*r)
    
    def query_range(self, l, r):
        '''query sum(data[l..r])'''
        r += 1
        res = self._query(self.val1, r) * r - self._query(self.val2, r)
        res -= self._query(self.val1, l) * l - self._query(self.val2, l)
        return res


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


def main():
    N = int(input())

    edges = [None] * (N - 1)
    adj = [[] for _ in range(N)]
    for i in range(N - 1):
        u, v, w = list(map(int, input().split()))
        u -= 1; v -= 1
        edges[i] = [u, v, w]
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    L = N.bit_length()
    depth = [0] * N
    dist = [0] * N 
    up = [[0] * N for _ in range(L + 1)]
    
    t = 0
    tin = [-1] * N
    tout = [-1] * N 

    @bootstrap
    def dfs(u, p=-1):
        nonlocal t
        up[0][u] = u if p == -1 else p 
        tin[u] = t; t += 1
        for v, w in adj[u]:
            if v == p: continue
            depth[v] = depth[u] + 1
            dist[v] = dist[u] + w 
            yield dfs(v, u)
        tout[u] = t
        yield None
    
    dfs(0)
    for k in range(1, L + 1):
        for u in range(N):
            up[k][u] = up[k - 1][up[k - 1][u]]
    
    def lca(u, v):
        if depth[u] < depth[v]: u, v = v, u 
        for k in range(L, -1, -1):
            if depth[up[k][u]] >= depth[v]:
                u = up[k][u]
        if u == v: return u 
        for k in range(L, -1, -1):
            if up[k][u] != up[k][v]:
                u, v = up[k][u], up[k][v]
        return up[0][u]
    
    # dist(u, v) = dist(0, u) + dist(0, v) - 2 * dist(0, lca(u, v))
    dist2 = [-1] * N 
    for u, d in enumerate(dist): dist2[tin[u]] = d
    fw = FenwickTreeRange(dist2)

    res = []
    Q = int(input())
    for _ in range(Q):
        ts = list(map(int, input().split()))
        if ts[0] == 1:
            i, w = ts[1] - 1, ts[2]
            u, v, old_w = edges[i]
            if depth[u] < depth[v]: u, v = v, u
            fw.add_range(tin[u], tout[u] - 1, w - old_w)
            edges[i][2] = w
        else:
            u, v = ts[1] - 1, ts[2] - 1
            a = lca(u, v)
            iu, iv, ia = tin[u], tin[v], tin[a]
            du, dv, da = fw.query_range(iu, iu), fw.query_range(iv, iv), fw.query_range(ia, ia)
            res.append(du + dv - 2 * da)
    
    return res





if __name__ == '__main__':
    res = main()
    print(*res, sep='\n')

