''' F. Not Splitting
https://codeforces.com/contest/1627/problem/F
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

from heapq import heappush, heappop

# halves must be rotationaly symmetric (around center)
# find paths from center to any boundary point s.t. pass through least adj edges

def solve(N, K, pairs):
    # convert to (K+1)*(K+1) grid of cell corners
    # hor[r][c] = edge weight between (r, c) and (r, c+1)
    # ver[r][c] = edge weight between (r, c) and (r+1, c)
    # weight is 1 if an edge or its mirror splits a pair
    hor = [[0]*K for _ in range(K)]
    ver = [[0]*K for _ in range(K)]
    for r1, c1, r2, c2 in pairs:
        if r1 + c1 > r2 + c2: r1, c1, r2, c2 = r2, c2, r1, c1
        if r1 == r2:
            ver[r1-1][c1] += 1
            ver[K-r1][K-c1] += 1
        else: 
            hor[r1][c1-1] += 1
            hor[K-r1][K-c1] += 1

    # djikstra from center to any boundary
    front = []
    dist = [[-1]*(K+1) for _ in range(K+1)]
    heappush(front, (0, K//2, K//2))

    while front:
        d, r, c = heappop(front)
        if dist[r][c] != -1: continue
        dist[r][c] = d
        if r == 0 or r == K or c == 0 or c == K: return N - d
        heappush(front, (d + ver[r-1][c], r-1, c))
        heappush(front, (d + ver[r][c], r+1, c))
        heappush(front, (d + hor[r][c-1], r, c-1))
        heappush(front, (d + hor[r][c], r, c+1))



def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        pairs = [list(map(int, input().split())) for _ in range(N)]
        out = solve(N, K, pairs)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

