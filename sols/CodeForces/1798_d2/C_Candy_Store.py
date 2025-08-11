''' C. Candy Store
https://codeforces.com/contest/1798/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def debug(*args):   
    if os.environ.get('debug') in [None, '0']: return
    from inspect import currentframe, getframeinfo
    from re import search
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')

INF = float('inf')

# -----------------------------------------

from math import gcd

def solve(N, pairs):
    res = 0
    a1, b1 = 0, 1
    for a2, b2 in pairs:
        lcm = b1 * b2 // gcd(b1, b2)
        m1, m2 = lcm // b1, lcm // b2 
        if a1 % m1 or a2 % m2:
            res += 1
            a1, b1 = a2, b2
        else:
            a1, b1 = gcd(a1 // m1, a2 // m2), lcm
    res += 1

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        pairs = [list(map(int, input().split())) for _ in range(N)]
        res = solve(N, pairs)
        print(res)


if __name__ == '__main__':
    main()

