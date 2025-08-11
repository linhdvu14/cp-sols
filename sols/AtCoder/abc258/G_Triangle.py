''' G - Triangle
https://atcoder.jp/contests/abc258/tasks/abc258_g
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
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

BITS = 63  # probably for signed int; TLE with 64, 31

def popcount(x):
    x -= (x >> 1) & 0x5555555555555555
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
    x += x >> 8
    x += x >> 16
    x += x >> 32
    return x & 0x7f

# https://atcoder.jp/contests/abc258/submissions/32943134
# https://atcoder.jp/contests/abc258/submissions/33225929
def main():
    N = int(input())
    grid = [input().decode().strip() for _ in range(N)]

    M = N // BITS + 1  # num blocks
    bitsets = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            for k in range(BITS):
                idx = j * BITS + k
                if idx < N and grid[i][idx] == '1':
                    bitsets[i][j] |= 1 << k
    
    res = 0
    for i in range(N):
        for j in range(i):
            if grid[i][j] == '0': continue
            for k in range(M):
                res += popcount(bitsets[i][k] & bitsets[j][k])
    
    res //= 3
    print(res)


if __name__ == '__main__':
    main()

