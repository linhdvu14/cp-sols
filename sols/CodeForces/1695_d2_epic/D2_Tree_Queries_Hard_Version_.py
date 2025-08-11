''' D2. Tree Queries (Hard Version)
https://codeforces.com/contest/1695/problem/D2
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

# for int dict key
from random import randrange
RAND = randrange(1 << 62)
def conv(x): return x ^ RAND

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

# https://atcoder.jp/contests/apc001/tasks/apc001_e
# if query u and v, all nodes on path u..v can be determined -> query nodes should be leaves
# if a subtree has n >= 2 children and alr a query at subtree root or outside, then need n-1 queries (in different children's subtrees) to distinguish all children nodes
# pick a node with 3+ children to be root and propagate bottom up

def solve(N, edges):
    if N == 1: return 0

    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    
    root = -1
    for u in range(N):
        if len(adj[u]) > 2:
            root = u
            break
    
    if root == -1: return 1  # line tree

    # min queries to distinguish u's descendants, excluding u
    # assume there's a query at u or outside u's subtree
    @bootstrap
    def dfs(u, p=-1):
        child = add = 0
        for v in adj[u]:
            if v == p: continue
            c = yield dfs(v, u)
            child += c
            if c == 0: add += 1
        yield child + max(add - 1, 0)

    return dfs(root)


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        edges = [list(map(int, input().split())) for _ in range(N-1)]
        out = solve(N, edges)
        print(out)


if __name__ == '__main__':
    main()

