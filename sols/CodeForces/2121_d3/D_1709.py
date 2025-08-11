''' D. 1709
https://codeforces.com/contest/2121/problem/D
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

def bubble(N, A, op):
    ops = []
    for i in range(N - 1):
        _, mni = min((A[j], j) for j in range(i, N))
        if i == mni: continue
        for j in range(mni - 1, i - 1, -1):
            ops += [(op, j + 1)]
            A[j], A[j + 1] = A[j + 1], A[j]
    return ops, A


def solve(N, A, B):
    ops_A, A = bubble(N, A, 1)
    ops_B, B = bubble(N, B, 2)
    res = ops_A + ops_B
    for i, (a, b) in enumerate(zip(A, B)):
        if a < b: continue
        res += [(3, i + 1)]
    
    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        res = solve(N, A, B)
        print(len(res))
        for op in res: print(*op)


if __name__ == '__main__':
    main()

