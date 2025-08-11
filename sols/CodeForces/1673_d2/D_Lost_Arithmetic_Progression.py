''' D. Lost Arithmetic Progression
https://codeforces.com/contest/1673/problem/D
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

MOD = 10**9 + 7

def factorize(n):
    '''return a sorted list of all distinct factors of n'''
    small, large = [], []
    for i in range(1, int(n**0.5) + 1, 2 if n & 1 else 1):
        if n % i == 0:
            small.append(i)
            large.append(n // i)
    if small[-1] == large[-1]: large.pop()
    return small + large[::-1]

def gcd(a, b):
    '''assume a, b >= 0'''
    if a < b: a, b = b, a
    while b > 0: a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def solve(B, C):
    b, q, y = B
    c, r, z = C
    lb, lc = b + q * (y-1), c + r * (z-1)

    if c < b or lc > lb or (c - b) % q != 0 or r % q != 0: return 0
    if c - r < b or lc + r > lb: return -1

    # a, p, x = A -> lcm(p, q) = r
    # c - r < a <= c, (c-a) % p == 0 -> r/p choices
    # lc <= la < lc + r, (la-lc) % p == 0 -> r/p choices
    res = 0
    factors = factorize(r)
    for p in factors:
        debug(p)
        if lcm(p, q) != r: continue
        res += pow(r//p, 2, MOD)

    return res % MOD


def main():
    T = int(input())
    for _ in range(T):
        B = list(map(int, input().split()))
        C = list(map(int, input().split()))
        out = solve(B, C)
        print(out)


if __name__ == '__main__':
    main()

