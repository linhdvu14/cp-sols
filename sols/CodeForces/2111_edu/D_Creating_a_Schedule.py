''' D. Creating a Schedule
https://codeforces.com/contest/2111/problem/D
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
def solve(N, M, A):
    A.sort(key=lambda a: a // 100)
    
    if N == 1: return [[A[0], A[-1]] * 3]

    res = [[0] * 6 for _ in range(N)]
    for c in range(6):
        for i in range(N // 2):
            res[i][c] = A[i] if c % 2 else A[-1 - i]
            res[-1 - i][c] = A[-1 - i] if c % 2 else A[i]
        if N % 2:
            res[N // 2][c] = A[N // 2] if c % 2 else A[-1 - N // 2]

    return res



def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        A = list(map(int, input().split()))
        res = solve(N, M, A)
        for r in res: print(*r)


if __name__ == '__main__':
    main()

