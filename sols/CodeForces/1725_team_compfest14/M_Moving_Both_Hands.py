''' M. Moving Both Hands
https://codeforces.com/contest/1725/problem/M
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

from heapq import heappush, heappop, heapify

def main():
    N, M = list(map(int, input().split()))

    adj = [[] for _ in range(N)]
    adj_rev = [[] for _ in range(N)]
    for _ in range(M):
        u, v, w = list(map(int, input().split()))
        adj[u - 1].append((v - 1, w))
        adj_rev[v - 1].append((u - 1, w))

    dist = [INF] * N 
    dist[0] = 0

    # min dist from 0
    h = [(0, 0)]
    while h:
        d, u = heappop(h)
        if dist[u] < d: continue
        for v, w in adj[u]: 
            if dist[v] <= d + w: continue
            dist[v] = d + w 
            heappush(h, (d + w, v))
    
    # branch
    h = [(d, u) for u, d in enumerate(dist) if d < INF]
    heapify(h)
 
    while h:
        d, u = heappop(h)
        if dist[u] < d: continue
        for v, w in adj_rev[u]:
            if dist[v] <= w + d: continue
            dist[v] = w + d
            heappush(h, (d + w, v))
    
    for u in range(N):
        if dist[u] is INF: dist[u] = -1
 
    print(*dist[1:])


if __name__ == '__main__':
    main()
 