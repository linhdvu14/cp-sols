''' E. Count Seconds
https://codeforces.com/contest/1704/problem/E
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
    def get(self, k, default=None): return super().get(k^self.rand, default)
    def keys(self): return [k^self.rand for k in super().keys()]
    def items(self): return [(k^self.rand, v) for k, v in super().items()]
    def __contains__(self, k): return super().__contains__(k^self.rand)

INF = float('inf')

# -----------------------------------------

MOD = 998244353

def solve(N, M, A, edges):
    adj = [[] for _ in range(N)]
    deg = [0] * N
    for u, v in edges:
        adj[u-1].append(v-1)
        deg[v-1] += 1
    
    # toposort
    topo = [u for u in range(N) if deg[u] == 0]
    for i in range(N):
        u = topo[i]
        for v in adj[u]:
            deg[v] -= 1
            if not deg[v]: topo.append(v)
    
    # after first N rounds, remaining non-epty nodes form a connected DAG rooted at sink node
    for t in range(N):
        if all(a == 0 for a in A): return t
        for u in topo[::-1]:
            if not A[u]: continue
            A[u] -= 1
            for v in adj[u]: A[v] += 1

    if all(a == 0 for a in A): return N

    # u can only start decreasing when its parents empty
    # dp[u] = total amount that must flow out from u until it becomes empty
    #       = amount originally at u + amount pushed down by u's parents
    #       = A[u] + SUM_{p -> u} dp[p]
    dp = A[:]
    for u in topo:
        for v in adj[u]: 
            dp[v] = (dp[v] + dp[u]) % MOD

    return (N + dp[topo[-1]]) % MOD


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        A = list(map(int, input().split()))
        edges = [list(map(int, input().split())) for _ in range(M)]
        out = solve(N, M, A, edges)
        print(out)


if __name__ == '__main__':
    main()

