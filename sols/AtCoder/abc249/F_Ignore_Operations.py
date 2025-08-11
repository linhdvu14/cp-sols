''' F - Ignore Operations
https://atcoder.jp/contests/abc249/tasks/abc249_f
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


def main():
    N, K = list(map(int, input().split()))

    idx = [1] * (N + 1)  # whether op i is assignment
    val = [0] * (N + 1)
    for i in range(N):
        t, y = list(map(int, input().split()))
        if t != 1: idx[i+1] = 0
        val[i+1] = y

    # choose each possible final assignment
    res, s = -INF, 0
    negs = []
    for i in range(N, -1, -1):
        if idx[i]:
            while K >= 0 and len(negs) > K: s -= heappop(negs)
            if K >= 0: res = max(res, val[i] + s)
            K -= 1
        else:
            if val[i] >= 0: s += val[i]
            else: heappush(negs, -val[i])

    print(res)


if __name__ == '__main__':
    main()

