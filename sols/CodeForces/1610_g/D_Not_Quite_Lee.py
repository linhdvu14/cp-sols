''' D. Not Quite Lee
https://codeforces.com/contest/1610/problem/D
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

MOD = 10**9 + 7

# let S(k) = sum of k consecutive numbers = k(k+1)/2 mod k
# any odd k is good
# any subset containing an odd is good (concat all evens to odd)

# consider subsets containing only 2m
# any subset with nonzero, even number of 4m+2 is good:
# * good subset must have even number of 4m+2 (2m+1 mod 4m+2)
# * any pair (4m+2, 4n+2) sums to (2m+1) + (2n+1) - (4m+2)X - (4n+2)Y for some X, Y
#   by Bezout, there exists X, Y s.t. m+n+1 = (2m+1)X + (2n+1)Y i.e. pair sums to 0
# * all 4m can be concat to a 4m+2 to make 4m+2

# consider subsets containing only 4m
# any subset with nonzero, even number of 8m+4 is good

# ...

# https://codeforces.com/contest/1610/submission/136630106

BITS = 32

def solve(N, A):
    # cnt[p] = num elements with >= p powers of 2
    cnt = [0]*BITS
    for a in A:
        c = 0
        while a % 2 == 0:
            a //= 2
            cnt[c] += 1
            c += 1
        cnt[c] += 1
        
    # any subset containing odd is good
    res = (pow(2, cnt[0]-cnt[1], MOD) - 1) * pow(2, cnt[1], MOD) 
    res %= MOD

    # note num even-size subsets == num odd-size subsets
    for i in range(1, BITS-1):
        a = cnt[i] - cnt[i+1]  # 4m+2
        b = cnt[i+1]           # 4m
        if a > 0:
            res += (pow(2, a-1, MOD) - 1) * (pow(2, b, MOD))
            res %= MOD
    
    return res


def main():
    N = int(input())
    A = list(map(int, input().split()))
    out = solve(N, A)
    output(f'{out}\n')


if __name__ == '__main__':
    main()

