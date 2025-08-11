''' C. 3SUM Closure
https://codeforces.com/contest/1698/problem/C 
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

def solve(N, A):
    pos = neg = zero = 0
    for a in A: 
        if a < 0: neg += 1
        elif a > 0: pos += 1
        else: zero += 1
    if pos >= 3 or neg >=3: return 'NO'

    known = set(A)
    A = [a for a in A if a != 0]
    for i in range(len(A)):
        for j in range(i):
            if zero and A[i] + A[j] not in known: return 'NO'
            for k in range(j):
                if A[i] + A[j] + A[k] not in known: return 'NO'

    return 'YES'


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        print(out)


if __name__ == '__main__':
    main()

