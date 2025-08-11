''' G1. Passable Paths (easy version)
https://codeforces.com/contest/1702/problem/G1
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


def main():
    N = int(input())
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = list(map(int, input().split()))
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)

    # S reachable if no node has > 2 branches containing nodes in S 
    def is_ok(S):
        S = set(u-1 for u in S)
        cnt = [0] * N  # num nodes in S under u's subtree

        @bootstrap
        def dfs(u, p=-1):
            if u in S: cnt[u] = 1
            branches = 0
            ok = True
            for v in adj[u]:
                if v == p: continue
                ok &= yield dfs(v, u)
                if cnt[v]:
                    branches += 1
                    cnt[u] += cnt[v]
            if len(S) - cnt[u]: branches += 1
            yield ok and branches < 3
            
        return dfs(0)

    
    Q = int(input())
    res = ['NO'] * Q
    for i in range(Q):
        K = int(input())
        S = set(map(int, input().split()))
        if is_ok(S): res[i] = 'YES'
        
    print(*res, sep='\n')


if __name__ == '__main__':
    main()

