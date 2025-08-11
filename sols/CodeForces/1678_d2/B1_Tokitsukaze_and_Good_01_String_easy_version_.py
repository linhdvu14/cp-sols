''' B1. Tokitsukaze and Good 01-String (easy version)
https://codeforces.com/contest/1678/problem/B1
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

# iff S[i] == S[i+1] for i%2 == 0

def solve(N, A):
    res = 0
    for i in range(0, N, 2):
        if A[i] != A[i+1]:
            res += 1
    return res



def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = input().decode().strip()
        out = solve(N, A)
        print(out)


if __name__ == '__main__':
    main()

