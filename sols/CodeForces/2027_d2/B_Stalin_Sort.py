''' B. Stalin Sort
https://codeforces.com/contest/2027/problem/B
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

from inspect import currentframe, getframeinfo
from re import search
DEBUG = os.environ.get('debug') not in [None, '0']

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
    res = N
    for i, a in enumerate(A):
        cand = i + sum(1 for j in range(i + 1, N) if A[j] > a)
        res = min(res, cand)

    return res

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        res = solve(N, A)
        print(res)


if __name__ == '__main__':
    main()

