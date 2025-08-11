''' D. K-good
https://codeforces.com/contest/1656/problem/D
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

# need n % k = k(k-1)/2, k small s.t. n >= k(k-1)/2 or k(k-1) <= 2n
# if k = 2l+1, then n % k = 0 -> k is odd divisor of n
# if k = 2l, then n % (2l) = l -> n = l * odd 
# min such k is a = all powers of 2 of 2n
# if a(a-1)/2 > n, then b(b-1)/2 <= n where b = 2n/a 
# so take k = min(a, b)

def solve_1(N):
    if N % 2 == 1: return 2
    a, b = 1, N
    while b % 2 == 0:
        a *= 2
        b //= 2
    if b == 1: return -1
    return min(b, 2*a)


# k^2 + (2m-1)k - 2n = 0
# k = (p-2m+1)/2 for p = sqrt((2m-1)^2 + 8n)
# 8n = (p + 2m - 1) * (p - 2m + 1) = a * b
# need: a even, b even, b >= 4, (a-b) // 2 odd

def solve_2(N):
    if N % 2 == 1: return 2
    N *= 8
    a = N
    while a % 2 == 0: a //= 2
    a *= 2
    b = N // a
    if a > b: a, b = b, a
    return a//2 if a > 2 else -1


solve = solve_1

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        out = solve(N)
        print(out)


if __name__ == '__main__':
    main()

