''' DMOPC '21 Contest 10 P2 - Cycle Sort
https://dmoj.ca/problem/dmopc21c10p2
'''

import os, sys
input = sys.stdin.readline  # strip() if str

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
    if N == 1: return [1]
    if N == 2: return [1, 2]
    lookup = {a: i for i, a in enumerate(A)}

    for i, a in enumerate(A):
        if a != 1: continue

        # swap 1 with 2 if have (2, 1)
        cand1 = A[:]
        if A[(i - 1) % N] == 2:
            A[(i - 1) % N], A[i] = A[i], A[(i - 1) % N]
            cand1 = [A[(i - 1 + d) % N] for d in range(N)]
            A[(i - 1) % N], A[i] = A[i], A[(i - 1) % N]

        # move 1 before 2
        for j in range(N):
            if A[(i + j) % N] == 2:
                A[(i + j - 1) % N], A[i] = A[i], A[(i + j - 1) % N]
                cand2 = [A[(i + j - 1 + d) % N] for d in range(N)]
                A[(i + j - 1) % N], A[i] = A[i], A[(i + j - 1) % N]
                break

        # move 2, 3, ... in order
        for j in range(N):
            if A[(i + j) % N] != j + 1:
                k = lookup[j + 1]
                A[(i + j) % N], A[k] = A[k], A[(i + j) % N]
                break
        cand3 = [A[(i + j) % N] for j in range(N)]

        return min(cand1, cand2, cand3)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    out = solve(N, A)
    print(*out)


if __name__ == '__main__':
    main()

