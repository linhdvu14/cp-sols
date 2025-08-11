''' G. Tokens on Graph
https://codeforces.com/contest/1790/problem/G
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

INF = float('inf')

# -----------------------------------------
from collections import deque

# alternate between moving 1 main chip towards 1 and moving any other chip to a bonus node
# main chip should be closest node reachable from 1 via bonus path
# other chips either move 1 step to bonus node or bounce between 2 bonus nodes

def solve(N, M, C, B, chips, bonuses, edges):
    chips = [u - 1 for u in chips]
    is_bonus = [0] * N 
    for b in bonuses: is_bonus[b - 1] = 1

    adj = [[] for _ in range(N)]
    can_bounce = [0] * N
    for u, v in edges:
        u -= 1; v -= 1
        adj[u].append(v)
        adj[v].append(u)
        if is_bonus[u] and is_bonus[v]: can_bounce[u] = can_bounce[v] = 1

    # dist from 0 via bonus
    dist = [INF] * N
    dist[0] = 0
    queue = deque([0])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if not is_bonus[v] or dist[v] < INF: continue
            dist[v] = dist[u] + 1
            queue.append(v)
    
    # pick main chip
    best = None
    for u in chips:
        if not u: return 'YES'
        d = INF 
        for v in adj[u]: d = min(d, dist[v] + 1)
        if d < INF and (not best or best[0] > d): best = (d, u)
    if not best: return 'NO'

    need, chosen = best
    if C == 1: return 'YES' if need < 2 else 'NO'
    
    # other chips should match or exceed main chip's travel distance
    have = 0
    for u in chips:
        if u == chosen: continue
        if any(can_bounce[v] for v in adj[u]): have += INF 
        elif any(is_bonus[v] for v in adj[u]): have += 1

    return 'YES' if have >= need - 1 else 'NO'


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        C, B = list(map(int, input().split()))
        chips = list(map(int, input().split()))
        bonuses = list(map(int, input().split()))
        edges = [list(map(int, input().split())) for _ in range(M)]
        _ = input()
        res = solve(N, M, C, B, chips, bonuses, edges)
        print(res)


if __name__ == '__main__':
    main()
