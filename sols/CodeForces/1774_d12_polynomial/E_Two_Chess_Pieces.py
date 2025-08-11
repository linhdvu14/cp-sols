''' E. Two Chess Pieces
https://codeforces.com/contest/1774/problem/E
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

class IntKeyDict(dict):
    from random import randrange
    rand = randrange(1 << 62)
    def __setitem__(self, k, v): super().__setitem__(k^self.rand, v)
    def __getitem__(self, k): return super().__getitem__(k^self.rand)
    def __contains__(self, k): return super().__contains__(k^self.rand)
    def __repr__(self): return str({k: v for k, v in self.items()})
    def get(self, k, default=None): return super().get(k^self.rand, default)
    def keys(self): return [k^self.rand for k in super().keys()]
    def items(self): return [(k^self.rand, v) for k, v in super().items()]

INF = float('inf')

# -----------------------------------------

def main():
    N, D = list(map(int, input().split()))

    adj = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = list(map(int, input().split()))
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)

    A = set(u - 1 for u in list(map(int, input().split()))[1:])
    B = set(u - 1 for u in list(map(int, input().split()))[1:])

    # if A visits u, B should visit u's D-th ancestor
    # returns max depth over all nodes in A under u's subtree
    @bootstrap
    def dfs1(u, A, B_extra, p=-1, d=0):
        mxd = -INF
        for v in adj[u]:
            if v == p: continue
            mxd = max(mxd, (yield dfs1(v, A, B_extra, u, d + 1)))
        if mxd - d == D: B_extra.add(u)
        if u in A: mxd = max(mxd, d)
        yield mxd
    
    A_extra, B_extra = set([0]), set([0])
    dfs1(0, A, B_extra)
    dfs1(0, B, A_extra)

    # returns: min cost to visit all nodes in A under p's subtree (0 if no such nodes)
    @bootstrap
    def dfs2(u, A, p=-1):
        res = 0
        for v in adj[u]:
            if v == p: continue
            res += yield dfs2(v, A, u)
        yield res + 2 if res or u in A else 0
    
    r1 = dfs2(0, A | A_extra) - 2
    r2 = dfs2(0, B | B_extra) - 2
    print(r1 + r2)




if __name__ == '__main__':
    main()

