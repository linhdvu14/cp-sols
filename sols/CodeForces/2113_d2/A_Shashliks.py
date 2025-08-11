''' A. Shashliks
https://codeforces.com/contest/2113/problem/A
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

def solve(K, A, B, X, Y):
    choices = sorted([(X, -A), (Y, -B)])
    res = 0
    for x, a in choices:
        a = -a
        if K < a: continue 
        n = (K - a) // x + 1
        res += n 
        K -= x * n

    return res


def main():
    T = int(input())
    for _ in range(T):
        K, A, B, X, Y = list(map(int, input().split()))
        res = solve(K, A, B, X, Y)
        print(res)


if __name__ == '__main__':
    main()

