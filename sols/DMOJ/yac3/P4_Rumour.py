''' Yet Another Contest 3 P4 - Rumour
https://dmoj.ca/problem/yac3p4
'''

# to test: 
# pypy3 template.py
# or: python3 interactive_runner.py python3 local_testing_tool.py 0 -- python3 a.py

import functools
import os, sys
input = sys.stdin.readline  # strip() if str; io.BytesIO(os.read(0,os.fstat(0).st_size)).readline doesn't work
output = functools.partial(print, flush=True)

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

def ask(x):
    output(f'{x + 1}')
    res = int(input())
    assert res != -1
    return res - 1


def main():
    N = int(input())
    adj = [set() for _ in range(N)]
    for _ in range(N-1):
        u, v = list(map(int, input().split()))
        adj[u-1].add(v-1)
        adj[v-1].add(u-1)
    
    # find subtree size
    @bootstrap
    def dfs1(u, p=-1):
        sz[u] = 1
        for v in adj[u]:
            if v == p: continue
            sz[u] += yield dfs1(v, u)
        yield sz[u]
    
    # find centroid
    @bootstrap
    def dfs2(u, n, p=-1):
        for v in adj[u]:
            if v == p: continue
            if sz[v] > n//2: yield (yield dfs2(v, n, u))
        yield u

    sz = [0] * N
    r = 0
    while True:
        # query centroid
        n = dfs1(r)
        y = dfs2(r, n)
        z = ask(y)
        if z == -1: break

        # remove centroid
        # if do not rm y, will TLE if 2 nodes remain
        for v in adj[y]: adj[v].remove(y)
        adj[y] = set()

        # continue in subtree continuing z
        r = z
 
if __name__ == '__main__':
    main()