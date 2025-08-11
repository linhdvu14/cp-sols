''' Star Trappers
https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000888d45
'''

from math import sqrt
from heapq import heappush, heappop

INF = float('inf')

# cross product: pq x pr
def cross(p,q,r): return (q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0])

# get orientation going from p -> q -> r
# 0 = collinear
# 1 = counterclockwise (left turn)
# -1 = clockwise (right turn)
def ccw(p,q,r):
    det = cross(q,r,p)
    if det==0: return 0
    return 1 if det>0 else -1


def distance(p, q):
    dx, dy = p[0]-q[0], p[1]-q[1]
    return sqrt(dx*dx+dy*dy)


def djikstra_circle(adj, src):
    front = []
    known = set()
    for v,w in adj[src]:
        heappush(front, (w,v))
    
    while front:
        d,u = heappop(front)
        if u==src: return d
        if u in known: continue
        known.add(u)
        for v,w in adj[u]:
            # if v in known: continue
            heappush(front, ((d+w),v))

    return INF


def solve(blue, whites, N):
    # connect white pair w1 -> w2 if ccw(w1, w2, blue) == 1
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            orient = ccw(whites[i], whites[j], blue)
            dist = distance(whites[i], whites[j])
            if orient == 1:
                adj[i].append((j, dist))
            elif orient == -1:
                adj[j].append((i,dist))
    
    # shortest circle from each src
    res = INF
    for src in range(N):
        d = djikstra_circle(adj, src)
        res = min(res, d)
    
    return res if res < INF else 'IMPOSSIBLE' 


def main():
    from sys import stdin
    
    T = int(stdin.readline().strip())

    for t in range(T):
        N = int(stdin.readline().strip())
        whites = [tuple(map(int, stdin.readline().strip().split())) for _ in range(N)]
        blue = tuple(map(int, stdin.readline().strip().split()))
        out = solve(blue, whites, N)
        print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
    main()
