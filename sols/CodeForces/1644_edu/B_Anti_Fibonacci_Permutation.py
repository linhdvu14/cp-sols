''' B. Anti-Fibonacci Permutation
https://codeforces.com/contest/1644/problem/B
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

def solve(N):
    if N == 3:
        print('3 2 1\n1 3 2\n3 1 2')
    else:
        A = list(range(N, 0, -1))
        for _ in range(N):
            print(*A)
            A = A[1:] + [A[0]]


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        solve(N)


if __name__ == '__main__':
    main()

