''' G. Kirill and Company
https://codeforces.com/contest/1741/problem/G
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

def solve(N, M, edges, P, pos, B, bad):
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)

    pos = [u - 1 for u in pos] 
    bad = [u - 1 for u in bad]
    mask = [0] * N
    for i, b in enumerate(bad): mask[pos[b]] |= 1 << i

    # reach[u] = all subsets of bad that lie on shortest path from node 0 to node u
    reach = [{0} for _ in range(N)]
    
    dist = [-1] * N
    dist[0] = 0
    
    queue = deque([0])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] == -1: 
                dist[v] = dist[u] + 1
                queue.append(v)
            if dist[v] == dist[u] + 1:
                for m in reach[u]: 
                    reach[v].add(m | mask[v])
    
    # find max covering of bad subsets using all F friends
    dp = {0}
    bad = set(bad)
    for i, p in enumerate(pos):
        if i in bad: continue
        dp = {m1 | m2 for m1 in dp for m2 in reach[p]}

    res = 0
    for m in dp: res = max(res, bin(m).count('1'))

    return B - res


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        edges = [list(map(int, input().split())) for _ in range(M)]
        P = int(input())
        pos = list(map(int, input().split()))
        B = int(input())
        bad = list(map(int, input().split()))
        res = solve(N, M, edges, P, pos, B, bad)
        print(res)


if __name__ == '__main__':
    main()

