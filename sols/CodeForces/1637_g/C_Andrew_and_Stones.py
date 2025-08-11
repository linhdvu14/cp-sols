''' C. Andrew and Stones
https://codeforces.com/contest/1637/problem/C
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

# each middle odd can be made even by another non-1 odd
# then it can be used to fix another middle odd if needed
# so can fix all middle odds as long as there's one middle non-1 odd
# total cost is sum(middle) // 2 + num middle odds

def solve(N, A):
    if N == 3 and A[1] % 2 == 1: return -1
    if all(a == 1 for a in A[1:-1]): return -1
    return sum((a+1) // 2 for a in A[1:-1])


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

