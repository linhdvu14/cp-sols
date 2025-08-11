''' Segmentation Fault 
https://www.codechef.com/COOK143A/problems/SEGFAULT
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

# for int dict key
from random import randrange
RAND = randrange(1 << 62)
def conv(x): return x ^ RAND

INF = float('inf')

# -----------------------------------------

# find all idx that appears in all but one seg
def solve(N, segs):
    endpoints = [s for l, r in segs for s in [(l-1, 1), (r, -1)]]
    endpoints.sort(reverse=True)

    res = []
    bal = 0
    for i in range(N):
        while endpoints and endpoints[-1][0] <= i: bal += endpoints.pop()[1]
        if bal == N-1 and not (segs[i][0] <= i+1 <= segs[i][1]): res.append(i+1)
    
    return res
    


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        segs = [list(map(int, input().split())) for _ in range(N)]
        out = solve(N, segs)
        print(len(out))
        print(*out, sep='\n')


if __name__ == '__main__':
    main()

