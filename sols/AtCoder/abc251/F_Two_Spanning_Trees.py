''' F - Two Spanning Trees
https://atcoder.jp/contests/abc251/tasks/abc251_f
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def debug(*args):   
    if os.environ.get('debug') in [None, '0']: return
    from inspect import currentframe, getframeinfo
    from re import search
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')

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

INF = float('inf')

# -----------------------------------------

from collections import deque

def main():
    N, M = list(map(int, input().split()))

    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = list(map(int, input().split()))
        adj[u].append(v)
        adj[v].append(u)

    # dfs for t1
    @bootstrap
    def dfs(u):
        for v in adj[u]:
            if used[v]: continue
            used[v] = 1
            t1.append((u, v))
            yield dfs(v)
        yield None

    t1 = []
    used = [0] * (N + 1)
    used[1] = 1
    dfs(1)

    # bfs for t2
    t2 = []
    used = [0] * (N + 1)
    used[1] = 1
    queue = deque([1])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if used[v]: continue
            used[v] = 1
            t2.append((u, v))
            queue.append(v)
    
    return t1, t2


if __name__ == '__main__':
    r1, r2 = main()
    for t in r1: print(*t)
    for t in r2: print(*t)

