''' Yet Another Contest 3 P3 - Topology
https://dmoj.ca/problem/yac3p3
'''

import os, sys
input = sys.stdin.readline  # strip() if str

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

def solve(N, M, reqs):
    # merge
    reqs = [(t, l-1, r-1) for t, l, r in reqs]
    reqs.sort(key=lambda x: x[1])
    segs = []
    for t, l, r in reqs:
        if not segs or l > segs[-1][2] or (l == segs[-1][2] and t != segs[-1][0]): segs.append([t, l, r])
        elif l < segs[-1][2] and t != segs[-1][0]: return [-1]
        else: segs[-1][2] = max(segs[-1][2], r)

    # handle max height = 2
    if max(r - l + 1 for _, l, r in segs) == 2:
        for i in [1, 2]:
            cand = [i, 3-i] * (N // 2) + [i] * (N % 2)
            for t, l, r in segs:
                if t == 1 and cand[l] > cand[r]: break
                if t == 2 and cand[l] < cand[r]: break
            else: return cand
    
    # greedily minimize max value of each seg
    res = [0] * N 
    for t, l, r in segs:
        if t == 1:
            h = 1
            if l > 0 and res[l-1] == h: h += 1
            for i in range(l, r+1):
                res[i] = h 
                h += 1
        else:
            h = max(r - l + 1, res[l])
            if l > 0 and res[l-1] == h: h += 1
            for i in range(l, r+1):
                res[i] = h
                h -= 1

    # assign remaining
    mxh = max(res)
    for i in range(N):
        if res[i] != 0: continue
        for h in range(1, mxh+1):
            if not ((i > 0 and h == res[i-1]) or (i < N-1 and res[i+1] != 0 and h == res[i+1])):
                res[i] = h
                break

    return res


def main():
    N, M = list(map(int, input().split()))
    reqs = [list(map(int, input().split())) for _ in range(M)]
    out = solve(N, M, reqs)
    print(*out)


if __name__ == '__main__':
    main()
