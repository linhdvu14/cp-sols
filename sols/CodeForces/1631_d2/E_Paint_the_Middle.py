''' E. Paint the Middle
https://codeforces.com/contest/1631/problem/E
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

# tests
# 7 2 3 4 7 4 2
# 5 2 7 5 2 7 4

def solve(N, A):
    # find first and last idx of each value
    left = [-1] * (N+1)
    right = [-1] * (N+1)
    for i, a in enumerate(A):
        if left[a] == -1: left[a] = i
        right[a] = i
    
    # indices inside each interval (l, r) can be set to 1
    intervals = []
    for l, r in zip(left, right):
        if l == -1 or l == r: continue
        intervals.append((l, r))
    intervals.sort()

    # all non-endpoint indices can be set
    # an interval nested inside previous interval (r2 < r1) can be rm
    tmp = []
    for l, r in intervals:
        if tmp and r < tmp[-1][1]: continue
        tmp.append((l, r))
    intervals = tmp

    # an interval covered by its previous and subsequent intervals (r1 > l3) can be rm
    tmp = []
    for i, (l, r) in enumerate(intervals):
        if tmp and i < len(intervals)-1 and tmp[-1][-1] > intervals[i+1][0]: continue
        tmp.append((l, r))
    intervals = tmp

    # all rightmost endpoints, except last one can be set
    res, end = 0, -1
    for i, (l, r) in enumerate(intervals):
        if l > end:  # first interval in cc
            res += r - l - 1
        else:
            res += r - end - 1
        end = r
 
    return res


def main():
    N = int(input())
    A = list(map(int, input().split()))
    out = solve(N, A)
    output(f'{out}\n')


if __name__ == '__main__':
    main()

