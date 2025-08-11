''' A. Div. 7
https://codeforces.com/contest/1633/problem/A
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
    if N % 7 == 0: return N
    base = N - N % 10
    for i in range(10):
        if (base + i) % 7 == 0:
            return base + i


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        out = solve(N)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

