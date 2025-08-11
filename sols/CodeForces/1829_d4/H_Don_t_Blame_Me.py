''' H. Don't Blame Me
https://codeforces.com/contest/1829/problem/H
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
MOD = 10**9 + 7
BITS = 6

def solve(N, K, A):
    dp = [0] * (1 << BITS)

    for a in A:
        ndp = dp[:]
        ndp[a] += 1
        for m in range(1 << BITS): ndp[m & a] = (ndp[m & a] + dp[m]) % MOD
        dp = ndp
    
    res = 0
    for m in range(1 << BITS):
        if bin(m).count('1') == K:
            res = (res + dp[m]) % MOD

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        res = solve(N, K, A)
        print(res)


if __name__ == '__main__':
    main()

