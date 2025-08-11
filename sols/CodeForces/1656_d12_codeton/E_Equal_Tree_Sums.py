''' E. Equal Tree Sums
https://codeforces.com/contest/1656/problem/E
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


# bicolor nodes
# assign black node deg(v) and white node -deg(v)
# any tree created this way has node sum = 0
# then after rm v, all subtrees has sum +1 or -1 from the incident edge with v

def solve(N, edges):
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    
    val = [0] * N

    @bootstrap
    def dfs(u, p=-1, s=1):
        val[u] = s * len(adj[u])
        for v in adj[u]:
            if v == p: continue
            yield dfs(v, u, -s)
        yield None
    
    dfs(0)
    return val


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        edges = [list(map(int, input().split())) for _ in range(N-1)]
        out = solve(N, edges)
        print(*out)


if __name__ == '__main__':
    main()

