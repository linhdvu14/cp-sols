''' G. Rudolf and CodeVid-23
https://codeforces.com/contest/1846/problem/G
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
from heapq import heappush, heappop 

def solve(N, M, orig_mask, A):
    ONE = (1 << N) - 1

    dist = [INF] * (1 << N)
    dist[orig_mask] = 0

    h = [(0, orig_mask)]
    while h:
        d, mask = heappop(h)
        if dist[mask] < d: continue
        for d2, rm, add in A:
            nxt_mask = mask & (rm ^ ONE) | add
            if dist[nxt_mask] <= d + d2: continue
            dist[nxt_mask] = d + d2 
            heappush(h, (d + d2, nxt_mask))

    res = dist[0]
    return res if res < INF else -1


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        mask = int(input().decode().strip(), 2)
        A = []
        for _ in range(M):
            d = int(input())
            rm = int(input().decode().strip(), 2)
            add = int(input().decode().strip(), 2)
            A.append((d, rm, add))
        res = solve(N, M, mask, A)
        print(res)


if __name__ == '__main__':
    main()
