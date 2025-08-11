''' D. Reachability and Tree
https://codeforces.com/contest/2112/problem/D
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

from inspect import currentframe, getframeinfo
from re import search
DEBUG = os.environ.get('debug') not in [None, '0']

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


def solve(N, edges):
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)
    
    for u in range(N):
        if len(adj[u]) == 2:
            root = u
            break
    else:
        return []
    
    res = []
    
    @bootstrap
    def dfs(u, p=-1, d=1):
        nonlocal res
        if u == root:
            v1, v2 = adj[u]
            res += [(v1, root), (root, v2)]
            yield dfs(v1, u, 1)
            yield dfs(v2, u, -1)
        else:
            for v in adj[u]:
                if v == p: continue
                res += [(u, v)] if d == 1 else [(v, u)]
                yield dfs(v, u, -d)
        yield None

    dfs(root)
    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        edges = [list(map(int, input().split())) for _ in range(N - 1)]
        res = solve(N, edges)
        print('YES' if res else 'NO')
        for u, v in res: print(u + 1, v + 1)


if __name__ == '__main__':
    main()
