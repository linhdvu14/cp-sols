''' C. Copil Copac Draws Trees
https://codeforces.com/contest/1831/problem/C
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
    adj = [[] for _ in range(N)]
    for i, (u, v) in enumerate(edges):
        adj[u - 1].append((v - 1, i))
        adj[v - 1].append((u - 1, i))
    
    @bootstrap
    def dfs(u, p=-1, ui=-1):
        res = 1
        for v, vi in adj[u]:
            if v == p: continue
            cand = (yield dfs(v, u, vi)) + (1 if vi < ui else 0)
            res = max(res, cand)
        yield res
    
    res = dfs(0)
    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        edges = [list(map(int, input().split())) for _ in range(N - 1)]
        res = solve(N, edges)
        print(res)


if __name__ == '__main__':
    main()

