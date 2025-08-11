''' H. Hospital Queue
https://codeforces.com/contest/1765/problem/H 
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

def solve(N, M, P, edges, n):
    deg = [0] * N
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[v - 1].append(u - 1)
        deg[u - 1] += 1
    
    h = [(-P[u], u) for u in range(N) if deg[u] == 0]
    heapify(h)

    res, pos = -1, N
    while h:
        p, u = heappop(h)
        if u == n: 
            res = pos
            continue
        if res != -1 and -p < pos: break
        for v in adj[u]:
            deg[v] -= 1
            if deg[v] == 0: heappush(h, (-P[v], v))
        pos -= 1
        res = pos

    return res


def main():
    N, M = list(map(int, input().split()))
    P = list(map(int, input().split()))
    edges = [list(map(int, input().split())) for _ in range(M)]
    res = [solve(N, M, P, edges, n) for n in range(N)]
    print(*res)


if __name__ == '__main__':
    main()

