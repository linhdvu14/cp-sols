''' C. GCD Grindset
https://tlx.toki.id/contests/troc-25/problems/C
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

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

# let a = m, b = m + 2 where m odd
# then g = 1, l = ab = m(m+2)

# (a + b) * N = g + l
# (2m + 2) * N = (m + 1)^2
# m = 2*N - 1

def solve(N):
    return 2*N - 1, 2*N + 1
    

def main():
    N = int(input())
    out = solve(N)
    print(*out)


if __name__ == '__main__':
    main()

