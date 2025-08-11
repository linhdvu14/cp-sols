''' Find A, B, C
https://www.codechef.com/JULY221A/problems/FINDABC
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

# 4 7 2
# a + b + c = 4
# a^1 + b^1 + c^1 = 7 --> 3 have pos 0 = 0
# a^2 + b^2 + c^2 = 2 --> 2 have pos 1 = 1 (-4), 1 have pos 1 = 0 (+2)

def solve(N, F):
    res = [0] * 3
    for b in range(16, -1, -1):
        if (1 << b) > N: continue
        diff = (F[1 << b] - F[0]) >> b 
        ones = 3 if diff == -3 else 2 if diff == -1 else 1 if diff == 1 else 0
        for i in range(ones): res[i] |= 1 << b
        res.sort()
   
    check(N, F, res[0], res[1], res[2])
    return res


def check(N, F, a, b, c):
    assert 0 <= min(a, b, c) <= max(a, b, c) <= N, f'{a} {b} {c} {N}'
    for i, f in enumerate(F): assert (a^i) + (b^i)+ (c^i) == f, f'{a} {b} {c} {i} {f}'


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        F = list(map(int, input().split()))
        out = solve(N, F)
        print(*out)



if __name__ == '__main__':
    main()

