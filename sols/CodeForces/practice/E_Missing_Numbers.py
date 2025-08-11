''' E. Missing Numbers
https://codeforces.com/contest/1081/problem/E
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

# let A[0] + ... + A[i] = B[i]^2, then
# A[0] = B[0]^2           --> free
# A[1] = B[1]^2 - B[0]^2  --> fixed
# A[2] = B[2]^2 - B[1]^2  --> free; need B[2] > B[1]
# A[3] = B[3]^2 - B[2]^2  --> fixed
# A[4] = B[4]^2 - B[3]^2  --> free; need B[4] > B[3]
# A[5] = B[5]^2 - B[4]^2  --> fixed

def solve(N, A):
    B = [0] * N
    for i, a in enumerate(A):
        cands = []  # possible (B[2i], B[2i+1]) pairs
        d1 = 1
        while d1 * d1 < a:
            d2, r = divmod(a, d1)
            if r == 0 and (d1 - d2) % 2 == 0: cands.append(((d2 - d1) // 2, (d2 + d1) // 2))
            d1 += 1
        
        # pick min B[2i+1] s.t. B[2i] > B[2i-1]
        cands.reverse()
        prev = -1 if i == 0 else B[2*i - 1]
        idx, lo, hi = -1, 0, len(cands) - 1
        while lo <= hi:
            mi = (lo + hi) // 2
            if cands[mi][0] > prev:
                idx = mi 
                hi = mi - 1
            else:
                lo = mi + 1
        
        if idx == -1: return []
        B[2*i], B[2*i + 1] = cands[idx]

    res = [0] * N
    for i in range(N):
        if i == 0: res[i] = B[0]**2
        elif i % 2 == 0: res[i] = B[i]**2 - B[i-1]**2
        else: res[i] = A[i//2]

    return res


def main():
    N = int(input())
    A = list(map(int, input().split()))
    out = solve(N, A)
    if out: 
        print('Yes')
        print(*out)
    else:
        print('No')


# s * d = p
# a = (s + d) / 2, b = (s - d) / 2
# (a, b) big when s >> d; small when s close to d
def gen():
    def pairs(a):
        cands = []
        d1 = 1
        while d1 * d1 < a:
            d2, r = divmod(a, d1)
            if r == 0 and (d1 - d2) % 2 == 0: cands.append((d1, d2, (d2 - d1) // 2, (d2 + d1) // 2))
            d1 += 1
        return cands
    
    for a in range(1, 100):
        p = pairs(a)
        p.reverse()
        if len(p) > 2:
            print(a, end=':\t')
            print(*p, sep=' | ')


if __name__ == '__main__':
    # main()
    gen()

