''' D. Matrix game
https://codeforces.com/contest/2120/problem/D
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
MOD = 10**9 + 7

def nCk(n, a): 
    res = 1
    for i in range(n, n - a, -1):
        res = res * i % MOD
    for i in range(2, a + 1):
        res = res * pow(i, MOD - 2, MOD) % MOD
    return res 


def solve(a, b, k):
    n = (a - 1) * k + 1
    m = k * nCk(n, a) * (b - 1) + 1
    return n % MOD, m % MOD


def main():
    T = int(input())
    for _ in range(T):
        a, b, k = list(map(int, input().split()))
        res = solve(a, b, k)
        print(*res)


if __name__ == '__main__':
    main()

