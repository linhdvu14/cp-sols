''' Minimise Difference
https://www.codechef.com/SNCKQL21/problems/MINDIFF1
'''


import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write


from heapq import heappop, heappush

# minimize max Di
# always optimal to assign highest val to node with fewest neighbors
# otherwise can swap without increasing max Di
def solve(N, M, edges):
    adj = [[] for _ in range(N)]
    count_nei = [0]*N
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        count_nei[u] += 1
        count_nei[v] += 1
    
    h = []
    for u in range(N):
        heappush(h, (count_nei[u], u))
    
    assignment = [0]*N
    for val in range(N, 0, -1):
        while True:
            _, u = heappop(h)
            if assignment[u] == 0: break
        assignment[u] = val
        for v in adj[u]:  # disconnect u-v
            if assignment[v] != 0: continue
            count_nei[v] -= 1
            # min heap so last entry guaranteed to pop first
            # no need to clean stale nodes
            heappush(h, (count_nei[v], v))

    assert len(set(assignment)) == N

    # max Di under assignment
    count_smaller = [0]*N
    for u, v in edges:
        if assignment[u] > assignment[v]:
            count_smaller[u] += 1
        else:
            count_smaller[v] += 1
    
    output(str(max(count_smaller)) + '\n')
    output(' '.join(map(str, assignment)) + '\n')


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        edges = []
        for _ in range(M):
            u, v = list(map(int, input().split()))
            edges.append((u-1, v-1))
        solve(N, M, edges)


if __name__ == '__main__':
    main()

