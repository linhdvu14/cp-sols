''' D. Repetitions Decoding
https://codeforces.com/contest/1642/problem/D
'''

import io, os, sys
from tkinter import E
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

def solve(N, A):
    # iteratively remove (A[0], A[i]) pair where i > 0 is idx of first occurrence of A[0]
    # abcda|... -> abcda|bcddcb|... -> abcdabcd|dcb|... -> ...|dcb|...
    ops, lens = [], []
    offset = 0
    while A:
        # abcd|a...
        j = 1
        while j < len(A) and A[j] != A[0]: j += 1
        if j == len(A): return -1, [], []

        # abcd|a|bcddcb...
        for k in range(1, j):
            ops.append((offset + j + k, A[k]))
        lens.append(2 * j)

        # abcdabcd|dcb... <-> aa|dcb...
        A = A[1:j][::-1] + A[j+1:]
        offset += lens[-1]

    return len(ops), ops, lens


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        n, r1, r2 = solve(N, A)
        if n == -1: print(-1)
        else:
            print(len(r1))
            for t in r1: print(*t)
            print(len(r2))
            print(*r2)

if __name__ == '__main__':
    main()

