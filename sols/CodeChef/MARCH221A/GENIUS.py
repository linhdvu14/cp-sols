''' Exact Marks
https://www.codechef.com/MARCH221A/problems/GENIUS
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

def solve(N, X):
    if X == 0: return 'YES', [0, 0, N]
    if X < 0: return ('NO', []) if N < X else ('YES', [0, 0, X])
    a = (X+2) // 3
    b = 3*a - X
    return ('NO', []) if a+b > N else ('YES', [a, b, N-a-b])


def main():
    T = int(input())
    for _ in range(T):
        N, X = list(map(int, input().split()))
        r1, r2 = solve(N, X)
        print(r1)
        if r2: print(*r2)


if __name__ == '__main__':
    main()

