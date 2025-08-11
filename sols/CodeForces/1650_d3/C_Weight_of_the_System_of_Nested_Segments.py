''' C. Weight of the System of Nested Segments
https://codeforces.com/contest/1650/problem/C
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

def solve(N, M, P):
    P.sort()
    P = [(x, i, w) for w, x, i in P[:2*N]]
    P.sort()

    print(sum([p[2] for p in P]))
    for i in range(N):
        print(P[i][1]+1, P[-1-i][1]+1)
    print()


def main():
    T = int(input())
    for _ in range(T):
        _ = input()
        N, M = list(map(int, input().split()))
        P = []
        for i in range(M):
            x, w = list(map(int, input().split()))
            P.append((w, x, i))
        solve(N, M, P)


if __name__ == '__main__':
    main()

