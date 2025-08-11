''' C. Division by Two and Permutation
https://codeforces.com/contest/1624/problem/C
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

from heapq import heapify, heappush, heappop

def solve(N, A):
    A = [-a for a in A]
    heapify(A)

    for mx in range(N, 0, -1):
        while -A[0] > mx:
            a = -heappop(A)
            a >>= 1
            heappush(A, -a)
        if -A[0] != mx: return False
        heappop(A)

    return True
    

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        print('YES' if out else 'NO')


if __name__ == '__main__':
    main()

