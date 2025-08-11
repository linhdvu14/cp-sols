''' C. Make Equal With Mod
https://codeforces.com/contest/1656/problem/C
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

# if 1 not in A, can make all vals 0 by repeatedly picking max nonzero val
# if 1 in A, need to make all vals 1

def solve(N, A):
    A = set(A)
    if len(A) == 1 or 1 not in A: return True
    A = sorted(list(A), reverse=True)
    return all(a - b != 1 for a, b in zip(A, A[1:]))


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        print('YES' if out else 'NO')


if __name__ == '__main__':
    main()
 