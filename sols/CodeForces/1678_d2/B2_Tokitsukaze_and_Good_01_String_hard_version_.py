''' B2. Tokitsukaze and Good 01-String (hard version)
https://codeforces.com/contest/1678/problem/B2
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


def solve(N, A):
    res1 = res2 = 0
    prev = ''
    for i in range(0, N, 2):
        if A[i] != A[i+1]: 
            res1 += 1
        else:
            if A[i] != prev: res2 += 1
            prev = A[i]
    return res1, max(res2, 1)


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = input().decode().strip()
        out = solve(N, A)
        print(*out)


if __name__ == '__main__':
    main()

