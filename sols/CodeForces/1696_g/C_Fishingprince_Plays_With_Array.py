''' C. Fishingprince Plays With Array
https://codeforces.com/contest/1696/problem/C
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

def factorize(A, M):
    res = []
    for a in A:
        cnt = 1
        while a % M == 0:
            cnt *= M 
            a //= M
        if res and res[-1][0] == a: res[-1][1] += cnt 
        else: res.append([a, cnt])
    return res


def solve(N, M, A, K, B):
    A = factorize(A, M)
    B = factorize(B, M)
    return 'Yes' if A == B else 'No'


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        A = list(map(int, input().split()))
        K = int(input())
        B = list(map(int, input().split()))
        out = solve(N, M, A, K, B)
        print(out)


if __name__ == '__main__':
    main()

