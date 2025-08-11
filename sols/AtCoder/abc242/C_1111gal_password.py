''' C - 1111gal password
https://atcoder.jp/contests/abc242/tasks/abc242_c
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

MOD = 998244353

def main():
    N = int(input())
    dp = [0] + [1] * 9
    for _ in range(N-1):
        ndp = [0] * 10
        for i in range(1, 10):
            for j in range(i-1, i+2):
                if 1 <= j <= 9: 
                    ndp[i] += dp[j]
        for i in range(10): dp[i] = ndp[i] % MOD
    
    print(sum(dp) % MOD)



if __name__ == '__main__':
    main()

