''' D. Fake Plastic Trees
https://codeforces.com/contest/1694/problem/D
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


# each node u is incremented only once to R[u]

def solve(N, P, segs):
    adj = [[] for _ in range(N)]
    for i, p in enumerate(P):
        adj[i+1].append(p-1)
        adj[p-1].append(i+1)
    
    # max flow-through of u's subtree
    @bootstrap
    def dfs(u, p=-1):
        nonlocal res
        s = 0
        for v in adj[u]:
            if v == p: continue
            s += yield dfs(v, u)
        if segs[u][0] > s: 
            res += 1
            yield segs[u][1]
        else:
            yield min(s, segs[u][1])
    
    res = 0
    dfs(0)

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        P = list(map(int, input().split()))
        segs = [list(map(int, input().split())) for _ in range(N)]
        out = solve(N, P, segs)
        print(out)


if __name__ == '__main__':
    main()

