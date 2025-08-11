''' F. Timofey and Black-White Tree
https://codeforces.com/contest/1790/problem/F
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

# https://codeforces.com/blog/entry/111948?#comment-998693
def solve(N, root, ops, edges):
    root -= 1
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)
    
    @bootstrap
    def dfs(u, p=-1):
        for v in adj[u]:
            if v == p: continue
            par[v] = u 
            yield dfs(v, u)
        yield None 
    
    par = [-1] * N 
    dfs(0)

    # dist[u] = min dist from u to a black node under u's subtree
    dist = [INF] * N 

    dist[root] = 0
    while par[root] != -1: 
        dist[par[root]] = dist[root] + 1
        root = par[root]
    
    res, mn = [], INF
    for u in ops:
        u -= 1
        d = 0
        while u != -1 and d < mn:
            mn = min(mn, d + dist[u])
            dist[u] = min(dist[u], d)
            d += 1
            u = par[u]
        res.append(mn)

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, root = list(map(int, input().split()))
        ops = list(map(int, input().split()))
        edges = [list(map(int, input().split())) for _ in range(N - 1)]
        res = solve(N, root, ops, edges)
        print(*res)


if __name__ == '__main__':
    main()

