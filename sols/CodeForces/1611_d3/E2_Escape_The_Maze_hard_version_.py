''' E2. Escape The Maze (hard version)
https://codeforces.com/contest/1611/problem/E2
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

INF = float('inf')

from collections import deque

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
        if dist_root[u] < dist_foe[u]: return -1

	# R moves down as foes move up
    # any subtree with dist_root >= dist_foe only needs 1 foe for all leaves underneath
    res = 0
    queue = deque([(0, -1)])
    while queue:
        u, p = queue.popleft()
        if dist_root[u] >= dist_foe[u]:
            res += 1
        else:
            for v in adj[u]:
                if v == p: continue
                queue.append((v, u))

    return res

def main():
    T = int(input())
    for _ in range(T):
        input()
        N, K = list(map(int, input().split()))
        foes = list(map(int, input().split()))
        edges = [list(map(int, input().split())) for _ in range(N-1)]
        out = solve(N, K, foes, edges)
        print(out)


if __name__ == '__main__':
	main()

