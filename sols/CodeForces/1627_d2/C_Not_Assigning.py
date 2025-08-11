''' C. Not Assigning
https://codeforces.com/contest/1627/problem/C
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


def solve(N, edges):
    adj = [[] for _ in range(N)]
    for i, (u, v) in enumerate(edges):
        adj[u-1].append((v-1, i))
        adj[v-1].append((u-1, i))

    # all non-leaf nodes must have degree 2 (2 + one odd prime)
    if max(len(e) for e in adj) > 2: return [-1]

    root = -1
    for u in range(N):
        if len(adj[u]) == 1:
            root = u
            break

    # alternate 2 and 3
    res = [-1]*(N-1)

    @bootstrap
    def dfs(u, c=2, p=-1):
        for v, i in adj[u]:
            if v != p:
                res[i] = c
                yield dfs(v, 5-c, u)
        yield None
    
    dfs(root)
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

