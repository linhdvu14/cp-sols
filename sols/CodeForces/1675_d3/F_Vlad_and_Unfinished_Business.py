''' F. Vlad and Unfinished Business
https://codeforces.com/contest/1675/problem/F 
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


# start from x and return to x
# need to visit all nodes whose subtrees contain a task or y
# each such node incurs cost of 2 (in and out)

def solve(N, K, x, y, A, edges):
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)

    dist = [-1] * N
    par = [-1] * N

    @bootstrap
    def dfs(u, p=-1, d=0):
        par[u] = p
        dist[u] = d
        for v in adj[u]:
            if v == p: continue
            yield dfs(v, u, d+1)
        yield None
    
    dfs(x-1)

    res = 0
    seen = [0] * N
    seen[x-1] = 1
    A.append(y)
    for u in A:
        u -= 1
        while not seen[u]:
            seen[u] = 1
            res += 2
            u = par[u]
    
    res -= dist[y-1]
    return res


def main():
    T = int(input())
    for _ in range(T):
        _ = input()
        N, K = list(map(int, input().split()))
        x, y = list(map(int, input().split()))
        A = list(map(int, input().split()))
        edges = [list(map(int, input().split())) for _ in range(N-1)]
        out = solve(N, K, x, y, A, edges)
        print(out)


if __name__ == '__main__':
    main()

