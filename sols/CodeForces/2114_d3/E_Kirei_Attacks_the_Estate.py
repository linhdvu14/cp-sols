''' E. Kirei Attacks the Estate
https://codeforces.com/contest/2114/problem/E
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


def solve(N, A, edges):
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)
    
    res = [-1] * N
    
    @bootstrap
    def dfs(u, p=-1, s=0, d=1, mn=INF, mx=-INF):
        s += A[u] * d
        mn = min(mn, s)
        mx = max(mx, s)
        if d == 1:
            res[u] = max(s, s - mn)
        else:
            res[u] = max(-s, mx - s)
        for v in adj[u]:
            if v == p: continue
            yield dfs(v, u, s, -d, mn, mx)
        yield None

    dfs(0)
    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        edges = [list(map(int, input().split())) for _ in range(N - 1)]
        res = solve(N, A, edges)
        print(*res)


if __name__ == '__main__':
    main()

