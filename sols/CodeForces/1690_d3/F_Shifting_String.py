''' F. Shifting String
https://codeforces.com/contest/1690/problem/F
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

from math import gcd

def lcm(a, b): return a * b // gcd(a, b)

def solve(N, A, P):
    def find_period(B):
        M = len(B)
        for p in range(1, M):
            for i in range(M):
                if B[i] != B[(i + p) % M]: break
            else: return p
        return M

    res = 1
    used = [0] * N
    for i, p in enumerate(P):
        if used[i]: continue
        B = []
        while not used[i]:
            B.append(A[i])
            used[i] = 1
            i = P[i] - 1
        p = find_period(B)
        res = lcm(res, p)
        
    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = input().decode().strip()
        P = list(map(int, input().split()))
        out = solve(N, A, P)
        print(out)


if __name__ == '__main__':
    main()

