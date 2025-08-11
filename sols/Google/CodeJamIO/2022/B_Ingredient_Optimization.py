''' Ingredient Optimization 
https://codingcompetitions.withgoogle.com/codejamio/round/00000000009d9870/0000000000a341ec
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

from collections import deque
from heapq import heappush, heappop

def solve(D, N, U, goods, orders):
    remain = deque(goods)
    avail = []

    res = 0
    for o in orders:
        while remain and remain[0][0] <= o:
            m, l, e = remain.popleft()
            heappush(avail, (m + e, l))
        need = U
        while avail and need:
            e, l = heappop(avail)
            if e <= o: continue
            use = min(need, l)
            need -= use
            l -= use
            if l: heappush(avail, (e, l))
        if need: break
        res += 1

    return res


def main():
    T = int(input())
    for t in range(T):
        D, N, U = list(map(int, input().split()))
        goods = [tuple(map(int, input().split())) for _ in range(D)]
        orders = list(map(int, input().split()))
        out = solve(D, N, U, goods, orders)
        print(f'Case #{t+1}: {out}')


if __name__ == '__main__':
    main()

