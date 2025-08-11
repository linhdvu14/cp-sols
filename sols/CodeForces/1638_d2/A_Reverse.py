''' A. Reverse
https://codeforces.com/contest/1638/problem/A
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

def solve(N, P):
    start = -1
    for i, p in enumerate(P):
        if p != i + 1:
            start = i
            break
    
    if start == -1: return P

    end = N
    for i in range(start + 1, N):
        if P[i] == start + 1:
            end = i + 1
            break

    return P[:start] + P[start:end][::-1] + P[end:]



def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        P = list(map(int, input().split()))
        out = solve(N, P)
        print(*out)


if __name__ == '__main__':
    main()

