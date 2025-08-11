''' D. Deleting Divisors
https://codeforces.com/contest/1537/problem/D
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

# all odds lose
# all evens except 2^odd win
def brute(N):
    win = [0] * (N + 1)
    for n in range(2, N+1):
        if win[n]: continue
        d = 1
        while d * d < n:
            if n % d == 0:
                if d > 1 and n + d <= N: win[n + d] = 1
                if n + n//d <= N: win[n + n//d] = 1
            d += 1
        if d * d == n and n + d <= N: win[n + d] = 1
    even_lose = [i for i in range(2, N+1, 2) if not win[i]]
    odd_win = [i for i in range(1, N+1, 2) if win[i]]
    print(even_lose)
    print(odd_win)


# proof by induction https://codeforces.com/blog/entry/91835?#comment-805791
# win state: even and not power of 2 -> odd -> even and not power of 2
def solve(N):
    if N % 2: return 'Bob'
    if bin(N).count('1') == 1 and bin(N).count('0') % 2 == 0: return 'Bob'
    return 'Alice'


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        out = solve(N)
        print(out)


if __name__ == '__main__':
    main()

