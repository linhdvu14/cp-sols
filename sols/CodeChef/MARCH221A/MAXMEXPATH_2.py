''' MEX on Trees
https://www.codechef.com/MARCH221A/problems/MAXMEXPATH
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

cnt = [0] * (10**5 + 1)

def solve(N, A, edges):
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    
    res = 0

    @bootstrap
    def dfs(u, mex=0, p=-1):
        nonlocal res
        cnt[A[u]] += 1
        while cnt[mex] > 0: mex += 1
        res = max(res, mex)

        for v in adj[u]:
            if v == p: continue
            yield dfs(v, mex, u)
            
        cnt[A[u]] -= 1
        yield None
    
    dfs(0)
    return res
            


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        edges = [list(map(int, input().split())) for _ in range(N-1)]
        out = solve(N, A, edges)
        print(out)


if __name__ == '__main__':
    main()

