''' E - Subtree K-th Max
https://atcoder.jp/contests/abc239/tasks/abc239_e
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


def main():
    N, Q = list(map(int, input().split()))
    X = list(map(int, input().split()))
    
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = list(map(int, input().split()))
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    
    top = [[] for _ in range(N)]

    @bootstrap
    def dfs(u, p=-1):
        cands = [X[u]]
        for v in adj[u]:
            if v == p: continue
            yield dfs(v, u)
            cands += top[v]
        top[u] = sorted(cands, reverse=True)[:20]
        yield None
    
    dfs(0)
    res = []
    for _ in range(Q):
        u, k = list(map(int, input().split()))
        res.append(top[u-1][k-1])

    print('\n'.join(map(str, res)))



if __name__ == '__main__':
    main()


