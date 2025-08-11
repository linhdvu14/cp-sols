''' E. Purple Crayon
https://codeforces.com/contest/1615/problem/E
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

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

# w(r-b) = (n-r-b)(r-b) = (n-r-b)r - (n-r-b)b = nr - rr - nb + bb = (n-r)r - (n-b)b
# B should pick b close to n/2
# R can pick up to k leaves; for each r, should minimize B's choosable nodes 

# https://codeforces.com/contest/1615/submission/140470104

def solve(N, K, edges):
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)

    # how many new nodes become unavailable for B under R's optimal policy?
    # equal distance from node to first unavailable node
    ban = []

    # return max depth from all u's subtrees
    # picking u adds 0; picking any non-max subtree adds its own depth
    @bootstrap
    def dfs(u, p=-1):
        mx = 0
        for v in adj[u]:
            if v == p: continue
            cand = yield dfs(v, u)
            if cand > mx: mx, cand = cand, mx
            ban.append(cand)
        yield mx + 1
    
    ban.append(dfs(0))
    ban.sort(reverse=True)

    # simulate
    res = -INF
    avail = N
    for r in range(K+1):
        if r > 0: avail -= ban[r-1]
        b = min(avail, N//2)
        res = max(res, (N-r-b)*(r-b))
    return res



def main():
    N, K = list(map(int, input().split()))
    edges = [list(map(int, input().split())) for _ in range(N-1)]
    out = solve(N, K, edges)
    output(f'{out}\n')


if __name__ == '__main__':
    main()

