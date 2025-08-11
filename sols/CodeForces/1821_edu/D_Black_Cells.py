''' D. Black Cells
https://codeforces.com/contest/1821/problem/D
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

def solve(N, K, L, R):
    res = INF
    s = 0
    h = []

    for l, r in zip(L, R):
        d = r - l + 1
        while s + d >= K:
            end = l + max(K - s - 1, 0)
            res = min(res, end + (len(h) + 1) * 2)
            if not h: break
            s -= heappop(h)
        s += d 
        heappush(h, d)

    return res if res < INF else -1


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        L = list(map(int, input().split()))
        R = list(map(int, input().split()))
        res = solve(N, K, L, R)
        print(res)


if __name__ == '__main__':
    main()


