''' G - Cubic?
https://atcoder.jp/contests/abc238/tasks/abc238_g
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

MAX = 10**6

# mo's algorithm
def main_tle():
    N, Q = map(int, input().split())

    # lpf
    lpf = [0] * (MAX + 1)
    primes = []
    for i in range(2, MAX + 1):
        if lpf[i] == 0:
            lpf[i] = i
            primes.append(i)
        for p in primes:
            if p > lpf[i] or i * p > MAX: break
            lpf[i * p] = p
  
    # count prime factors
    A = list(map(int, input().split()))
    factors = {}
    for a in A:
        if a in factors: continue
        mp = {}
        t = a
        while t > 1:
            mp[lpf[t]] = (mp.get(lpf[t], 0) + 1) % 3
            t //= lpf[t]
        factors[a] = mp
    
    # mo's
    queries = [tuple(map(int, input().split())) for _ in range(Q)]
    idx = sorted(list(range(Q)), key=lambda i: (queries[i][0] // int(N**0.5), queries[i][1]))
    
    def mo_add(a):
        for f, c in factors[a].items():
            cnt[f] = (cnt.get(f, 0) + c) % 3
            if cnt[f] == 0: cnt.pop(f)
    def mo_remove(a):
        for f, c in factors[a].items():
            cnt[f] = (cnt.get(f, 0) - c) % 3
            if cnt[f] == 0: cnt.pop(f)

    res = ['No'] * Q
    l, r = 0, -1
    cnt = {}  # reflect l..r
    for i in idx:
        ql, qr = queries[i]
        ql -= 1
        qr -= 1
        while l > ql:
            l -= 1
            mo_add(A[l])
        while r < qr:
            r += 1
            mo_add(A[r])
        while l < ql:
            mo_remove(A[l])
            l += 1
        while r > qr:
            mo_remove(A[r])
            r -= 1
        if len(cnt) == 0: res[i] = 'Yes'
    
    print('\n'.join(res))



# xor hash
# assign each prime p 3 random large ints: X[p] = [x1, x2, x1^x2]
# calc hash H[i] = XOR_p X[p][j%3], over all prime factor p of A[i], j = num occurrences of p in prefix A[..i] with dup
# if A[l] x ... x A[r] is cubic, then H[l] ^ ... ^ H[r] = 0

from random import randint
from collections import defaultdict

def main_ac():
    # gen X
    MAX_INT = (1 << 64) - 1
    X = {}
    lpf = [0] * (MAX + 1)
    primes = []
    for i in range(2, MAX + 1):
        if lpf[i] == 0:
            lpf[i] = i
            primes.append(i)
            x1 = randint(0, MAX_INT)
            x2 = randint(0, MAX_INT)
            X[i] = [x1, x2, x1^x2]
        for p in primes:
            if p > lpf[i] or p*i > MAX: break
            lpf[p*i] = p

    # gen H
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    H = [0] * N
    cnt = defaultdict(int)
    for i, a in enumerate(A):
        while a > 1:
            p = lpf[a]
            cnt[p] = (cnt[p] + 1) % 3
            H[i] ^= X[p][cnt[p] % 3]
            a //= p
    
    # prefix xor
    pref = [1] * (N+1)
    for i, h in enumerate(H): pref[i + 1] = pref[i] ^ h
    
    # query
    res = ['No'] * Q
    for i in range(Q):
        l, r = map(int, input().split())
        xor = pref[r] ^ pref[l-1]
        if xor == 0: res[i] = 'Yes'
    
    print('\n'.join(res))


main = main_ac


if __name__ == '__main__':
    main()

