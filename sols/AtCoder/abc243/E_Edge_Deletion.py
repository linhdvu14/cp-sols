''' E - Edge Deletion
https://atcoder.jp/contests/abc243/tasks/abc243_e
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

def main():
    N, M = list(map(int, input().split()))

    edges = []
    dist = [[INF] * N for _ in range(N)]
    for _ in range(M):
        u, v, w = list(map(int, input().split()))
        dist[u-1][v-1] = w
        dist[v-1][u-1] = w
        edges.append((u-1, v-1, w))

    # all pair min dist
    for k in range(N):
        for u in range(N):
            for v in range(N):
                dist[u][v] = min(dist[u][v], dist[u][k] + dist[k][v])
    
    # rm edges that can be replaced by an intermediary node
    res = 0
    for u, v, w in edges:
        for i in range(N):
            if dist[u][i] + dist[i][v] <= w:
                res += 1
                break
    
    print(res)


if __name__ == '__main__':
    main()

