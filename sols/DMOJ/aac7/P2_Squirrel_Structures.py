''' An Animal Contest 7 P2 - Squirrel Structures
https://dmoj.ca/problem/aac7p2
'''

import os, sys
input = sys.stdin.readline  # strip() if str

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
    for _ in range(N - 1):
        u, v = list(map(int, input().split()))
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    
    # hook each node to its grandparent
    root = {u: u for u in [0] + adj[0]}
    trees = {u: [] for u in [0] + adj[0]}

    @bootstrap
    def dfs(u, p=-1):        
        for v in adj[u]:
            if v == p: continue
            if p != -1: 
                trees[root[p]].append((v, p))
                root[v] = root[p]
            yield dfs(v, u)
        yield None 
    
    dfs(0, -1)
    
    print(len(trees))
    for edges in trees.values():
        print(len(edges) + 1)
        for u, v in edges: print(u+1, v+1)


if __name__ == '__main__':
    main()

