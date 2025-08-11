''' E. PermutationForces II
https://codeforces.com/contest/1698/problem/E
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

# reorder (A, B) s.t. need to change A into 1..N

# at step i:
# - value i must be swapped with A[i] into correct pos
# - all j < i alr in correct pos, so A[i] = j >= i
# - if originally j = A[i], swap (i, A[i]) requires strength A[i] - i
# - if originally j = A[k] for some k < i
#   - step k swaps (k, A[k]), requires strength A[k] - k
#   - step i swaps (i, A[k]), requires strength A[k] - i < A[k] - k
# so min strength needed is max_i (A[i] - B[i])

# e.g.
# B: 1 2 3 4 5
# A: 3 4 2 5 1
#    1 4 2 5 3 -> requires 3 - 1
#    1 2 4 5 3 -> requires 4 - 2
#    1 2 3 5 4 -> requires 4 - 3 < 4 - 2
#    1 2 3 4 5 -> requires 5 - 4 < 5 - 3
# -> min strength is 2

from bisect import bisect_left
MOD = 998244353

def solve(N, S, A, B):
    rema = []
    remb = set(range(1, N+1))
    for (a, b) in zip(A, B):
        if b == -1: 
            rema.append(a)
        else:
            if a - b > S: return 0
            remb.remove(b)
    remb = sorted(list(remb))

    # for each a, count how many b satisfies b >= a - S
    cnt = [len(remb) - bisect_left(remb, a - S) for a in rema]
    cnt.sort()
    
    # greedily assign from largest a
    res = 1
    for i, c in enumerate(cnt):
        res = (res * (c - i)) % MOD

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, S = list(map(int, input().split()))
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        out = solve(N, S, A, B)
        print(out)


if __name__ == '__main__':
    main()

