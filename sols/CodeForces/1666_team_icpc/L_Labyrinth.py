''' L. Labyrinth
https://codeforces.com/contest/1666/problem/L
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

from collections import deque

def main():
    N, M, S = list(map(int, input().split()))
    S -= 1
    adj = [[] for _ in range(N)]
    for _ in range(M):
        u, v = list(map(int, input().split()))
        adj[u-1].append(v-1)

    if len(adj[S]) < 2: print('Impossible'); return

    # output
    def trace(u, v):
        tu = [v + 1, u + 1]
        cur = u
        while cur != S:
            cur = par[cur]
            tu.append(cur + 1)
        tu.reverse()

        tv = [v + 1]
        cur = v
        while cur != S:
            cur = par[cur]
            tv.append(cur + 1)
        tv.reverse()
        
        print('Possible', len(tu), ' '.join(map(str, tu)), len(tv), ' '.join(map(str, tv)), sep='\n')

    first_par, par = [-1] * N, [-1] * N
    queue = deque([])
    for u in adj[S]:
        first_par[u], par[u] = u, S
        queue.append(u)

    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if v == S: continue
            if first_par[v] == -1: 
                first_par[v], par[v] = first_par[u], u
                queue.append(v)
            elif first_par[v] != first_par[u]:
                trace(u, v)
                return
    
    print('Impossible')


if __name__ == '__main__':
    main()

