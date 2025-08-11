''' A. Energy Crystals
https://codeforces.com/contest/2111/problem/A
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

def solve(X):
    res = a = 0
    while a < X:
        a = min(a * 2 + 1, X)
        res += 2
    return res + 1


def main():
    T = int(input())
    for _ in range(T):
        X = int(input())
        res = solve(X)
        print(res)


if __name__ == '__main__':
    main()
