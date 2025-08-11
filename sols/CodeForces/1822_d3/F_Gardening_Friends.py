''' F. Gardening Friends
https://codeforces.com/contest/1822/problem/F
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


def solve(N, K, C, edges):
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1) 

    @bootstrap
    def dfs1(u, p=-1):
        if p != -1: depth[u] = depth[p] + 1
        h = 0
        for v in adj[u]:
            if v == p: continue
            h = max(h, (yield dfs1(v, u)) + 1)
        height[u] = h 
        yield h 
    
    depth = [0] * N 
    height = [0] * N
    dfs1(0)

    @bootstrap
    def dfs2(u, p=-1, up=0):
        nonlocal res 
        res = max(res, max(up, height[u]) * K - depth[u] * C)
        cands = sorted([(height[v] + 1, v) for v in adj[u] if v != p], reverse=True) + [(0, -1)]
        for v in adj[u]:
            if v == p: continue
            if v != cands[0][1]: yield dfs2(v, u, max(up, cands[0][0]) + 1)
            else: yield dfs2(v, u, max(up, cands[1][0]) + 1)
        yield None

    res = height[0] * K
    dfs2(0)

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, K, C = list(map(int, input().split()))
        edges = [list(map(int, input().split())) for _ in range(N - 1)]
        res = solve(N, K, C, edges)
        print(res)


if __name__ == '__main__':
    main()
