''' Yet Another Contest 4 P3 - Canadian Cactus Competition
https://dmoj.ca/problem/yac4p3
'''

import os, sys
input = sys.stdin.readline  # strip() if str

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


def solve(N, M, B, edges):
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    
    m = 1 << (B.bit_length() - 1)
    val = [m, m - 1, 0]
    idx = [-1] * N

    # bi- or tri-coloring
    @bootstrap
    def dfs(u, p=-1):
        ok = [1] * 3
        for v in adj[u]:
            if idx[v] != -1: 
                ok[idx[v]] = 0
        for i in range(3):
            if ok[i]: 
                idx[u] = i
                break
        for v in adj[u]:
            if v == p or idx[v] != -1: continue
            yield dfs(v, u)
        yield None
    
    for u in range(N):
        if idx[u] != -1: continue
        dfs(u)

    res = INF
    for u, v in edges:
        res = min(res, val[idx[u-1]] ^ val[idx[v-1]])
    
    return res, [val[idx[u]] for u in range(N)]


def main():
    N, M, B = list(map(int, input().split()))
    edges = [list(map(int, input().split())) for _ in range(M)]
    r1, r2 = solve(N, M, B, edges)
    print(r1)
    print(*r2)


if __name__ == '__main__':
    main()
