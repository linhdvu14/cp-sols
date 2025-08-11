''' D - ±1 Operation 2
https://atcoder.jp/contests/abc255/tasks/abc255_d
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

from bisect import bisect_left, bisect_right

def main():
    N, Q = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A.sort()

    pref = [0]
    for a in A: pref.append(pref[-1] + a)

    res = []
    for _ in range(Q):
        x = int(input())
        l = bisect_left(A, x)
        r = bisect_right(A, x)
        res.append((x * l - pref[l]) + (pref[-1] - pref[r] - x * (N - r)))
    
    print(*res, sep='\n')





if __name__ == '__main__':
    main()

