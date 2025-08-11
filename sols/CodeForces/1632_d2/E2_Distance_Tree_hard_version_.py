''' E2. Distance Tree (hard version)
https://codeforces.com/contest/1632/problem/E2
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


# let f(x) = result for given x
# consider all nodes u with depth(u) > f(x)
# should add edge (0, m) s.t. dist(u, m) + dist(m, 0) = dist(u, m) + x <= f(x)

# pick u1, u2 s.t. dist(u1, u2) is max and set m = midpoint(u1, u2)
# then for all u, dist(u, m) <= max(dist(u1, m), dist(u2, m)) --> dist(u, m) + x <= max(dist(u1, m), dist(u2, m)) + x
# thus f(x) is valid iff max(dist(u1, m), dist(u2, m)) + x <= f(x)
# iff ceil(dist(u, v) / 2) + x <= f(x)

# let D(d) = max dist(u1, u2) s.t. depth(u1), depth(u2) > d
# then ans f(x) is min d s.t. ceil(D(d) / 2) + x <= d
# note that D(d) increases as d decreases

# how to calc D(d) for all d ?
# consider each u as a potential lca(u1, u2) for some d, then
# * u1, u2 must come from the subtrees of 2 different children of u
# * min(depth(u1), depth(u2)) > d
# -> algo:
# 1. find u1, u2 with max depth from different subtrees
# 2. let p = min(depth(u1), depth(u2)), update D(d) for all d=0..p-1

def solve(N, edges):
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    
    # D[d] = max dist between 2 nodes whose depth > d
    D = [0] * N

    @bootstrap
    def dfs(u, p=-1, d=0):
        # find 2 subtrees with max depth
        mx1 = mx2 = d  # distance to root
        for v in adj[u]:
            if v == p: continue
            c = yield dfs(v, u, d+1)
            if c > mx1: mx1, mx2 = c, mx1
            elif c > mx2: mx2 = c

        # take u as potential lca
        if mx2 > 0: D[mx2-1] = max(D[mx2-1], mx1 + mx2 - 2*d)
        yield mx1

    # propagate
    mxd = dfs(0)
    for i in range(N-2, -1, -1):
        D[i] = max(D[i], D[i+1])

    # output
    res = []
    for x in range(1, N+1):
        d, lo, hi = mxd, 0, mxd
        while lo <= hi:
            mi = (lo + hi) // 2
            if mi >= (D[mi] + 1) // 2 + x:
                d = mi
                hi = mi - 1
            else:
                lo = mi + 1
        res.append(d)

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        edges = [list(map(int, input().split())) for _ in range(N-1)]
        out = solve(N, edges)
        print(*out)


if __name__ == '__main__':
    main()

