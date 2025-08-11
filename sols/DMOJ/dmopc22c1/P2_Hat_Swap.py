''' DMOPC '22 Contest 1 P2 - Hat Swap
https://dmoj.ca/problem/dmopc22c1p2
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

from collections import deque

def main():
    N, M = list(map(int, input().split()))
    C = list(map(int, input().split()))

    adj = [[] for _ in range(N)]
    for _ in range(M):
        u, v = list(map(int, input().split()))
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    
    # min dist to 0
    da = [INF] * N
    da[0] = 0
    q = deque([0])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if da[v] < INF: continue
            da[v] = da[u] + 1
            q.append(v)
    
    # min dist to N - 1
    db = [INF] * N
    db[N - 1] = 0
    q = deque([N - 1])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if db[v] < INF: continue
            db[v] = db[u] + 1
            q.append(v)
    
    # aggregate dist pair by color
    ga = [[] for _ in range(N)]
    gb = [[] for _ in range(N)]
    for i, (a, b, c) in enumerate(zip(da, db, C)):
        if a is INF and b is INF: continue
        ga[c - 1].append(i)
        gb[c - 1].append(i)

    res = INF
    for la, lb in zip(ga, gb):
        if len(la) < 2: continue
        la.sort(key=lambda i: da[i])
        lb.sort(key=lambda i: db[i])
        if la[0] != lb[0]: res = min(res, da[la[0]] + db[lb[0]])
        else: res = min(res, da[la[0]] + db[lb[1]], da[la[1]] + db[lb[0]])

    print(res if res < INF else -1)



if __name__ == '__main__':
    main()

