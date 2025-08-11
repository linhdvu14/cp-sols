''' Largest Square in the garden
https://www.codechef.com/JULY221A/problems/LARSQR31
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

class SparseTableMin:
    def __init__(self, data, func=min):
        self.func = func
        self.data = [list(data)]
        i, n = 1, len(self.data[0])
        while 2 * i <= n:
            prev = self.data[-1]
            self.data.append([func(prev[j], prev[j + i]) for j in range(n - 2 * i + 1)])
            i <<= 1

    def query(self, l, r):
        '''func of data[l..r]; O(1)'''
        depth = (r - l + 1).bit_length() - 1
        return self.func(self.data[depth][l], self.data[depth][r - (1 << depth) + 1])

    def __getitem__(self, idx):
        return self.data[0][idx]


def solve(N, segs):
    mxl = SparseTableMin([l for l, _ in segs], max)
    mnr = SparseTableMin([r for _, r in segs], min)

    def is_ok(d):
        for i in range(d-1, N):
            l = mxl.query(i-d+1, i)
            r = mnr.query(i-d+1, i)
            if r - l + 1 >= d: return True
        return False
    
    res, lo, hi = 1, 1, N
    while lo <= hi:
        mi = (lo + hi) // 2
        if is_ok(mi):
            res = mi
            lo = mi + 1
        else:
            hi = mi - 1

    return res


def main():
    N = int(input())
    segs = [list(map(int, input().split())) for _ in range(N)]
    out = solve(N, segs)
    print(out)


if __name__ == '__main__':
    main()

