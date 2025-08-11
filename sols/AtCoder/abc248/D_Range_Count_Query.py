''' D - Range Count Query 
https://atcoder.jp/contests/abc248/tasks/abc248_d
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
    N = int(input())
    A = list(map(int, input().split()))

    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    
    pos = {x: [] for _, _, x in queries}
    for i, a in enumerate(A):
        if a in pos: pos[a].append(i)
    
    res = []
    for l, r, x in queries:
        if not pos[x]: res.append(0)
        else:
            il = bisect_left(pos[x], l-1)
            ir = bisect_right(pos[x], r-1)
            res.append(ir - il)
    
    print(*res, sep='\n')


if __name__ == '__main__':
    main()

