''' C. Double Sort
https://codeforces.com/contest/1681/problem/C
'''

import io, os, sys
from re import I
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

def solve(N, A, B):
    res = []
    for i in range(N):
        j = i 
        for j2 in range(i, N):
            if (A[j2], B[j2]) < (A[j], B[j]):
                j = j2
        if i != j:
            res.append((i+1, j+1))
            A[i], A[j] = A[j], A[i]
            B[i], B[j] = B[j], B[i]
    
    if B != sorted(B): return -1, []
    return len(res), res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        r1, r2 = solve(N, A, B)
        print(r1)
        for r in r2: print(*r)


if __name__ == '__main__':
    main()

