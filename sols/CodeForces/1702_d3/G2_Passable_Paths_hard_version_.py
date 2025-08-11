''' G2. Passable Paths (hard version)
https://codeforces.com/contest/1702/problem/G2
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

# for int dict key
from random import randrange
RAND = randrange(1 << 62)
def conv(x): return x ^ RAND

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


def main():
    N = int(input())
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = list(map(int, input().split()))
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)

    @bootstrap
    def dfs(u, p=-1):
        nonlocal timer
        tin[u] = timer = timer + 1
        up[u][0] = p if p != -1 else u
        for k in range(1, L+1):
            up[u][k] = up[up[u][k-1]][k-1]  # go up 2^(k-1) twice from u
        for v in adj[u]:
            if v == p: continue
            depth[v] = depth[u] + 1
            yield dfs(v, u)
        tout[u] = timer = timer + 1
        yield None

    L = N.bit_length()
    tin, tout, depth = [0]*N, [0]*N, [0]*N
    up = [[0]*(L+1) for _ in range(N)]
    timer = 0
    dfs(0)
    
    def is_ancestor(anc, desc): return tin[anc] <= tin[desc] and tout[anc] >= tout[desc]
    
    def lca(u, v):
        if is_ancestor(u, v): return u
        if is_ancestor(v, u): return v
        for k in range(L, -1, -1):
            if not is_ancestor(up[u][k], v):
                u = up[u][k]
        return up[u][0]

    def is_ok(S):
        if len(S) < 3: return True
        S = [u-1 for u in S]
        S.sort(key=lambda u: depth[u])

        # S must partition into 1 or 2 line trees
        s1, s2 = [], []
        for u in S:
            if not s1 or is_ancestor(s1[-1], u): s1.append(u)
            elif not s2 or is_ancestor(s2[-1], u): s2.append(u)
            else: return False
        
        if not s2 or len(s1) == 1: return True
        l = lca(s1[1], s2[0])
        if l != s1[0] and is_ancestor(s1[0], l): return False
        return True
    
    Q = int(input())
    res = ['NO'] * Q
    for i in range(Q):
        _ = int(input())
        S = list(map(int, input().split()))
        if is_ok(S): res[i] = 'YES'
        
    print(*res, sep='\n')



if __name__ == '__main__':
    main()

