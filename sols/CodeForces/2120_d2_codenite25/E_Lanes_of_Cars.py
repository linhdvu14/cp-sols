''' E. Lanes of Cars
https://codeforces.com/contest/2120/problem/E
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

def solve(N, K, A):
    if N == 1: return A[0] * (A[0] + 1) // 2

    A.sort()
    ps1 = [0] * (N + 1)
    ps2 = [0] * (N + 1)
    for i, a in enumerate(A):
        ps1[i] = ps1[i - 1] + a
        ps2[i] = ps2[i - 1] + a * (a + 1) // 2

    def f(op):
        res = 0

        for i in range(1, N):
            need = A[i] * i - ps1[i - 1]
            if need >= op:
                h, r = divmod(op + ps1[i - 1], i)
                res -= r * (h + 1) * (h + 2) // 2 + (i - r) * h * (h + 1) // 2 - ps2[i - 1]
                break 
        else: 
            return -INF
        
        for i in range(N - 2, -1, -1):
            need = ps1[N - 1] - ps1[i] - A[i] * (N - i - 1)
            if need >= op:
                h, r = divmod(op - ps1[N - 1] + ps1[i], N - i - 1)
                res -= r * (h + 1) * h // 2 + (N - i - 1 - r) * h * (h - 1) // 2 - (ps2[N - 1] - ps2[i])
                break 
        else:
            return -INF
        
        return res - K * op
    

    lo, hi = 0, sum(A)
    while lo < hi:
        mi = (lo + hi) // 2
        if f(mi) >= f(mi + 1):
            hi = mi 
        else:
            lo = mi + 1

    res = sum(a * (a + 1) // 2 for a in A) - f(lo)
    return res



def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        res = solve(N, K, A)
        print(res)


if __name__ == '__main__':
    main()

