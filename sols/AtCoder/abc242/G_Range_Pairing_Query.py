''' G - Range Pairing Query
https://atcoder.jp/contests/abc242/tasks/abc242_g
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

from math import ceil, sqrt

# mo's algorithm
def main():
    N = int(input())
    A = [x-1 for x in map(int, input().split())]

    # divide queries to buckets of same l, sorted r
    Q = int(input())
    sz = ceil(sqrt(N))  #ceil(N / sqrt(2 * Q))
    buckets = [[] for _ in range(N//sz + 1)]
    for i in range(Q):
        l, r = map(int, input().split())
        l -= 1; r -= 1
        buckets[l//sz].append((l, r, i))
    for i in range(len(buckets)):
        buckets[i].sort(key=lambda x: x[1], reverse=i&1)
    
    # calc
    odd = [0] * len(A)
    pairs = 0
    l, r = 0, -1
    res = [0] * Q
    for bucket in buckets:
        for ql, qr, qi in bucket:
            while l > ql: 
                l -= 1
                pairs += odd[A[l]]
                odd[A[l]] ^= 1
            while r < qr: 
                r += 1
                pairs += odd[A[r]]
                odd[A[r]] ^= 1
            while l < ql: 
                odd[A[l]] ^= 1
                pairs -= odd[A[l]]
                l += 1
            while r > qr: 
                odd[A[r]] ^= 1
                pairs -= odd[A[r]]
                r -= 1
            res[qi] = pairs
    
    print(*res, sep='\n')


if __name__ == '__main__':
    main()

