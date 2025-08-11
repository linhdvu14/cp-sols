''' D. Tree XOR
https://codeforces.com/contest/1882/problem/D
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


# A[u] ^ C[u] = A[par[u]] -> C[u] = A[u] ^ A[par[u]]
def solve(N, A, edges):
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)
    
    sz = [1] * N 
    cost = [0] * N 
    res = [-1] * N 

    @bootstrap
    def dfs1(u, p=-1):
        for v in adj[u]:
            if v == p: continue
            yield dfs1(v, u)
            sz[u] += sz[v]
            cost[u] += cost[v]
        if p != -1: cost[u] += sz[u] * (A[u] ^ A[p])
        yield None
    
    @bootstrap
    def dfs2(u, p=-1):
        if p == -1: res[u] = cost[u]
        else: res[u] = res[p] + (N - 2 * sz[u]) * (A[u] ^ A[p])
        for v in adj[u]: 
            if v == p: continue
            yield dfs2(v, u)
        yield None

    dfs1(0)
    dfs2(0)

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        edges = [list(map(int, input().split())) for _ in range(N - 1)]
        res = solve(N, A, edges)
        print(*res)


if __name__ == '__main__':
    main()

