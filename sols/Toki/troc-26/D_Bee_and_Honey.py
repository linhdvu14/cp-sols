''' D. Bee and Honey
https://tlx.toki.id/contests/troc-26/problems/D
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
    K, L = list(map(int, input().split()))
    
    N = int(input())
    ab = [tuple(map(int, input().split())) for _ in range(N)]
    ab.sort()

    M = int(input())
    cd = [tuple(map(int, input().split())) for _ in range(M)]
    cd.sort()

    if K > L + M: return -1

    # time[i] = min time to consume flower i
    time = [INF] * M
    i, last = 0, -INF
    for j, (c, _) in enumerate(cd):
        while i < N and ab[i][0] <= c:
            if ab[i][1] == 1: last = ab[i][0]
            i += 1
        time[j] = min(time[j], c - last)

    i, last = N - 1, INF
    for j in range(M-1, -1, -1):
        c = cd[j][0]
        while i >= 0 and ab[i][0] >= c:
            if ab[i][1] == -1: last = ab[i][0]
            i -= 1
        time[j] = min(time[j], last - c)

    time = [(t, i) for i, t in enumerate(time) if t < INF]
    time.sort(reverse=True)

    # go as far as possible without consuming
    # when need to consume, start with lowest cost flower
    res = 0
    avail = []
    for t in range(L, K):           
        # just survived day t
        while time and time[-1][0] <= t:
            _, i = time.pop()
            heappush(avail, cd[i][1])
        # want to survive day t + 1
        if not avail: return -1
        res += heappop(avail)

    return res


if __name__ == '__main__':
    out = main()
    print(out)

