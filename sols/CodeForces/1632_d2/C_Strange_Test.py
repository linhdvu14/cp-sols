''' C. Strange Test
https://codeforces.com/contest/1632/problem/C
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

def solve(a, b):
    res = b - a
    # turn a -> na, b -> min nb s.t. na | nb == nb
    for na in range(a, b):
        nb = na
        for i in range(31, -1, -1):
            if nb >= b: break
            if (b >> i) & 1 == 1 and (nb >> i) & 1 == 0:
                nb |= 1 << i
        res = min(res, na - a + nb - b + 1)
    return res

def main():
    T = int(input())
    for _ in range(T):
        a, b = list(map(int, input().split()))
        out = solve(a, b)
        output(f'{out}\n')


if __name__ == '__main__':
    main()


