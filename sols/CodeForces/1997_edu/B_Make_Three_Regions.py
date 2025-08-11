''' B. Make Three Regions
https://codeforces.com/contest/1997/problem/B
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

def solve(N, A, B):
    res = 0
    for i in range(1, N - 1):
        if A[i] == A[i - 1] == A[i + 1] == B[i] == '.' and B[i - 1] == B[i + 1] == 'x': res += 1
        if B[i] == B[i - 1] == B[i + 1] == A[i] == '.' and A[i - 1] == A[i + 1] == 'x': res += 1

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = input().decode().strip()
        B = input().decode().strip()
        res = solve(N, A, B)
        print(res)


if __name__ == '__main__':
    main()

