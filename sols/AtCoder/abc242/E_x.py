''' E - (∀x∀)
https://atcoder.jp/contests/abc242/tasks/abc242_e
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

def solve(N, S):
    S = [ord(c) - ord('A') for c in S]
    res = 0

    # X[:i] == S[:i], X[i] < S[i]
    for i in range(N//2):    
        rem = (N + 1) // 2 - i - 1
        res = (res + S[i] * pow(26, rem, MOD)) % MOD
    
    if N % 2 == 1: res += S[N//2]
    if S[:N//2][::-1] <= S[-(N//2):]: res += 1

    return res % MOD


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = list(input().decode().strip())
        out = solve(N, S)
        print(out)


if __name__ == '__main__':
    main()

