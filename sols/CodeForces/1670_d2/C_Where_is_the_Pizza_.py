''' C. Where is the Pizza?
https://codeforces.com/contest/1670/problem/C
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

MOD = 10**9 + 7

def solve(N, A, B, C):
    I = [-1] * N
    P = [-1] * N
    for i, (a, b) in enumerate(zip(A, B)):
        P[a-1] = b-1
        I[a-1] = i

    # count free cycles (no idx in C set)
    # each free cycle has 2 assignments
    cnt = 0
    used = [0] * N
    for i in range(N):
        if used[i]: continue
        free = True
        ln = 0
        while not used[i]:
            ln += 1
            free &= C[I[i]] == 0
            used[i] = 1
            i = P[i]
        if free and ln > 1: cnt += 1

    return pow(2, cnt, MOD)


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        C = list(map(int, input().split()))
        out = solve(N, A, B, C)
        print(out)


if __name__ == '__main__':
    main()

