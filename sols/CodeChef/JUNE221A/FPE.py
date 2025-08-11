''' Full Path Eraser
https://www.codechef.com/JUNE221A/problems/FPE
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


from math import gcd

def solve(N, A, edges):
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    
    # gcd of subtree
    @bootstrap
    def dfs1(u, p=-1):
        g = A[u]
        for v in adj[u]:
            if v == p: continue
            g = gcd(g, (yield dfs1(v, u)))
        G[u] = g
        yield g

    G = [0] * N
    dfs1(0)

    # max beauty of subtree
    # either take entire subtree or slice off root and recurse down one child
    @bootstrap
    def dfs2(u, p=-1):
        mx = G[u]
        total = sum(G[v] for v in adj[u] if v != p)
        for v in adj[u]:
            if v == p: continue
            cand = (total - G[v]) + (yield dfs2(v, u))
            mx = max(mx, cand)
        yield mx

    return dfs2(0)
    

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        edges = [list(map(int, input().split())) for _ in range(N-1)]
        out = solve(N, A, edges)
        print(out)


if __name__ == '__main__':
    main()
