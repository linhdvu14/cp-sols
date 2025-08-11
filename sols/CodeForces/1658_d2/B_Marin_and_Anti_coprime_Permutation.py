''' B. Marin and Anti-coprime Permutation
https://codeforces.com/contest/1658/problem/B
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

# can't have gcd >= 3 (1/3 vals to distribute into 2/3 pos)
# so can only have gcd == 2
# distribute even eles into odd pos, odd eles into even pos

MOD = 998244353

def solve(N):
    if N % 2 == 1: return 0
    f = 1
    for i in range(N//2):
        f = (f * (i+1)) % MOD
    return pow(f, 2, MOD)


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        out = solve(N)
        print(out)


if __name__ == '__main__':
    main()

