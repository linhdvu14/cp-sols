''' E. Hemose on the Tree
https://codeforces.com/contest/1670/problem/E
'''

import io, os, sys
from platform import node
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


# consider u = the first node with bit p set on any path from root, then cost(root..u) >= 2^p
# let root = 2^p and pair (x, x + 2^p) where x < 2^p
# construct s.t. costs <= 2^p

def solve():
    P = int(input())
    N = 1 << P

    adj = [[] for _ in range(N)]
    for i in range(N-1):
        u, v = list(map(int, input().split()))
        adj[u-1].append((v-1, i))
        adj[v-1].append((u-1, i))

    node_val = [-1] * N
    edge_val = [-1] * (N-1)
    x = 1

    @bootstrap
    def dfs(u, par=-1):
        nonlocal x
        for v, i in adj[u]:
            if v == par: continue
            if (node_val[u] >> P) & 1:
                edge_val[i] = x + (1 << P)
                node_val[v] = x
            else:
                edge_val[i] = x
                node_val[v] = x + (1 << P)
            x += 1
            yield dfs(v, u)
        yield None

    node_val[0] = 1 << P
    dfs(0)

    print(1)
    print(*node_val)
    print(*edge_val)



def main():
    T = int(input())
    for _ in range(T):
        solve()


if __name__ == '__main__':
    main()

