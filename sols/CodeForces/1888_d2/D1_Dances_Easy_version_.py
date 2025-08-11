''' D1. Dances (Easy version)
https://codeforces.com/contest/1888/problem/D1
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

def solve(N, M, A, B):
    A = sorted([1] + A)
    B.sort()

    def find(val, i):
        lo, hi, idx = i, N - 1, -2
        while lo <= hi: 
            mi = (lo + hi) // 2
            if B[mi] > val:
                idx = mi 
                hi = mi - 1
            else:
                lo = mi + 1
        return idx

    start = 0
    for i, a in enumerate(A):
        start = find(a, start) + 1
        if start == -1: return N - i

    return 0


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        res = solve(N, M, A, B)
        print(res)


if __name__ == '__main__':
    main()

