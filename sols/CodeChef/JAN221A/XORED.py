''' Retrieve back the Array
https://www.codechef.com/JAN221A/problems/XORED
'''

import io, os, sys
import re
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

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

MAX = 5*10**5
BOUND = 3*10**5

def solve(N, X):
    # padding quadruples: [4,5,6,7], [8,9,10,11], ... except the one containing X
    pad = [4*(i+1)+j for i in range(N//4 + 3) for j in range(4) if i+1 != X//4]
    pad = pad[:(N-N%4)]

    # xor == X and not included in pad
    triple = [X-X%4+i for i in range(4) if X-X%4+i != X]
    if X == 1: triple = [BOUND, BOUND|2, 3]
    if X == 2: triple = [BOUND, BOUND|1, 3]
    if X == 3: triple = [BOUND, BOUND|1, 2]
    if X == MAX: triple = [int('0b1111010000000000000', 2), int('0b1111000000100000000', 2), int('0b1111000000000100000', 2)]

    if N % 4 == 0: return pad[:-4] + [0] + triple
    if N % 4 == 1: return pad + [X]
    if N % 4 == 2: return pad + [0, X]
    return pad + triple


def main():
    T = int(input())
    for _ in range(T):
        N, X = list(map(int, input().split()))
        out = solve(N, X)
        print(*out)


if __name__ == '__main__':
    main()

