''' E. Labeling the Tree with Distances
https://codeforces.com/contest/1794/problem/E
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

import random
MOD = (1 << 64) - 5

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
    A = list(map(int, input().split()))
    adj = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = list(map(int, input().split()))
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)

    BASE = random.randrange(MOD)
    POW = [1] * (N + 1)
    for i in range(1, N + 1): POW[i] = POW[i - 1] * BASE % MOD
    
    s = sum(POW[a] for a in A) % MOD
    OK = set((s + POW[i]) % MOD for i in range(N))

    # dn[u] = hash of u's subtree
    par = [-1] * N
    dn = [0] * N

    @bootstrap
    def dfs1(u):
        s = 0
        for v in adj[u]:
            if v == par[u]: continue 
            par[v] = u
            s += yield dfs1(v)
        dn[u] = (1 + s * BASE) % MOD 
        yield dn[u]
    
    dfs1(0)

    # up[u] = hash if root at par[u], excluding u's subtree
    up = [0] * N
    res = []

    @bootstrap
    def dfs2(u):
        up[u] = (dn[par[u]] - dn[u] * BASE + up[par[u]] * BASE) % MOD
        if (up[u] * BASE + dn[u]) % MOD in OK: res.append(u + 1)
        for v in adj[u]:
            if v == par[u]: continue
            yield dfs2(v)
        yield None

    if dn[0] in OK: res.append(1)
    for u in adj[0]: dfs2(u)

    res.sort()
    print(len(res))
    if res: print(*res)



if __name__ == '__main__':
    main()

