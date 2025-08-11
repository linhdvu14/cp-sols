''' D. This Is the Last Time
https://codeforces.com/contest/2126/problem/D
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

from inspect import currentframe, getframeinfo
from re import search
DEBUG = os.environ.get('debug') not in [None, '0']

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

def solve(N, K, segs):
    segs.sort(key=lambda t: t[2])
    
    for l, r, real in segs:
        if l <= K <= r:
            K = max(K, real)

    return K


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        segs = [list(map(int, input().split())) for _ in range(N)]
        res = solve(N, K, segs)
        print(res)


if __name__ == '__main__':
    main()

