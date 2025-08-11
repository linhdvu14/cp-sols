''' B. Mirror in the String
https://codeforces.com/contest/1616/problem/B
'''

import io, os, sys
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

def solve(N, S):
    if N == 1 or S[0] <= S[1]: return S[0]*2
    for i in range(1, N):
        if S[i] > S[i-1]:
            S = S[:i]
            break
    return S + S[::-1]

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input().decode().strip()
        out = solve(N, S)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

