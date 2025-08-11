''' Maximum Trio
https://www.codechef.com/LTIME103B/problems/MXMTRIO
'''

import io, os, sys
from re import I
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

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

def solve(N, A):
    SA = sorted(A)
    first = {}
    for i, a in enumerate(SA):
        if a not in first: first[a] = i
    
    # should reverse entire interval (orig pos, correct pos)
    intervals = []
    for i, a in enumerate(A):
        intervals.append(sorted([i, first[a]]))
    intervals.sort()

    # merge then reverse
    res = 0
    start, end = intervals[0]
    for s, e in intervals[1:]:
        if s > end:
            res += max(A[start:end+1]) - min(A[start:end+1])
            start, end = s, e
        end = max(end, e)
    
    res += max(A[start:end+1]) - min(A[start:end+1])
    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

