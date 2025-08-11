''' D. Madoka and the Best School in Russia
https://codeforces.com/contest/1647/problem/D
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

def is_prime(n):
    '''Miller-Rabin primality test'''
    if n < 5 or n & 1 == 0 or n % 3 == 0: return 2 <= n <= 3
    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p == 1 or p == n - 1 or a % n == 0: continue
        for _ in range(s):
            p = (p * p) % n
            if p == n - 1: break
        else: return False
    return True


def solve(x, d):
    cnt = 0
    while x % d == 0:
        cnt += 1
        x //= d
    if cnt < 2: return False
    if x > 1 and not is_prime(x): return True
    if cnt == 2: return False
    if x == 1: return not is_prime(d)
    if cnt > 3: return not is_prime(d)

    # cnt == 3, x prime
    k1 = 2
    while k1*k1 <= d:
        k2, r = divmod(d, k1)
        if r == 0 and (x * k1) % d != 0 or (x * k2) % d != 0: return True
        k1 += 1
    return False


def main():
    T = int(input())
    for _ in range(T):
        x, d = list(map(int, input().split()))
        out = solve(x, d)
        print('YES' if out else 'NO')


if __name__ == '__main__':
    main()

