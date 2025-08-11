''' C. Infected Tree
https://codeforces.com/contest/1689/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') not in [None, '0']

if DEBUG:
    from inspect import currentframe, getframeinfo
    from re import search

def debug(*args):
    if not DEBUG: return
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


def solve_1(N, edges):
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    
    # subtree size
    @bootstrap
    def dfs1(u, p=-1):
        sz[u] = 1
        for v in adj[u]:
            if v == p: continue
            yield dfs1(v, u)
            sz[u] += sz[v]
        yield None

    sz = [0] * N
    dfs1(0)

    # if this node is infected, how many subtree nodes can be saved
    @bootstrap
    def dfs2(u, p=-1):
        child = [v for v in adj[u] if v != p]
        if not child: yield 0
        if len(child) == 1: yield sz[child[0]] - 1
        v1, v2 = child
        yield max(
            sz[v1] - 1 + (yield dfs2(v2, u)),
            sz[v2] - 1 + (yield dfs2(v1, u)),
        )

    return dfs2(0)


# count number of lost nodes
# each level except root loses 2 nodes (1 deleted + 1 infected)
# infection spreads till reach node with < 2 children

def solve_2(N, edges):
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    
    @bootstrap
    def dfs(u, p=-1):
        nonlocal res
        deg = 0
        for v in adj[u]:
            if v == p: continue
            depth[v] = depth[u] + 1
            yield dfs(v, u)
            deg += 1
        # lose root, 2 nodes per level till now, num children of current node
        if deg < 2: res = max(res, N - 1 - 2 * depth[u] - deg)
        yield None
        
    depth = [0] * N
    res = 0
    dfs(0)
    return res


solve = solve_2

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        edges = [list(map(int, input().split())) for _ in range(N-1)]
        out = solve(N, edges)
        print(out)


if __name__ == '__main__':
    main()

