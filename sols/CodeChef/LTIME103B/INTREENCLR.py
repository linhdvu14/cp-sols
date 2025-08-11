''' In-tree-active Node Coloring
https://www.codechef.com/LTIME103B/problems/INTREENCLR
'''

# to test: 
# pypy3 template.py
# or: python interactive_runner.py python local_testing_tool.py 0 -- python3 a.py

import functools
import os, sys
input = sys.stdin.readline  # io.BytesIO(os.read(0,os.fstat(0).st_size)).readline doesn't work
output = functools.partial(print, flush=True)

DEBUG = os.environ.get('debug') is not None

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

def query(x):
    output(f'{x}')
    y = int(input())
    if y == -1: exit(1)
    return y


def solve():
    N, _ = list(map(int, input().split()))
    
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = list(map(int, input().split()))
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)

    # color[u] = 1 if u (flipped) has same color as parent (flipped)
    color = [-1]*N

    @bootstrap
    def dfs1(u, p=-1):
        child_same = 0

        # set subtree color
        for v in adj[u]:
            if v == p: continue
            child_same += yield dfs1(v, u)
        
        # set u's color
        diff = query(u+1)
        color[u] = diff - (len(adj[u]) - 1 - child_same)
        if p == -1: assert color[u] == 1

        yield color[u]
    
    dfs1(0)
    debug(color)

    # color[u] = final color of u
    @bootstrap
    def dfs2(u, p=-1):
        for v in adj[u]:
            if v == p: continue
            color[v] = color[u] ^ (1 - color[v])
            yield dfs2(v, u)
        yield None

    dfs2(0)
    debug(color)

    # flip minority color
    minority = 1 if sum(color) <= N/2 else 0
    debug(minority)

    for u, c in enumerate(color):
        if c == minority:
            query(u+1)
    
    # check
    _ = query(0)

    return


def main():
    T = int(input())
    for _ in range(T):
        solve()
    
 
if __name__ == '__main__':
    main()