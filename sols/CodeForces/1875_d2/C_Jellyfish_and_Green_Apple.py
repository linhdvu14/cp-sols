''' C. Jellyfish and Green Apple
https://codeforces.com/contest/1875/problem/C
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
BITS = 30
from math import gcd

def solve(a, b):
    a %= b
    if not a: return 0

    g = gcd(a, b)
    a //= g
    b //= g
    if bin(b).count('1') != 1: return -1

    res = 0
    for i in range(BITS):
        if (a >> i) & 1 == 0: continue
        two = 1 << i
        res += two * (b // two - 1)

    return res * g


def main():
    T = int(input())
    for _ in range(T):
        a, b = list(map(int, input().split()))
        res = solve(a, b)
        print(res)


if __name__ == '__main__':
    main()

