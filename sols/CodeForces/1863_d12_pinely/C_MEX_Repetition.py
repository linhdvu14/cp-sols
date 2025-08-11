''' C. MEX Repetition
https://codeforces.com/contest/1863/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def debug(*args):   
    if os.environ.get('debug') in [None, '0']: return
    from inspect import currentframe, getframeinfo
    from re import search
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

def solve(N, K, A):
    seen = set(A)
    miss = [a for a in range(N + 1) if a not in seen]
    heapify(miss)

    s = N * K // (N + 1) % N 
    A = A[-s:] + A[:-s]

    r = N * K % (N + 1)
    i = N * K // (N + 1) * (N + 1) % N
    for _ in range(r):
        mex = heappop(miss)
        if A[i] <= N: heappush(miss, A[i])
        A[i] = mex
        i = (i + 1) % N

    return A


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        res = solve(N, K, A)
        print(*res)


if __name__ == '__main__':
    main()
