''' D. Friendly Spiders
https://codeforces.com/contest/1775/problem/D
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
from collections import deque

def solve(N, A, src, tar):
    if src == tar: return 1, [src]
    src -= 1; tar -= 1

    M = max(A)

    lpf = list(range(M + 1))
    for i in range(2, M + 1):
        if lpf[i] == i:
            for j in range(i, M + 1, i):
                if lpf[j] == j:
                    lpf[j] = i
    
    mults = IntKeyDict()
    for i, a in enumerate(A):
        while a > 1:
            p = lpf[a]
            while a % p == 0: a //= p 
            if p not in mults: mults[p] = []
            mults[p].append(i)
    
    p2n = IntKeyDict()
    n2p = IntKeyDict()
    for i, a in enumerate(A):
        facs = []
        while a > 1:
            p = lpf[a]
            while a % p == 0: a //= p 
            if p not in p2n: p2n[p] = []
            p2n[p].append(i)
            facs.append(p)
        n2p[i] = facs

    p2n = IntKeyDict()
    n2p = IntKeyDict()
    for i, a in enumerate(A):
        facs = []
        while a > 1:
            p = lpf[a]
            while a % p == 0: a //= p 
            if p not in p2n: p2n[p] = []
            p2n[p].append(i)
            facs.append(p)
        n2p[i] = facs

    trace = [-1] * N
    dist = [INF] * N 
    dist[tar] = 1
    queue = deque([tar])
    while queue:
        u = queue.popleft()
        for p in n2p[u]:
            for v in p2n[p]:
                if dist[v] < INF: continue
                dist[v] = dist[u] + 1
                trace[v] = u
                queue.append(v)
            p2n[p].clear()
        n2p[u].clear()

    if dist[src] is INF: return -1, []

    res = []
    u = src 
    while u != -1:
        res.append(u + 1)
        u = trace[u]

    return dist[src], res


def main():
    N = int(input())
    A = list(map(int, input().split()))
    src, tar = list(map(int, input().split()))
    a, b = solve(N, A, src, tar)
    print(a)
    if b: print(*b)


if __name__ == '__main__':
    main()
