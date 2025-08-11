''' B. GCD Arrays
https://codeforces.com/contest/1629/problem/B
'''

import io, os, sys
from tkinter.tix import Tree
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

def solve(L, R, K):
    if L == R: return L > 1
    if K == 0: return False
    if K == R-L: return True

    N = R - L + 1 - K  # min num components after applying K ops
    c2 = ((R//2)*2 - ((L+1)//2)*2) // 2 + 1
    c3 = ((R//3)*3 - ((L+2)//3)*3) // 3 + 1

    return c2 >= N or c3 >= N



def main():
    T = int(input())
    for _ in range(T):
        L, R, K = list(map(int, input().split()))
        out = solve(L, R, K)
        print('YES' if out else 'NO')


if __name__ == '__main__':
    main()

