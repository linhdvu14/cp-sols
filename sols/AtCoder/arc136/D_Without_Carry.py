''' D - Without Carry
https://atcoder.jp/contests/arc136/tasks/arc136_d
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

# multi-dimensional sos dp
# https://atcoder.jp/contests/arc136/submissions/29769184
# https://atcoder.jp/contests/arc136/submissions/29766133

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MAX = 10**6

    # dp[n] = num eles in A with all digits <= corresponding digits of n
    dp = [0] * MAX

    # num eles <= n, that may differ from n in last 0 digits
    for n in A: dp[n] += 1

    # num eles <= n, that may differ from n in last i=1..6 digits
    for i in range(6):
        for n in range(MAX):
            d = n // (10**i) % 10
            if d > 0: dp[n] += dp[n - 10**i]  # P[d]S -> P[d-1]S

    res = 0
    for a in A:
        b = 0
        for i in range(5, -1, -1): b = 10*b + 9 - a // (10**i) % 10
        res += dp[b]
        bad = True  # whether a <= b in all pos
        for i in range(5, -1, -1):
            da = a // (10**i) % 10
            db = b // (10**i) % 10
            if da > db: bad = False
        if bad: res -= 1
    return res // 2


if __name__ == '__main__':
    out = main()
    print(out)

