''' C. Make it Increasing
https://codeforces.com/contest/1668/problem/C
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
    res = INF

    # make B[i] zero
    for i in range(N):
        cand = 0
        prev = 0
        for j in range(i-1, -1, -1):
            t = (A[j] - prev) // A[j]
            cand += t
            prev = -A[j] * t
        prev = 0
        for j in range(i+1, N):
            t = (prev + A[j]) // A[j]
            cand += t
            prev = A[j] * t
        res = min(res, cand)
    
    return res



def main():
    N = int(input())
    A = list(map(int, input().split()))
    out = solve(N, A)
    print(out)


if __name__ == '__main__':
    main()

