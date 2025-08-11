''' F. 1-1-1, Free Tree!
https://codeforces.com/contest/2126/problem/F 
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

from inspect import currentframe, getframeinfo
from re import search
DEBUG = os.environ.get('debug') not in [None, '0']

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
import random

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


def solve():
    rand = random.randrange(1 << 60)
    N, Q = list(map(int, input().split()))
    A = list(map(int, input().split()))

    tot = same = 0
    adj = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, c = list(map(int, input().split()))
        u -= 1
        v -= 1
        adj[u].append([v, c])
        adj[v].append([u, c]) 
        tot += c
        if A[u] == A[v]: same += c

    par = [[-1, -1] for _ in range(N)]
    child = [{} for _ in range(N)]

    @bootstrap
    def dfs(u, p=-1):
        for v, c in adj[u]:
            if v == p: continue
            par[v] = [u, c]
            child[u][A[v]^rand] = child[u].get(A[v]^rand, 0) + c
            yield dfs(v, u)
        yield None

    dfs(0)

    res = [0] * Q
    for i in range(Q):
        u, a2 = list(map(int, input().split()))
        u -= 1
        p, pc = par[u]
        a1 = A[u]

        if a1 != a2:
            same += child[u].get(a2^rand, 0) - child[u].get(a1^rand, 0)
            if u:
                if A[p] == a1: same -= pc 
                if A[p] == a2: same += pc
                child[p][a1^rand] -= pc 
                if not child[p][a1^rand]: child[p].pop(a1^rand)
                child[p][a2^rand] = child[p].get(a2^rand, 0) + pc        
            A[u] = a2       

        res[i] = tot - same 

    print(*res, sep='\n')


def main():
    T = int(input())
    for _ in range(T):
        solve()


if __name__ == '__main__':
    main()

