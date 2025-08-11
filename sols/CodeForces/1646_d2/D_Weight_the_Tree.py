''' D. Weight the Tree
https://codeforces.com/contest/1646/problem/D
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


# https://www.cs.princeton.edu/~wayne/kleinberg-tardos/pearson/10ExtendingTractability.pdf
def solve(N, edges):
    if N == 2: return 2, 2, [1, 1]

    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)

    # dp_in[u] = (max good nodes in u's subtree, min sum nodes in u's subtree) if u is good
    # dp_out[u] = .... if u is not good
    dp_in = [[1, -len(adj[u])] for u in range(N)]
    dp_out = [[0, -1] for _ in range(N)]

    @bootstrap
    def dfs1(u, p=-1):
        for v in adj[u]:
            if v == p: continue
            yield dfs1(v, u)
            dp_in[u][0] += dp_out[v][0]
            dp_in[u][1] += dp_out[v][1]
            mx = max(dp_in[v], dp_out[v])
            dp_out[u][0] += mx[0]
            dp_out[u][1] += mx[1]
        yield None
    
    dfs1(0)

    # trace
    mx = max(dp_in[0], dp_out[0])
    val_map = [1] * N

    @bootstrap
    def dfs2(u, p, is_in):
        if is_in: val_map[u] = len(adj[u])
        for v in adj[u]:
            if v == p: continue
            if is_in or dp_out[v] > dp_in[v]: yield dfs2(v, u, False)
            else: yield dfs2(v, u, True)
        yield None
    
    dfs2(0, -1, dp_in[0] == mx) 
    return mx[0], -mx[1], val_map



def main():
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N-1)]
    r1, r2, r3 = solve(N, edges)
    print(r1, r2)
    print(*r3)


if __name__ == '__main__':
    main()

