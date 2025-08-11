''' C. Almost Increasing Subsequence
https://codeforces.com/contest/1818/problem/C
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
from bisect import bisect_left

def solve(N, Q, A, queries):
    segs = []
    i = 0
    while i < N:
        j = i + 1
        while j < N and A[j] <= A[j - 1]: j += 1
        if j - i > 2: segs.append((i, j))
        i = j 
    
    M = len(segs)
    ps = [0] * (M + 1)
    for i, (l, r) in enumerate(segs): ps[i] = ps[i - 1] + (r - l - 2)

    res = [0] * Q
    for qi, (l, r) in enumerate(queries):
        l -= 1
        res[qi] = r - l
        li = bisect_left(segs, (l, l))
        ri = bisect_left(segs, (r, r)) - 1
        if li: 
            pl, pr = segs[li - 1]
            res[qi] -= max(min(pr, r) - max(pl, l) - 2, 0)    
        if ri >= li:
            pl, pr = segs[ri]
            res[qi] -= max(min(pr, r) - max(pl, l) - 2, 0)
        if ri > li: res[qi] -= ps[ri - 1] - ps[li - 1]

    return res


def main():
    N, Q = list(map(int, input().split()))
    A = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for _ in range(Q)]
    res = solve(N, Q, A, queries)
    print(*res, sep='\n')


if __name__ == '__main__':
    main()
