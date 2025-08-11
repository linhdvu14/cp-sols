''' E1. Escape The Maze (easy version)
https://codeforces.com/contest/1611/problem/E1
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

INF = float('inf')

from collections import deque

# win if can reach a node before any foe
def solve(N, K, foes, edges):
    foes = [u-1 for u in foes]
    adj = [set() for _ in range(N)]
    for u, v in edges:
        adj[u-1].add(v-1)
        adj[v-1].add(u-1)

    # min dist to root
    dist_root = [INF]*N
    queue = deque([(0, -1, 0)])
    while queue:
        u, p, d = queue.popleft()
        if dist_root[u] < INF: continue
        dist_root[u] = d
        for v in adj[u]:
            if v == p or dist_root[v] < INF: continue
            queue.append((v, u, d+1))

    # min dist to foe
    dist_foe = [INF]*N
    queue = deque([(u, -1, 0) for u in foes])
    while queue:
        u, p, d = queue.popleft()
        if dist_foe[u] < INF: continue
        dist_foe[u] = d
        for v in adj[u]:
            if v == p or dist_foe[v] < INF: continue
            queue.append((v, u, d+1))

    # check for winning leaf
    for u in range(1, N):
        if len(adj[u]) != 1: continue
        if dist_root[u] < dist_foe[u]: return True
    return False



def main():
    T = int(input())
    for _ in range(T):
        input()
        N, K = list(map(int, input().split()))
        foes = list(map(int, input().split()))
        edges = [list(map(int, input().split())) for _ in range(N-1)]
        out = solve(N, K, foes, edges)
        print('YES' if out else 'NO')


if __name__ == '__main__':
    main()

