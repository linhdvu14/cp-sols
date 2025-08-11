''' E. Median String
https://codeforces.com/contest/1144/problem/E 
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

BASE = 26

def solve(N, A, B):
    A = [ord(c) - ord('a') for c in A]
    B = [ord(c) - ord('a') for c in B]

    # C = B - A
    C = [0] * N
    carry = 0
    for i in range(N-1, -1, -1):
        C[i] = B[i] - A[i] - carry
        carry = 0
        if C[i] < 0: 
            C[i] += BASE
            carry = 1
    
    # C /= 2
    for i in range(N):
        C[i], r = divmod(C[i], 2)
        if r: C[i + 1] += r * BASE

    # A += C
    carry = 0
    for i in range(N-1, -1, -1):
        A[i] = A[i] + C[i] + carry
        carry = 0
        if A[i] >= BASE:
            A[i] -= BASE
            carry = 1

    return ''.join(chr(j + ord('a')) for j in A)


def main():
    N = int(input())
    A = input().decode().strip()
    B = input().decode().strip()
    out = solve(N, A, B)
    print(out)


if __name__ == '__main__':
    main()

