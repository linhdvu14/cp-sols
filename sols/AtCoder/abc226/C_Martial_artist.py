''' C - Martial artist
https://atcoder.jp/contests/abc226/tasks/abc226_c
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

from collections import deque

def main():
    N = int(input())
    cost = [0]*N
    adj = [[] for _ in range(N)]
    for u in range(N):
        nums = list(map(int, input().split()))
        cost[u] = nums[0]
        adj[u] = [num-1 for num in nums[2:]]

    seen = [False]*N
    seen[-1] = True
    queue = deque([N-1])
    res = 0
    while queue:
        u = queue.pop()
        res += cost[u]
        for v in adj[u]:
            if seen[v]: continue
            queue.append(v)
            seen[v] = True
    print(res)


if __name__ == '__main__':
    main()

