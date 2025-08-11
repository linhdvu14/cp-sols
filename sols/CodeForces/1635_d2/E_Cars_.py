''' E. Cars
https://codeforces.com/contest/1635/problem/E
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

from collections import deque

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


def solve(N, M, edges):
    # t=0 -> head away, t=1 -> head towards
    # should form bipartite graph either way
    adj = [[] for _ in range(N)]
    for _, u, v in edges:
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    
    @bootstrap
    def dfs(u, c=0, p=-1):
        color[u] = c
        ok = True
        for v in adj[u]:
            if v == p: continue
            if color[v] == -1: ok = yield dfs(v, c^1, u)
            elif color[v] != c^1: ok = False
            if not ok: break
        yield ok

    color = [-1] * N
    for u in range(N):
        if color[u] == -1 and not dfs(u): return []
    
    # let 0 stay still, 1 move right
    # add edge u -> v if v is right of u
    adj = [[] for _ in range(N)]  # v in adj[u] if there is edge u <- v
    deg = [0] * N
    for t, u, v in edges:
        u -= 1
        v -= 1
        t -= 1
        if color[u] == t: # u -> v
            adj[v].append(u)  
            deg[u] += 1
        else:             # v -> u
            adj[u].append(v)
            deg[v] += 1
    
    # toposort
    res = [''] * N
    queue = deque([(u, color[u]) for u in range(N) if deg[u] == 0])
    i = 0
    while queue:
        u, d = queue.popleft()
        res[u] = 'R ' + str(i) if d % 2 == 0 else 'L ' + str(i)
        i += 1
        for v in adj[u]:
            deg[v] -= 1
            if deg[v] == 0: queue.append((v, d^1))
    if i < N: return []
    return res


def main():
    N, M = list(map(int, input().split()))
    edges = [list(map(int, input().split())) for _ in range(M)]
    out = solve(N, M, edges)
    if not out: 
        print('NO')
    else:
        print('YES')
        print('\n'.join(out))


if __name__ == '__main__':
    main()

