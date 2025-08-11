''' The Lost Array
https://www.codechef.com/LTIME109A/problems/LOSTARRAY_
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

def check(N, A, B):
    x = 0
    for a in A: x ^= a
    C = [x]
    for a in A: C.append(x ^ a)
    assert sorted(C) == sorted(B), f'A={A} B={B} C={C}'


def solve(N, B):
    if N % 2 == 1:
        x = 0  # xor(A)
        for b in B: x ^= b
        res = [b ^ x for b in B if b != x]
        while len(res) < N: res.append(0)
    else:  # take random ele to be xor(A)
        res = [B[i] ^ B[0] for i in range(1, N+1)]

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        B = list(map(int, input().split()))
        A = solve(N, B)
        print(*A)


if __name__ == '__main__':
    main()

