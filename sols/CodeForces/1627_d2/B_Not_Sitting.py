''' B. Not Sitting
https://codeforces.com/contest/1627/problem/B
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

# T picks side, R picks center
def solve(R, C):
    dists = [max(r+c, R-r+C-c-2, R-r+c-1, r+C-c-1) for r in range(R) for c in range(C)]
    dists.sort()
    return dists


def main():
    T = int(input())
    for _ in range(T):
        R, C = list(map(int, input().split()))
        out = solve(R, C)
        print(*out)


if __name__ == '__main__':
    main()

