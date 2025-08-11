''' Convex Hulk
https://www.codechef.com/NOV21B/problems/CONHULK
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def cross(p, q): return p[0]*q[1] - p[1]*q[0]
def area2(p, q, r): return cross(p, q) + cross(q, r) + cross(r, p)

def point_inside_triangle(p, q, r, x):
    a = abs(area2(p, q, r))
    a1 = abs(area2(p, q, x))
    a2 = abs(area2(x, q, r))
    a3 = abs(area2(p, x, r))
    return a > 0 and a1 > 0 and a2 > 0 and a3 > 0 and a1 + a2 + a3 == a

def orient(p, q, r):
    det = area2(p, q, r)
    if det == 0: return 0
    return 1 if det > 0 else -1

def convex_hull(points, include_collinear=False, presorted=False):	
    if len(points) <= 2: return []
    if not presorted: points.sort()
    up, dn = [], []
    for p in points:
        if not include_collinear:
            while len(up) > 1 and orient(up[-2], up[-1], p) >= 0: up.pop()
            while len(dn) > 1 and orient(dn[-2], dn[-1], p) <= 0: dn.pop()
        else:
            while len(up) > 1 and orient(up[-2], up[-1], p) > 0: up.pop()
            while len(dn) > 1 and orient(dn[-2], dn[-1], p) < 0: dn.pop()
        up.append(p)
        dn.append(p)
    return dn + up[1:-1][::-1]


# let S = orig set of N points, CH = convex hull of S including collinear
# then cand set is
# * midpoints of all a-b in CH
# * midpoints of all b-d, for each neighbors (a-b, b-c) in CH and d in S that lies strictly inside triangle a-b-c
def solve(N, S):
    S.sort()
    
    # min idx s.t. S[idx][0] > x1
    def search_left(x1):
        idx, lo, hi = -1, 0, len(S)-1
        while lo <= hi: 
            mi = (lo + hi) // 2
            if S[mi][0] > x1:
                idx = mi
                hi = mi - 1
            else:
                lo = mi + 1
        return idx
    
    # max idx s.t. S[idx][0] < x2
    def search_right(x2):
        idx, lo, hi = -1, 0, len(S)-1
        while lo <= hi: 
            mi = (lo + hi) // 2
            if S[mi][0] < x2:
                idx = mi
                lo = mi + 1
            else:
                hi = mi - 1
        return idx

    # CH of orig point set
    CH = convex_hull(S, include_collinear=True, presorted=True)
    M = len(CH)

    # filter cands in final CH
    cands = set()
    for i in range(M):
        # midpoints of a-b
        a, b, c = CH[i], CH[(i+1) % M], CH[(i+2) % M]
        cands.add((a[0] + b[0], a[1] + b[1]))
        if orient(a, b, c) == 0: continue

        # midpoints of b-d
        l = search_left(min(a[0], b[0], c[0]))
        r = search_right(max(a[0], b[0], c[0]))
        for j in range(l, r+1):
            if point_inside_triangle(a, b, c, S[j]):
                cands.add((S[j][0] + b[0], S[j][1] + b[1]))

    # another round of CH
    cands = list(cands)
    hull = convex_hull(cands, include_collinear=False, presorted=False)
    return len(hull)


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        points = [tuple(map(int, input().split())) for _ in range(N)]
        out = solve(N, points)
        print(out)


if __name__ == '__main__':
    main()
