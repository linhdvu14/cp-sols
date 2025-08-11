''' G. Ksyusha and Chinchilla
https://codeforces.com/contest/1833/problem/G
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


def solve(N, edges):
    if N % 3: return -1, []

    adj = [[] for _ in range(N)]
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)
        
    @bootstrap
    def dfs(u, p=-1):
        for v in adj[u]:
            if v == p: continue
            par[v] = u
            child_cnt[u] += 1
            yield dfs(v, u)
        yield None 
    
    par = [-1] * N
    child_cnt = [0] * N
    dfs(0)

    size = [1] * N 
    leaf = [u for u in range(N) if not child_cnt[u]]
    
    rm = set()
    while leaf:
        u = leaf.pop()
        p = par[u]
        if size[u] > 3 or (size[u] < 3 and p == -1): return -1, []

        if size[u] < 3:
            size[p] += size[u]
            child_cnt[p] -= 1
        elif p != -1:
            rm.add((u + 1, p + 1))
            child_cnt[p] -= 1
        
        if p != -1 and not child_cnt[p]: leaf.append(p)

    res = [i + 1 for i, (u, v) in enumerate(edges) if (u, v) in rm or (v, u) in rm]
    return len(res), res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        edges = [list(map(int, input().split())) for _ in range(N - 1)]
        a, b = solve(N, edges)
        print(a)
        if a != -1: print(*b)


if __name__ == '__main__':
    main()

