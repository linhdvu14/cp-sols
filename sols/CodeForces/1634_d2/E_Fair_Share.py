''' E. Fair Share
https://codeforces.com/contest/1634/problem/E
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


from collections import deque

# construct bipartite graph
# * left vertices = arrays (M)
# * right vertices = values over all arrays (sum N)
# * edge (m, n) = array m contains value n (with multiplicity)
# then all vertices have even degrees, so there exists Eulerian circuit
# designate incoming = L, outgoing = R

def main():
    M = int(input())

    color = []
    adj = [deque([]) for _ in range(M)]
    val_map = {}
    val_id, edge_id = M, 0
    sizes = []

    for m in range(M):
        s = int(input())
        sizes.append(s)
        color += ['L'] * s

        A = list(map(int, input().split()))

        # pair up even occurrences
        seen = {}  # val -> (par, last idx)
        for i, n in enumerate(A):
            if n not in val_map: 
                adj.append(deque([]))
                val_map[n] = val_id
                val_id += 1
            n = val_map[n]
            if n not in seen: seen[n] = [0, -1]
            if seen[n][0] == 1: color[edge_id] = 'R'
            seen[n][0] ^= 1
            seen[n][1] = edge_id
            edge_id += 1
        
        # add remaining singles
        for n, (cnt, edge) in seen.items():
            if cnt == 0: continue
            adj[m].append((n, edge))
            adj[n].append((m, edge))

    if any(len(edges) % 2 == 1 for edges in adj): return 'NO'

    @bootstrap
    def dfs(u):
        while adj[u]:
            v, edge = adj[u].pop()
            if visited[edge]: continue
            visited[edge] = True
            tour.append(edge)
            yield dfs(v)
            break  # circuit, so much cycle back to start vertex
        yield None

    visited = [False] * edge_id
    for u in range(M):
        tour = []
        dfs(u)
        for i in range(0, len(tour), 2): color[tour[i]] = 'R'

    res = ['YES']
    i = 0
    for s in sizes:
        res.append(''.join(color[i:i+s]))
        i += s

    return '\n'.join(res)
    


if __name__ == '__main__':
    res = main()
    print(res)
